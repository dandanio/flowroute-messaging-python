"""demo.py

flowroute-messaging-python is a Python SDK that provides methods
to send an outbound SMS from a Flowroute phone number and also
to retrieve a Message Detail Record (MDR). These methods use v2
(version 2) of the Flowroute API.

Copyright:
    Flowroute, Inc.  2016

Prerequisites:
    * Messaging enabled on both numbers.
"""

import os
import pprint
from time import sleep

from FlowrouteMessagingLib.Controllers.APIController import *
from FlowrouteMessagingLib.Models.Message import *

# Set up your API credentials
# Please replace the variables in Configuration.php with your information.
username = os.getenv('ACCESS_KEY')
password = os.getenv('SECRET_KEY')
from_number = os.getenv('FROM_E164')
to_number = os.getenv('TO_E164')

# Print the demo script header.
print("Flowroute, Inc - Demo SMS Python script.\n")

# Create the Controller.
controller = APIController(username=username, password=password)
pprint.pprint(controller)

# Build your message.
message = Message(to=to_number, from_=from_number, content='Your cool new SMS message here!')

# Send your message.
try:
    response = controller.create_message(message)
    pprint.pprint(response)
except APIException as e:
    print("Send Error - " + str(e.response_code) + '\n')
    pprint.pprint(e.response_body['errors'])
    exit(1)        # can't continue from here

# Get the MDR id from the response.
mdr_id = response['data']['id']

# Retrieve the MDR record.
try:
    # Example MDR: 'mdr1-b334f89df8de4f8fa7ce377e06090a2e'
    mdr_record = controller.get_message_lookup(mdr_id)
    pprint.pprint(mdr_record)
except APIException as e:
    print("Get Error - " + str(e.response_code) + '\n')
    pprint.pprint(e.response_body['errors'])
    exit(2)
