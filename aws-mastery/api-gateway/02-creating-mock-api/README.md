# The API: Products API

# Base resource: /products

# Endpoint 1 — GET /products
Purpose: Get a list of all products
No parameters at all.
Mock Response:
json
{
  "products": [
    { "id": "1", "name": "Laptop", "category": "Electronics", "price": 75000 },
    { "id": "2", "name": "Desk Chair", "category": "Furniture", "price": 12000 },
    { "id": "3", "name": "Notebook", "category": "Stationery", "price": 150 }
  ]
}

Create a resource, add GET method, mock integration, hardcoded response, deploy and test.
=================================================

# Endpoint 2 — GET /products/{id}
Purpose: Get one specific product by its ID
Path Parameter: id
Example URL: GET /products/1
Mock Response:
json
{
  "id": "1",
  "name": "Laptop",
  "category": "Electronics",
  "price": 75000
}

Define {id} in resource path, API Gateway captures it, reads it in mapping template using $input.params('id'), echoes it back in response.
=================================================

# Endpoint 3 — GET /products?category=Electronics&inStock=true
Purpose: Search/filter products
Query Parameters:

category — mandatory (e.g., Electronics, Furniture)
inStock — optional (true / false)

Example URL: GET /products?category=Electronics&inStock=true
Mock Response:
json
{
  "category": "$input.params('category')",
  "inStock": "$input.params('inStock')",
  "products": [
    { "id": "1", "name": "Laptop", "price": 75000 }
  ]
}

Declare query params in API Gateway, both mandatory and optional, read them in mapping template using $input.params('category'), test in Postman Params tab and AWS console test tool.
=================================================

# Endpoint 4 — POST /products
Purpose: Add a new product
No parameters. Request body sent from Postman.
Request body:
json
{
  "name": "Mouse",
  "category": "Electronics",
  "price": 1500
}

Mock Response (status 201):
json
{
  "message": "Product created successfully",
  "id": "4",
  "name": "Mouse",
  "category": "Electronics",
  "price": 1500
}

POST method setup, return 201 instead of 200, send request body from Postman.
Mock does not actually read the body — Lambda is needed for that.

Full Structure — One Glance
/products
    GET              → Get all products (no params)
    POST             → Add a product (hardcoded 201 response)

/products/{id}
    GET              → Get one product by ID (path param)

Query params category and inStock are on the same GET /products endpoint — just add them as URL Query String Parameters on that method.

Reading path parameter:
$input.params('id')

Reading query parameters:
$input.params('category')
$input.params('inStock')

Stage 3 mapping template example:
json{
  "category": "$input.params('category')",
  "inStock": "$input.params('inStock')"
}
=================================================

test-webpage.html is to test the behavior of the API is CORS is disabled/enabled.
===================================================