from flask import Flask, render_template, request
from dnd import dnd_check
import json


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home_page():
    '''
    Render home page
    '''
    error = None
    data = None
    if 'phone_number' in request.args:
        data = {}
        number = request.args.get('phone_number')
        resp = json.loads(dnd_check.check_dnd(number))
        data['phone_number'] = resp.keys()[0]
        data['dnd_status'] = resp[resp.keys()[0]][2]
        print data
        return render_template('index.html', error=error, data=data)
    else:
        error = "Need valid number"
        return render_template('index.html', error=error)


if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0')
