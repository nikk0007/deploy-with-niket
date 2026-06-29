# Section 4: CONDITIONAL RETURN - one function, different answers
# Example: classify an HTTP status code from an API health check.

def classify_http_status(status_code):
    if status_code == 200:
        return "OK - Request successful"
    if status_code == 401:
        return "Unauthorized - Check your API key"
    if status_code == 403:
        return "Forbidden - You don't have permission"
    if status_code == 404:
        return "Not Found - Check the endpoint URL"
    if status_code == 500:
        return "Server Error - Retry or escalate"
    return "Unknown status code"


print(classify_http_status(200))   # OK - Request successful
print(classify_http_status(404))   # Not Found - Check the endpoint URL
print(classify_http_status(503))   # Unknown status code


print()
print("=== Early Return Pattern: deployment authorization ===")


# Nested style - works, but harder to read as conditions grow
def authorize_deployment_nested(tests_passed, has_approval, environment):
    if tests_passed:
        if has_approval:
            if environment == "production":
                return "Deployment authorized for production"
            else:
                return "Deployment authorized"
        else:
            return "Approval pending"
    else:
        return "Tests failed - deployment blocked"


# Early return style - "fail fast": check problems first, success last
def authorize_deployment(tests_passed, has_approval, environment):
    if not tests_passed:
        return "Tests failed - deployment blocked"
    if not has_approval:
        return "Approval pending"
    if environment == "production":
        return "Deployment authorized for production"
    return "Deployment authorized"


print(authorize_deployment(tests_passed=False, has_approval=True, environment="staging"))
print(authorize_deployment(tests_passed=True, has_approval=False, environment="production"))
print(authorize_deployment(tests_passed=True, has_approval=True, environment="production"))
print(authorize_deployment(tests_passed=True, has_approval=True, environment="staging"))

# Both functions above produce identical results for the same inputs -
# the early-return version is just easier to read and extend.
