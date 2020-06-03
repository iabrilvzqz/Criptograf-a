# export FLASK_APP=node_server.py
# flask run --port 8000
# python3 run_app.py

import datetime
import json

import requests
from flask import url_for,render_template, redirect, request

import pymongo

from flask_login import login_user, LoginManager, login_required

from app import app

from werkzeug.security import check_password_hash

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []

client = pymongo.MongoClient(
    'mongodb+srv://betote:6hBzndMr3RLsBDFx@cluster0-3vp2d.mongodb.net/test?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')
db = client.test

def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    data = None

    if request.method == 'POST':
        employeeNumber = request.form['username']
        passwd = request.form['password']

        userInfo = db.userBlockChain.find_one({'user_id': int(employeeNumber)})

        if userInfo != None:
            password = check_password_hash(userInfo.get('password'), passwd)

            if password == True:
                return redirect(url_for('index'))
        
        error = 'Invalid Credentials. Please try again.'    
    
    return render_template('login.html', error=error)


@app.route('/index')
def index():
    fetch_posts()
    return render_template('index.html',
                           title='YourNet: Decentralized '
                                 'content sharing',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    author = request.form["author"]

    post_object = {
        'author': author,
        'content': post_content,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/index')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')