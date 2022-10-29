import json
import os
import sys
from flask import Flask, render_template, url_for, request

server_code_dir = os.getcwd()
print("server_code_dir", server_code_dir)
os.chdir("..")
os.chdir("src")
os.chdir("user_end")
user_end_dir = os.getcwd()
sys.path.insert(1, user_end_dir)
# from folder_structure import src_user_end
# key_pair_relative = src_user_end()[0]
# print("nwsdsa", key_pair_relative)
# sys.path.append(key_pair_relative)
from key_pairs_address_generation import *
os.chdir(server_code_dir)


app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/my-link/')
def my_link():
    key_pairs = key_pairs_generation()
    addresses = address_generation()
    addresses1 = json.loads(addresses)
    print(addresses)
    main_file()
    return render_template('out.html', addresses=addresses1)
@app.route('/client-area/')
def my_link1():
    return render_template('index.html')
@app.route('/tx-generation/')
def my_link2():
    return render_template('tx-generation.html')
@app.route('/confirmation-page/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       sender_address = request.form.get("sender_address")
       receiver_address = request.form.get("receiver_address")
       amount = request.form.get("amount")
       block_number = request.form.get("block_number")
       sender_public_key = request.form.get("sender_public_key")
       sender_private_key = request.form.get("sender_private_key")
       values = {
           "sender_address": sender_address,
           "receiver_address": receiver_address,
           "amount": amount,
           "block_number": block_number,
           "sender_public_key": sender_public_key,
           "sender_private_key": sender_private_key,
       }
       return json.dumps(values)
    return render_template("confirmation.html")


if __name__ == '__main__':
    app.run(debug=True)
