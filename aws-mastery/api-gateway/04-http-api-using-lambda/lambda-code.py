import json

# This Lambda function is designed to handle HTTP requests from API Gateway. It processes different HTTP methods (GET, POST, PUT, DELETE) and returns appropriate responses based on the request data. The function also includes error handling to manage unexpected issues gracefully.
def lambda_handler(event, context):

    print("Received Event:")
    # Using json.dumps with indent=2 to pretty-print the event object for better readability in the logs. This helps in understanding the structure of the incoming request and debugging if necessary.
    print(json.dumps(event, indent=2))

    try:

        # Extracting the HTTP method from the event object. The HTTP method indicates the type of request being made (e.g., GET, POST, PUT, DELETE). This information is crucial for determining how to process the request and what kind of response to generate.
        http_method = event["requestContext"]["http"]["method"]
        print(f"HTTP Method Extracted: {http_method}")

        # Path parameters
        # here "or" means if pathParameters is None, use an empty dictionary
        path_parameters = event.get("pathParameters") or {}
        print(f"Path Parameters Extracted: {path_parameters}")

        # Request body
        body = event.get("body")
        print(f"Request Body Extracted: {body}")

        response_body = {}

        # Python switch-case using match-case (available in Python 3.10+)
        match http_method:

            case "GET":
                
                print("Handling GET request")

                # Example:
                # GET /tools
                # GET /tools/101

                tool_id = path_parameters.get("id")

                if tool_id:
                    response_body = {
                        "message": f"Fetching tool with ID: {tool_id}",
                        "method": "GET"
                    }

                else:
                    response_body = {
                        "message": "Fetching all tools",
                        "method": "GET"
                    }

            case "POST":
                
                print("Handling POST request")

                # if no body then use empty dictionary
                request_data = json.loads(body) if body else {}

                response_body = {
                    "message": "Tool created successfully",
                    "method": "POST",
                    "requestBody": request_data
                }

            case "PUT":
                
                print("Handling PUT request")

                tool_id = path_parameters.get("id")

                request_data = json.loads(body) if body else {}

                response_body = {
                    "message": f"Updating tool with ID: {tool_id}",
                    "method": "PUT",
                    "updatedData": request_data
                }

            case "DELETE":
                
                print("Handling DELETE request")

                tool_id = path_parameters.get("id")

                response_body = {
                    "message": f"Deleting tool with ID: {tool_id}",
                    "method": "DELETE"
                }

            # Handle unsupported HTTP methods. "case _" means "default" case in switch-case
            case _:
                
                print(f"Unsupported HTTP method: {http_method}")

                return {
                    "statusCode": 405,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    "body": json.dumps({
                        "message": "Method Not Allowed"
                    })
                }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            
            # we are using json.dumps to convert the response_body dictionary into a JSON string, which is required for the API Gateway response format.
            "body": json.dumps(response_body)
        }

    except Exception as e:

        print("Error occurred:")
        print(str(e))

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Internal Server Error",
                "error": str(e)
            })
        }