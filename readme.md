# Alternative SO

## Implementation of Alternative Stackoverflow using MetaPy library
#### This implementation is part of Course CS-410 Text Information Systems, for MCS-DS (Fall 2017), University of Illinois Urbana Champaigne 

## Setup
1. Install Python3.6. Python 3.6 can be downloaded from [here](https://www.python.org/downloads/)

2. Setup PIP by following instructions [here](https://pip.pypa.io/en/stable/installing/)

3. Install Pipenv

   Application uses Pipenv for package management. To install pip run the folowing command.  

   ```bash
   pip install pipenv --user
   ```

4. Clone the git repository and `cd` into the repository
    ```bash
    git clone git@github.com:zztop/alternative-so.git && cd alternative-so
    ```

5.  Install all python modules and create python virtual environment
    ```bash
    pipenv install && pipenv shell
    ```

6. To run the search application execute the following command
    ```bash
    python server.py
    ```
    Open a browser and type in http://127.0.0.1:5000/ . This will launch the search engine




