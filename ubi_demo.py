import time
import requests
import os
from dotenv import load_dotenv

load_dotenv

# TOKEN = "..."  # Put your TOKEN here
TOKEN = os.getenv('TOKEN') # Put your TOKEN here
# DEVICE_LABEL = "machine"  # Put your device label here 
DEVICE_LABEL = os.getenv('LABEL')  # Put your device label here 
# VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here
VARIABLE_LABEL_1 = os.getenv('VARIABLE')  # Put your first variable label here
VARIABLE_LABEL_2 = os.getenv('VARIABLE2') # Put your second variable label here
VARIABLE_LABEL_3=  os.getenv('VARIABLE3')# Put your second variable label here



def build_payload(variable_1, keranjang1,variable_2, keranjang2,variable_3, keranjang3):
    # Creates two random values for sending data
    value_1 = keranjang1
    value_2 = keranjang2
    value_3 = keranjang3

    # Creates a random gps coordinates
    # lat = random.randrange(34, 36, 1) + \
    #     random.randrange(1, 1000, 1) / 1000.0
    # lng = random.randrange(-83, -87, -1) + \
    #     random.randrange(1, 1000, 1) / 1000.0
    # payload = {variable_1: value_1,
    #            variable_2: value_2,
    #            variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}}}
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: value_3
    
    }

    return payload

# def build_payload(variable_1):
#     # Creates two random values for sending data
#     value_1 = Temperature_1.get_data()
#     # value_2 = random.randint(0, 85)

#     # Creates a random gps coordinates
#     # lat = random.randrange(34, 36, 1) + \
#     #     random.randrange(1, 1000, 1) / 1000.0
#     # lng = random.randrange(-83, -87, -1) + \
#     #     random.randrange(1, 1000, 1) / 1000.0
#     # payload = {variable_1: value_1,
#     #            variable_2: value_2,
#     #            variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}}}
#     payload = {'variable': variable_1,
#     'value':value_1}

#     return payload



def post_request(payload):
    # Creates the headers for the HTTP requests
    try:
        url = "http://industrial.api.ubidots.com/api/v1.6/devices/"+ DEVICE_LABEL +"/" 
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

        # Makes the HTTP requests
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        time.sleep(1)

        # Processes results
        print(req.status_code, req.json())
        if status >= 400:
            print("[ERROR] Could not send data after 5 attempts, please check \
                your token credentials and internet connection")
            pass

        print("[INFO] request made properly, your device is updated")
        return True
    except:
        print("Cannot send to ubidots")
        pass

# def post_request(payload):
#     try:
#         api = ApiClient(token=TOKEN) # Replace with your Ubidots Token here
#         api.save_collection([payload])
#         # api.save_collection(payload)
#         print('sent to ubidots')
#     except:
#         print('problem in ubidots')
#         pass




def send_data(keranjang1, keranjang2, keranjang3):
    payload = build_payload(
         VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)

    # payload = build_payload(
    #     VARIABLE_ID)

    print("[INFO] Attemping to send data")
    print(payload)
    post_request(payload)
    print("[INFO] finished")


# if __name__ == '__main__':
    # while (True):
    #     main()
    #     time.sleep(1)