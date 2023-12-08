from random import choice
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import requests

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

def send_mars_email(from_email, to_email, img_url):
    message = Mail(
        from_email = from_email,
        to_emails = to_email,
        subject = 'Here is your Mars Rover Picture',
        html_content = '<strong>Check out this Mars pic</strong><br>'
                        f'<img src="{img_url}"></img>'
    )
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)

rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

def get_mars_photo(sol, api_key='DEMO_KEY'):
    params = {'sol':sol, 'api_key': api_key}
    response = requests.get(rover_url, params).json()
    photos = response['photos'] #photos dict from json

    return choice(photos)['img_src'] #pick a photo using random library