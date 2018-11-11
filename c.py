##using html

from flask import Flask , request , render_template
app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>Hie</h2>'

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html" , name=name)
    

if __name__ == "__main__" :
    app.run(debug=True)    
