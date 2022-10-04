import os
import sys
from flask import Flask, render_template, url_for

code_dir = os.getcwd()
print("jksaksads" , code_dir)
sys.path.insert(0, code_dir) 
from folder_structure import src_user_end
key_pair_relative = src_user_end()[0]
print("nwsdsa", key_pair_relative)
sys.path.append(key_pair_relative)
from key_pairs_address_generation import main_file
app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  # my_function()
  main_file()
  return render_template('out.html')

if __name__ == '__main__':
  app.run(debug=True)