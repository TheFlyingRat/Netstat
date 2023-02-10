import subprocess

class Interface():
    def __init__(self):
        pass
    def get_interface(self):

        # Query the system for wlan interface information
        response = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8')

        # Remove new lines from the response and also remove blank strings and make this into a list
        resultsInterpreted = list(filter(None, response.split('\r\n')))

        # Declare a blank dictionary
        returnObject = {}

        # Loop through each line of the interpreted output, splitting on ":", removing whitespaces and creating a new dictionary
        # We want to ignore the first line of the output as it contains useless information
        for key_value in resultsInterpreted[1:]: 
            try:
                key, value, *_ = key_value.split(':')
            except ValueError:
                pass
            returnObject[key.strip()] = value.strip()

        return returnObject
