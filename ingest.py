# Python imports
from datetime import datetime
import json
import urllib.parse as parse
import urllib.request as request

# Third party imports

# Package imports
import database.models as models


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

    query_params = parse.urlencode(values)

    full_req = base_url + '?' + query_params

    # Ideally, this is a debug or info level log statement
    print(full_req)
    with request.urlopen(full_req) as response:
        results = response.read()

    results_str = results.decode('utf-8')
    data = json.loads(results_str)
    #data_obj = json.dumps(data, indent=4, sort_keys=True)
    data_items = data['items']
    print("There are {0} data items".format(len(data_items)))

    top_results = []
    for data_item in data_items:
        print('**************************************************')
        print(data_item.get('full_name'))   # repo full name
        #print(data_item.get('id'))     # repo id
        #print(data_item.get('url'))#  url
        print(data_item.get('created_at'))#  created date
        print(data_item.get('pushed_at'))#  last push date  ,this will likely update
        #print(data_item.get('description'))#  description
        #print(data_item.get('stargazers_count'))#  number of stars

        item_results ={}
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
    entries = []
    for result in items:
        db_entry = models.PythonProjects(
        repo_name = result.get('repo_name'),
        repo_id = result.get('repo_id'),
        url = result.get('url'),
        creation_time = result.get('creation_time'),
        last_push_time = result.get('last_push_time'),
        description = result.get('description'),
        stars = result.get('stars'))
        entries.append(db_entry)

    return entries

if __name__ == '__main__':
    # This should be a config file or command line argument
    URL = 'https://api.github.com/search/repositories'

    results = get_github_python_stars(URL)
    prepared_entries = prepare_database_entries(results)
