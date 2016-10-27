import requests

# curl http://ncprstatus.in/api/v1/status?numbers={1234567890,1234566789}
url = "http://ncprstatus.in/api/v1/status"
# payload = {"numbers": [1234567890]}
# resp = requests.get(url, params=payload)
# print resp.content


def check_dnd(number):
    '''
    Returns the dnd status
    '''
    payload = {'numbers': number}
    resp = requests.get(url, params=payload)
    if (resp.status_code == 200):
        return resp.content
    else:
        return "Please check after sometime back"
