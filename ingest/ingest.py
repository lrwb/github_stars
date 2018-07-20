'''
Ingest data at the defined API with the expected structure.
'''
# Python imports
from datetime import datetime
import json
import urllib.parse
import urllib.request

# Third party imports

# Package imports
from ingest.database.models import PythonProjects


def get_github_python_stars(base_url):
    '''
    Get the results at the url.

    Args:
        base_url (string) - The url base.
    '''
    values = {
        'q': 'language:python',
        'sort': 'stars',
        'order': 'desc'
        }

    query_params = urllib.parse.urlencode(values)

    full_req = base_url + '?' + query_params

    # Ideally, this is a debug or info level log statement
    print(full_req)
    with urllib.request.urlopen(full_req) as response:
        results = response.read()

    results_str = results.decode('utf-8')
    data = json.loads(results_str)
    data_items = data['items']
    print("There are {0} data items".format(len(data_items)))

    top_results = []
    for data_item in data_items:
        print('**************************************************')
        print(data_item.get('full_name'))   # repo full name
        print(data_item.get('created_at'))#  created date
        print(data_item.get('pushed_at'))#  last push date  ,this will likely update
        print(data_item.get('stargazers_count'))#  number of stars

        item_results = {}
        item_results['repo_name'] = data_item.get('full_name')
        item_results['repo_id'] = data_item.get('id')
        item_results['url'] = data_item.get('url')
        item_results['creation_time'] = datetime.strptime(
            data_item.get('created_at'),
            '%Y-%m-%dT%H:%M:%SZ')
        item_results['last_push_time'] = datetime.strptime(
            data_item.get('pushed_at'),
            '%Y-%m-%dT%H:%M:%SZ')
        item_results['description'] = data_item.get('description')
        item_results['stars'] = data_item.get('stargazers_count')
        top_results.append(item_results)

    return top_results

def prepare_database_entries(items):
    '''
    Create PythonProjects objects to store in the database.

    Args:
        items (list of dictionaries) - list of dictionary items to convert
            to PythonProjects items.
    Returns:
        A list of PythonProjects class objects.
    '''
    entries = []
    for result in items:
        db_entry = PythonProjects(
            repo_name=result.get('repo_name'),
            repo_id=result.get('repo_id'),
            url=result.get('url'),
            creation_time=result.get('creation_time'),
            last_push_time=result.get('last_push_time'),
            description=result.get('description'),
            stars=result.get('stars'))

        entries.append(db_entry)

    return entries
