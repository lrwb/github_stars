# Requirements
=================================
* Python >= 3.6 
* sqlite

# Setup
1.  Create a virutal environment
    * `$ python3.6 -m venv env3`
2.  Active your virtual environment
    * `$ source env3/bin/activate`
3.  Install python packages
    * `$ pip install -r requirements.txt`
4.  Set specific flask project settings
    * `$ source settings.sh`
5.  Ingest from github.  For more explanation, see below.
    * `$ python start_ingest.py`
6.  Start flask module.  For more explanation, see below.
    * `$ flask run`
7. When finished running modules, deactivate the environment.
    * `$ deactivate`

## To Ingest from Github
Start the script to query the github api and store results to the table
`python_projects` in an sqlite database, `github.db`.  You must first run the
ingester to populate the database.  This script is run independently of the
flask application.

## To View the Results
Start the flask app with, `$ flask run`.  Using a browser, navigate to
`localhost:5000/project`.  Click through the list to view individual results.
Project details are provided at `localhost:5000/project/<repo_id>`.
This structure was chosen to support discoverability.

## Notes
This is a quick example of reading an API and storing the results in a
database with one module while accessing the database from a flask application
in another module.  This provides the data in HTML only.  I would enhance this
to return JSON and/or XML objects.

I have left some of the print statements in tact.  These statements should be
logging statements with a proper logger, some at the `INFO` level but most at
the `DEBUG` level.  I left the logger configuration out for time considerations.

The database connection is hard coded.  A proper application would have a
configuration module to allow defining the database connection string more
flexibly, either via command line, config file, or  environment variable.

There are several hard coded values.  Ideally, these would be handled via a
constants module to make maintenance and updates easier.

Pagination is not implemented because the github api returns the top 30
starred results.  This number is reasonable.

Unit tests need to be added as well.
