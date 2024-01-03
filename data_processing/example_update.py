import json
from datetime import date, timedelta, datetime
import math
import requests
from bs4 import BeautifulSoup

import sys
sys.path.append("..")
from api.settings.imports import *
from api.settings.utils import *

# Adding a customer
customer_id = 'bYLblf5XjTCSNQa4'
data = {
    'name': 'API Customer 1 EDIT'
}
customer = update_customer(app_id, customer_id, data)
print(customer)
        
    
