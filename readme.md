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


# Server Exclusive Endpoints

[Login with Discord](http://localhost:5000/v1/login) | `http://localhost:5000/v1/login`

Callback Returns
```json
{
  "userid": ""
}
```
<hr>

[Logout of Website](http://localhost:5000/v1/logout) | `http://localhost:5000/v1/logout` **GET**

Callback Returns
```json
{
  "error": false
}
```
<hr>

[List all Api Keys](http://localhost:5000/v1/apikeys/list) | `http://localhost:5000/v1/apikeys/list` **GET**

Callback Returns
```json
[
    {
        "key": "GvqOvBDMGOUjozFt",
        "permissions": [
            "MANAGE_PRODUCTS"
        ]
    },
    {
        "key": "bpivforBpTcoEtyc",
        "permissions": [
            "MANAGE_PRODUCTS"
        ]
    }
]
```
<hr>

[Generate Api Keys](http://localhost:5000/v1/apikeys/create) | `http://localhost:5000/v1/apikeys/create` **POST**

Data Requirement
-  Body (Json Formatted)
  - `permissions` array

Callback Returns
```json
{
  "permissions": ["MANAGE_PRODUCTS"],
  "key": "abcdefg"
}
```
<hr>

[Delete Api Keys](http://localhost:5000/v1/apikeys/delete) | `http://localhost:5000/v1/apikeys/delete` **DELETE**

Data Requirement
- Url Parameters
  - `key` value (apikey)

Callback Returns
```json
{
  "error": false
}
```
<hr>

[Update Api Keys](http://localhost:5000/v1/apikeys/update) | `http://localhost:5000/v1/apikeys/update` **PUT**

Data Requirement
- Body (Json Formatted)
  - `permissions` array of permissions to add
  - `key` object with key to update permissions of

Callback Returns
```json
{
  "error": false
}
```
<hr>

# Api-key Accessed Endpoints

[List all Products](http://localhost:5000/v1/products/list) | `http://localhost:5000/v1/products/list` **GET**

Authorization
- Header Required: **api-key**
- Permission Required: **MANAGE_PRODUCTS**

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
<hr>

[Add a product](http://localhost:5000/v1/products/add) | `http://localhost:5000/v1/products/add` **POST**

Authorization
- Header Required: **api-key**
- Permission Required: **MANAGE_PRODUCTS**

Data Requirement
- Body (Json Formatted).
    - `name`
    - `description`
    - `price`
    - `category`

Callback Returns
```json
{
  "name": "NAME",
  "description": "DESCRIPTION",
  "price": 0,
  "category": "CATEGORY"
}
```
<hr>

[Remove a product](http://localhost:5000/v1/products/remove) | `http://localhost:5000/v1/products/remove` **DELETE**

Authorization
- Header Required: **api-key**
- Permission Required: **MANAGE_PRODUCTS**

Data Requirement
- Body (Json Formatted).
    - `name`

Callback Returns
```json
{
  "error": false
}
```
<hr>

[Get User Data](http://localhost:5000/v1/users/<user_id>) | `http://localhost:5000/v1/users/<user_id>` **GET**

Authorization
- Header Required: **api-key**
- Permission Required: **MANAGE_USERS**

Callback Returns
```json
{
  "userid": "1"
}
```
<hr>


