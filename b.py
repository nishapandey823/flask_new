#HTTP methods : "GET" AND "POST"
# WHENEVER YOU WANT USER TO SUBMIT SOME INFORMATION , USE "POST" e.g. forrms

from flask import Flask , request
app = Flask(__name__)


@app.route('/')
def index1():
    return "method used : %s" % request.method

@app.route('/form' , methods = ['GET' , 'POST']) # by defaut handles get , thats why using methods
def form():
    if request.method == 'POST':
        return "you are using POST"
    else: 
        return "you are using GET"  


if __name__ == "__main__":
    app.run(debug=True)