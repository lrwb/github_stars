# Requirements
=================================
* Python >= 3.6 
* sqlite

# Setup
1. Create a virutal environment
   * `$ python3.6 -m venv env3`
2.  Active your virtual environment
    * `$ source env3/bin/activate`
3.  Install python packages
    * `$ pip install -r requirements.txt`
4. Set specific flask project settings
    * `$ source settings.sh`

## To Ingest from Github
Start the script to query the github api and store results to an sqlite database.
`$ python start.py`
You must first run the ingester to populate data in the database.  This script is run independently of the flask application.

## To View the Results
Start the flask app with, `$ flask run`.  Using a browser, navigate to `localhost:5000/project`.  Click through the list to view individual results.

## Notes
This is a quick example of reading an API and storing the results in a database with one module while accessing the database from a flask application in another module.  This provides the data in HTML only.  In my experience, I would be interested in returning the JSON and/or XML object.
