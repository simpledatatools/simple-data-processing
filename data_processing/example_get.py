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


# profiles
filters = {}
profiles = get_profiles(app_id, filters=filters)
for profile in profiles:
   print(profile)

# One profile
profile_id = 'bYLblf5XjTCSNQa4'
profile = get_profile(app_id, profile_id)
if profile:
    print(profile)

'''
app_id = 't9wH6RI5HnOFJcsQ'
app = get_app(app_id)
if app:
    print(app)
'''


