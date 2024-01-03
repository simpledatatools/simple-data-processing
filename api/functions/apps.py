import requests
import json

from api.settings.vars import *
from api.settings.utils import *

def get_app(app_id):

    # # Request Url
    url = BASE_URL + '/apps/' + app_id + '/'

    # Request
    response = requests.get(
        url,
        headers={
            "Authorization" : API_KEY
        }
    )

    if not check_status(response):
        return None

    # Response
    else:
        data = response.json()
        app = data['app']

        line(top=1,bottom=1)
        print(app['name'] + ' --> ' + app['app_id'])
        line(top=1,bottom=1)

        return app


def get_apps(filters=None):
    
    # # Request Url
    url = BASE_URL + '/apps/'

    # Filters
    page = None
    page_size = None
    search = None
    sort = None
    if filters:
        if 'page' in filters:
            page = filters['page']
        if 'page_size' in filters:
            page_size = filters['page_size']
        if 'search' in filters:
            search = filters['search']
        if 'sort' in filters:
            sort = filters['sort']

    # Request
    response = requests.get(
        url,
        headers={
            "Authorization" : API_KEY
        }
    )

    if not check_status(response):
        return None

    # Response
    else:
        data = response.json()
        apps = data['apps']

        if apps:
            
            line(top=1,bottom=1)
            
            for app in apps:
                print(app['name'] + ' --> ' + app['app_id'])
        
        line(top=1,bottom=1)

        print('Page: ' + str(data['page']))
        print('Pages: ' + str(data['pages']))
        
        line(top=1,bottom=1)

        return apps

    
