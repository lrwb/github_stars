# Python package imports

# Third party package imports
from flask import render_template

# Package imports
#from database.DAO import PythonProjectsDAO
from stars_app import app
from stars_app.database import init_db
from stars_app.models import PythonProjects

init_db()

#dao = PythonProjectsDAO()

@app.route('/')
@app.route('/project', methods=['GET'])
def index():
    results = PythonProjects.query.all()
    result_list = []
    for result in results:
        result_dict = {}
        result_dict['repo_name'] = result.repo_name
        result_dict['repo_id'] = result.repo_id
        result_list.append(result_dict)

    return render_template('index.html', projects=result_list)

@app.route('/project/<int:repo_id>', methods=['GET'])
def get_details(repo_id):
    results = PythonProjects.query \
                          .filter(PythonProjects.repo_id==repo_id) \
                          .first()
    return render_template('detail.html', project=results)
