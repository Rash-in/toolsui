# ToolsUI
Used to test various HTTP frontend frameworks. This is not yet ready to consume for its intended use. The only portion that is working currently is the runtime environment to get the application up and running with no defined routes.
- **Not intended to be used in production**

## Prerequisites
- Python 3.11 or later (Typing syntax and performance gains)
- Not a Windows OS (will most likely get it working later but the REAL web uses linux so deal :P )

## Direct Dependencies
- hypercorn: ASGI Server used to serve the apps.
- fastapi: ASGI application that serves data and html
- httpx: Used to make external API calls for data
- loguru: Logging framework
- Jinja2: HTML Templating framework
- pipdeptree: Used in testing scripts to show python package dependencies.

## Environment Variables
Environment variables are in `configs/toolsui.toml`. If the file is not present, create it.

Variables in toolsui.toml:
1) APP_PATH="PLACEHOLDER"
- (folder path where main.py is located.)
2) LOG_PATH="PLACEHOLDER"
- (folder path that logs will be stored in. Files will be automatically created in this folder for logs)
3) CERT_PATH="PLACEHOLDER"
- (folder path where the .crt file used for SSL is located.)
4) KEY_PATH="PLACEHOLDER"
- (folder path where the .key file used for SSL is located.)
5) CA_PATH="PLACEHOLDER"
- (folder path where the .pem file used for SSL validation is located.)

Replace PLACEHOLDER in each of the variables to the exact path (without the trailing '/').

## Installation
1) Terminal: cd to the directory where you want to save the app and clone repo
- `git clone https://github.com/Rash-in/toolsui.git`
2) cd into toolsui
- `cd toolsui`
3) install virtual environment
- `python3.11 -m venv .env`
4) Activate virtual environment
- `source .env/bin/activate` or `. .env/bin/activate`
5) Install requirements
- `pip install -r requirements.txt`
6) deactivate virtual environment
- `deactivate`
7) Modify environment variables (see above)
8) Run application
- `python3 -B bin/start_local.py`
9) In browser navigate to http://localhost:5000/docs

## start_local.py
This file creates the subprocess that runs hypercorn ASGI server that serves the application. Without any arguments, it will run preconfigured with intended settings for a developer environment. with -c switch and a filepath it will import a hypercorn config file that you can set. See documentation [here](https://hypercorn.readthedocs.io/en/latest/how_to_guides/configuring.html#configuration-options).

- bind "0.0.0.0:5000"
(binds to all interfaces on port 5000)

- worker-class "asyncio"
(uses async workers to serve the applcation)

- log-level "DEBUG"
(sets the log level to the highest logging setting)

- error-logfile "-"
(sets the error logs to stdout)

- reload
(Looks for any python file changes inside the app path and reloads upon saving the file.)

**NOTE: There is a sample file in the configs folder called hypercorn.toml that does the same thing so that people can see what the format looks like as an example.**

## start_server.py
(Work in Progress). The intended use for this is to test builds to be installed on a server. I am creating it with the intent on a production build but it is not ready yet.

## start_tests.py
(Work in Progress) used to initiate pytest tests configured in the tests folder. There are updates that need to be made initially so it is also not yet ready to consume.
