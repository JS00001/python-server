# Python oAuth2

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
[Login with Discord](http://localhost:5000/login) | `http://localhost:5000/login`