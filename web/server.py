from flask import Flask, render_template, url_for
from testing import *
app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  my_function()
  return render_template('out.html')

if __name__ == '__main__':
  app.run(debug=True)