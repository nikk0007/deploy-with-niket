import asyncio
import time
import aiohttp
# third-party library for async HTTP requests (pip install aiohttp)
# regular 'requests' library is blocking — aiohttp is its non-blocking equivalent


# ─────────────────────────────────────────────
# COROUTINE 1: fetch a single endpoint
# ─────────────────────────────────────────────

async def fetch_metrics(session, endpoint):
    # 'session' is the shared aiohttp.ClientSession passed in from main()
    # 'endpoint' is the URL string this particular coroutine will hit

    async with session.get(endpoint) as response:
        # 'session.get(endpoint)' sends a non-blocking HTTP GET request
        #
        # 'async with' is used here because:
        #   - the HTTP response is a resource that must be properly opened and closed
        #   - 'async with' is the async version of regular 'with'
        #   - it automatically closes the response connection when the block exits
        #   - the 'await' is built into 'async with' — it pauses this coroutine
        #     until the response headers arrive, letting other coroutines run meanwhile
        #
        # 'as response' gives us the response object to read status, headers, body etc.

        print(f"Got response from {endpoint} | Status: {response.status}")
        # response.status → HTTP status code (200 = OK, 404 = Not Found, etc.)


# ─────────────────────────────────────────────
# COROUTINE 2: orchestrate all fetch calls
# ─────────────────────────────────────────────

async def main():

    endpoints = [
        "https://httpbin.org/delay/2",   # this URL intentionally waits 2 seconds before responding
        "https://httpbin.org/delay/2",   # simulates a slow real-world API (DB call, ML inference, etc.)
        "https://httpbin.org/delay/2",   # all 3 take 2s — without async this would be 6s total
    ]

    async with aiohttp.ClientSession() as session:
        # ClientSession is aiohttp's connection manager
        #
        # Why 'async with' here too?
        #   - ClientSession holds a pool of open TCP connections underneath
        #   - 'async with' ensures those connections are properly closed when done
        #   - creating a new session per request is wasteful — one shared session
        #     is the recommended pattern so connections can be reused across requests
        #
        # 'session' will be passed into each fetch_metrics() call below

        tasks = [fetch_metrics(session, url) for url in endpoints]
        # list comprehension creates a list of coroutine objects — one per endpoint
        # at this point NO request has been sent yet
        # calling fetch_metrics(...) only creates the coroutine, it does not run it
        # the coroutines are scheduled and run only when handed to asyncio.gather()

        await asyncio.gather(*tasks)
        # asyncio.gather() takes multiple coroutines and runs them CONCURRENTLY
        #
        # *tasks unpacks the list: gather(task1, task2, task3)
        # 'await' pauses main() here until ALL three coroutines complete
        #
        # what happens under the hood:
        #   - all 3 HTTP requests fire almost simultaneously
        #   - each coroutine hits 'async with session.get(...)' and pauses — waiting for response
        #   - while coroutine 1 is waiting, event loop runs coroutine 2
        #   - while coroutine 2 is waiting, event loop runs coroutine 3
        #   - all 3 are waiting in parallel (non-blocking)
        #   - when any response arrives, that coroutine resumes and prints its result
        #   - total time ≈ 2s (slowest single request), NOT 6s (sum of all)


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

start = time.time()
# record the wall-clock time before anything runs

asyncio.run(main())
# asyncio.run() does three things:
#   1. creates a new event loop
#   2. runs the main() coroutine on it until completion
#   3. closes and cleans up the event loop
#
# this is always the outermost call — you pass your top-level coroutine here
# never call asyncio.run() inside an async function — only at the top level

end = time.time()
# record wall-clock time after everything completes

print(f"\nTotal time taken: {end - start:.2f} seconds")
# expected output: ~2 seconds (not 6) — proof that all 3 requests ran concurrently