import json
from datetime import date, timedelta, datetime
import math
import requests
from bs4 import BeautifulSoup

import sys
sys.path.append("..")
from api.settings.imports import *
from api.settings.utils import *

# Adding a profile
data = {
    'name': 'API profile 1'
}
profile = add_profile(app_id, data)
print(profile)
        
    
