import requests
import json

from api.settings.vars import *
from api.settings.utils import *

def get_customer(app_id, customer_id):

    # # Request Url
    url = BASE_URL + '/apps/' + app_id + '/customers/' + customer_id

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
        customer = data['customer']

        return customer


def get_customers(app_id, filters=None):
    
    # # Request Url
    url = BASE_URL + '/apps/' + app_id + '/customers/'

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
        customers = data['customers']

        line(top=1,bottom=1)

        print('Page: ' + str(data['page']))
        print('Pages: ' + str(data['pages']))
        
        line(top=1,bottom=1)

        return customers
    

def add_customer(app_id, data):

    # # Request Url
    url = BASE_URL + '/apps/' + app_id + '/customers/add/'

    # Request
    response = requests.post(
        url,
        headers={
            "Authorization" : API_KEY
        },
        json=data,
    )

    if not check_status(response):
        return None

    # Response
    else:
        data = response.json()
        customer = data['customer']

        return customer


def update_customer(app_id, customer_id, data):

    # # Request Url
    url = BASE_URL + '/apps/' + app_id + '/customers/' + customer_id + '/update/'

    # Request
    response = requests.put(
        url,
        headers={
            "Authorization" : API_KEY
        },
        json=data,
    )

    if not check_status(response):
        return None

    # Response
    else:
        data = response.json()
        customer = data['customer']

        return customer


def archive_customer(app_id, customer_id):

    # # Request Url
    url = BASE_URL + '/apps/' + app_id + '/customers/' + customer_id + '/archive/'

    # Request
    response = requests.put(
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

        line(top=1,bottom=1)
        print(customer_id + ' --> Archived ')
        line(top=1,bottom=1)

        return data