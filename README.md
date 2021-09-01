### Summary:

The REST APIs are built using Python Django framework and Mysql database.


### Python Libraries/Frameworks used:
-  **django** - This is a Python-based open-source web framework that follows the model-template-view
architectural pattern.
-  **djangorestframework** - This is a powerful and flexible toolkit built on top of the Django web framework
for building REST APIs.
-  **django-filter** - This is a reusable Django application for allowing users to filter querysets
dynamically from URL parameters.
-  **mysqlclient** - MySQL database connector for Python.
-  **black** - This is Python code formatter that formats code adhering to PEP8 standards.


### How to get the application up and running using virtual environment

This setup will install everything inside the virtual environment and requires bit more steps than docker to perform to get the application started.

Before started, make sure Mysql is installed and running in your system.

Create and activate the virtual environment using commands ```python3 -m venv env``` and ```source env/bin/activate```.

Login into mysql server and run the sql script `source /Users/furqanaziz/Documents/Smart-Study_tech-test/smartstudy/conf/init.sql` to create database. (absolute path to init.sql file)

Once database is created, do the three steps:
- Install project requirements:  ```make install-requirements```
- Create database tables:  ```make migrate```
- Run the application server:  ```make start-server```

Run ```make tests``` to execute the tests.


### How to access django admin to insert data into the database
Run the command ```make create-superuser``` to create the application super user and hit the url <http://localhost:8000/admin/>

Once everything is built and running with either of the setup, hit the url <http://localhost:8000/api/> to consume the api's.


The project is using [PEP 8](https://www.python.org/dev/peps/pep-0008/) code styling and has [black](https://black.readthedocs.io/en/stable/) set up for auto-formatting with [flake8](https://flake8.pycqa.org/en/latest/) in place.

**Notes:**
- Makefile includes many other useful commands to interact with the application.
