from flask import Flask
from flask.wrappers import Request
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/send', methods=['POST'])
def send():
    from background.tasks import send_email

    content = request.json

    recipient = content['recipient']
    subject = content['subject']
    message = content['message']

    kwargs = {
        'recipient': recipient,
        'subject': subject,
        'message': message,
    }

    send_email.delay(**kwargs)

    return jsonify({
        'error': 0
    })