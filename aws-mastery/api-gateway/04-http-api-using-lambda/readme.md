# For testing with localhost website:

In the terminal, go to the path where HTML file is present on the system and run this python command:
python3 -m http.server 8000

Open browser and go to:
http://localhost:8000/sample-webpage.html

Also Note that CORS haders are also sent in the GET response but not visible in POSTMAN as:
Postman does not send an Origin header in its requests by default.
CORS headers like Access-Control-Allow-Origin are only returned by the server when the request contains an Origin header — because that is how CORS works. The server sees an Origin header, recognizes it as a cross-origin request, and adds CORS headers to the response.
Postman does not send Origin by default → Server does not see a cross-origin request → Server does not add CORS headers to the response → Postman does not show them.

# Proof — Add Origin Header Manually in Postman.
In Postman → your GET request → Headers tab → add:
Origin: http://localhost:8000
Send the request again — now you will see Access-Control-Allow-Origin: * in the response headers.


xxx
add console.log to log incoming event in the lambda function. to understand the EVENT json format.
