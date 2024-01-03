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
profile_id = 'bYLblf5XjTCSNQa4'
data = {
    'name': 'API profile 1 EDIT'
}
profile = update_profile(app_id, profile_id, data)
print(profile)
        
    
