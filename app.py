from flask import Flask, g, request
from logging import INFO, Formatter
from logging.handlers import RotatingFileHandler
import os
from time import time as time_now

app = Flask(__name__)
app.config['BASE_DIR'] = os.path.abspath(os.path.dirname(__file__))
app.config['ENABLE_LOGGING'] = True
app.config['LOGS_DIR'] = os.path.join(app.config['BASE_DIR'], 'logs/')
app.config['REQUEST_LOG_FILE'] = os.path.join(app.config['LOGS_DIR'], 'requests.log')

if app.config['ENABLE_LOGGING']:

    if not os.path.exists(app.config['LOGS_DIR']):
        os.mkdir(app.config['LOGS_DIR'])

    file_handler = RotatingFileHandler(app.config['REQUEST_LOG_FILE'], maxBytes=10240, backupCount=10)
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(INFO)
    app.logger.info('LOG START UP')

@app.before_request
def before_requests():
    g.start = time_now()

@app.after_request
def after_requests(request):
    pass

@app.route('/')
def index():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)
