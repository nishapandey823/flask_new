from flask import Flask , request
app = Flask(__name__)# this is our main app , whenever we pass a name, we help it determine a route path

@app.route('/')# connect a web page , forward slash is a route directory or home page of your website
def index():
    return '<h2>This is the homepage</h2>' 

'''app.route('/')
def index1(): 
    return 'Method used %s' %request.Method ''' 
  

@app.route('/tuna') 
def tuna():
    return "<h2>tuna is good</h2>" 

@app.route('/profile/<username>') # making a variable (username) in your url 
def profile(username):
    return "hey there %s" % username 

@app.route('/post/<int:post>') # for int mention  datatype
def show_post(post):
    return "post id is %s" % post



if __name__ == "__main__":
    app.run(debug=True)     