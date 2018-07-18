# Python package imports

# Third party package imports
from flask import render_template

# Package imports
from database.DAO import PythonProjectsDAO
from stars_app import app

dao = PythonProjectsDAO()

@app.route('/')
@app.route('/project', methods=['GET'])
def index():
    name_id_list = dao.get_python_projects_names_and_ids()
    return render_template('index.html', projects=name_id_list)

@app.route('/project/<int:repo_id>', methods=['GET'])
def get_details(repo_id):
    details = dao.get_python_project_by_repo_id(repo_id)
    return render_template('detail.html', project=details)
