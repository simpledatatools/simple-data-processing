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
data = {
    'name': 'API Customer 1'
}
customer = add_customer(app_id, data)
print(customer)
        
    
