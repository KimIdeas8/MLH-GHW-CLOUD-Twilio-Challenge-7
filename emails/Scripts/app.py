from flask import Flask, request

from mars_emails import send_mars_email, get_mars_photo

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def email_response():
    from_email = request.form['from']
    to_email = request.form['to']
    subject = request.form['subject']
    body = str.split(request.form['text'])[0]

    print('From:', from_email)
    print('To:', to_email)
    print('Subject', subject)
    print('Body:', body)

    if body.isdigit():
        img_url = get_mars_photo(body)
    else:
        img_url = get_mars_photo('1000')
    send_mars_email(to_email, from_email, img_url) #respond to user's mail

    return '' 

if __name__ == '__main__':
    app.run(debug=True)