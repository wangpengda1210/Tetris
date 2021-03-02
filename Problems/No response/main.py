import requests


def get_response(url):
    if not url.startswith('https://'):
        print('No response')
    else:
        try:
            response = requests.get(url)
            print(response.status_code)
        except InvalidSchema:
            print('No response')
