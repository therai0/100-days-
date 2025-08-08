
from flask import Flask
# Creating the instance of Flask class
app = Flask(__name__)
#Decorators
@app.route('/') # home page route 
def index():
    return "Hi welcome to Python world" 

# contact page route
@app.route('/contact')
def contact():
    return "This is contact page"

# about page route
@app.route('/about')
def about():
    return "This is about page" 

# entry point to the app
if __name__ == "__main__":
    app.run(debug=True)
# debug = True 
# when we make some changes in code it automatically render it 
