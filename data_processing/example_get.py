import sys
import json
import os
import random
import math
from datetime import date, timedelta, datetime
import pickle
import re

import sys
sys.path.append("..")
from api.settings.imports import *
from api.settings.utils import *


# customers
'''
filters = {}
customers = get_customers(app_id, filters=filters)
for customer in customers:
   print(customer)

'''
# One customer
customer_id = 'bYLblf5XjTCSNQa4'
customer = get_customer(app_id, customer_id)
if customer:
    print(customer)

'''
app_id = 't9wH6RI5HnOFJcsQ'
app = get_app(app_id)
if app:
    print(app)
'''


