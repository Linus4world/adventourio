# Backend

### Introduction

The backend project is the server implentation of our application. It uses Flask to provide an easy to understand python-based server implementation. Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

### Local Development
##### Prerequisites
1. [Python 3](https://www.python.org/downloads/)
    Download the latest version of python and make sure to set the PATH variable accordongly. Verify your installation by running this command from a command line:
    ```sh
    python -V
    
    # check if pip is installed

    pip -V
    ```
2. Dependencies
    You can install all other dependencies by running:
    ```sh
    pip install -r requirements.txt
    ```

    *If you add new dependencies in the future make sure to also add them to the requirements.txt file!*

##### Running the server
You can start the server by running:
```sh
python server.py
```

You can now open your browser and navigate to `http://localhost:5000`


### JSON files

#### places 

Places are grouped into three categories, Entertainment, University, Sightseeing. Each category further divided into three stages (as for now for, stage 0 is meant as a buffer stage for places I haven't found a challenge for yet. Feel free to change it if you get an idea).