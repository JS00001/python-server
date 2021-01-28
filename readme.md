# Python Backend

### Installation
This server requires Python to run.
Execute the following in a command prompt in order to activate the virtual environment and install all dependencies.
```shell
$ py -m venv venv
$ .\venv\scripts\activate
$ pip install -r requirements.txt
```

### Run Server
To run the server, run the `start.bat` file in the main directory, or run the following command.
```shell
$ .\venv\scripts\activate && flask run 
```

### Potential Errors
**Create a `.env` file** - The .env file for this project is included in the gitignore for safety purposes. Copy the `.env.example` file and rename it to `.env`, and fill out all fields accordingly

## Endpoints

#### Server Exclusive Endpoints
<hr>
<br>
[Login with Discord](http://localhost:5000/v1/login) | `http://localhost:5000/v1//login`
<br>
<br>
Callback Returns
```json
{
  "userid": ""
}
```
──────────────────────────────────────────────────────

[Logout of Website](http://localhost:5000/v1/logout) | `http://localhost:5000/v1/logout`
<br>
<br>
Callback Returns
```json
{
  "error": false
}
```
──────────────────────────────────────────────────────
#### Api-key Accessed Endpoints

[List all Products](http://localhost:5000/v1/products/list) | `http://localhost:5000/v1/products/list`
<br>
<br>
Authorization
- Header Required: **api-key**
- Permission Required: **MANAGE_PRODUCTS**
- Request Type: **GET**

Callback Returns
```json
[
  {
    "name": "NAME",
    "description": "DESCRIPTION",
    "price": 0,
    "category": "CATEGORY"
  },
  {
    "name": "NAME",
    "description": "DESCRIPTION",
    "price": 0,
    "category": "CATEGORY"
} 
]
```
──────────────────────────────────────────────────────

[Add a product](http://localhost:5000/v1/products/add) | `http://localhost:5000/v1/products/add`
<br>
<br>
Authorization
- Header Required: **api-key**
- Permission Required: **MANAGE_PRODUCTS**
- Request Type: **POST**

Data Requirement
- Body (Json Formatted).
    - name
    - description
    - price
    - category

Callback Returns
```json
{
  "name": "NAME",
  "description": "DESCRIPTION",
  "price": 0,
  "category": "CATEGORY"
}
```
──────────────────────────────────────────────────────

[Remove a product](http://localhost:5000/v1/products/remove) | `http://localhost:5000/v1/products/remove`
<br>
<br>
Authorization
- Header Required: **api-key**
- Permission Required: **MANAGE_PRODUCTS**
- Request Type: **DELETE**

Data Requirement
- Body (Json Formatted).
    - name

Callback Returns
```json
{
  "error": false
}
```
──────────────────────────────────────────────────────


