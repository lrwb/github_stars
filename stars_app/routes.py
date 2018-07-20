# Python package imports

# Third party package imports
from flask import render_template

# Package imports
from stars_app import app
import stars_app.database as dao

dao.init_db()

@app.route('/')
@app.route('/project', methods=['GET'])
def index():
    '''
    Render a list of projects via HTML.
    '''
    result_list = dao.get_names_and_ids()

    return render_template('index.html', projects=result_list)

@app.route('/project/<int:repo_id>', methods=['GET'])
def get_details(repo_id):
    '''
    Render the details of a specific project.

    Args:
        repo_id (int) - An id that should match a repo_id in the
            python_projects table.
    '''
    results = dao.get_project_details(repo_id)

    return render_template('detail.html', project=results)
