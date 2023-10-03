
from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def return_time():
    current_time = datetime.now (timezone("UTC"))
    return current_time.strftime("%H:%M:S")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)


