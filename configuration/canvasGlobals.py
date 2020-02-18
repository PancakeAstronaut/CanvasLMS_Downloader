'''
Stephen Hengeli
Canvas API File Download Functionality Test
October 03, 2019
Canvas Package Simplifier Module [CPSM]

Required Packages:
'from canvasapi import Canvas'   # Accesses the methods included in the canvasapi package
'import json'       # Reads the API key from the JSON config file
'''
from canvasapi import Canvas
import json

'''Global values needed everywhere'''
# This list is the list of all courseIDs you are currently enrolled in.
courseList = [
  # course numbers go here
]

# Accesses the canvas API access token
with open('configuration/config.json') as json_config:
    config = json.load(json_config)
    for access in config['canvas']:
        api_key = access['access_token']

# These are the variables that represent the enrolled classes
# These numbers can be found in the URL of the class on Canvas
# To add a class, add the courseID to the list and set a named variable equal to the index of the new number
MGMT418 = courseList[0]
IST440 = courseList[1]
IST421 = courseList[2]

# This is the Student number that Canvas creates. Not your University studentID
# Run the line of code below to find yours. Requires Canvas object
# print(CANVAS.get_current_user())
# SISNUM GOES BELOW AS INT
SISNUM = ""

# API Connection Information
API_URL = "[put canvas url here]"     # Canvas API URL
API_KEY = str(api_key)                      # Canvas API key

# Canvas Object Declarations
CANVAS = Canvas(API_URL, API_KEY)           # Initialize a new Canvas object
USER = CANVAS.get_user(SISNUM)             # Use the Canvas object to get the User object

'''End of Global Values'''
