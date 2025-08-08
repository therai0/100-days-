# this is the simple flask which helps to render the html page
from flask import Flask,render_template,request

# Creating the instance of Flask class
app = Flask(__name__)
#Decorators
@app.route('/',methods=['GET']) # home page route 
def index():
    return render_template('index.html')
# contact page route
@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

# about page route
@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')







# form 
@app.route('/form',methods=['GET','POST'])
def demo_form():
    return render_template('form.html')

# form 
@app.route('/submit',methods=['GET','POST'])
def submit_data():
    if request.method == 'POST':
        username = request.form['username']
        return f'{username} Welcome to python world'
    return render_template('form.html')


# entry point to the app
if __name__ == "__main__":
    app.run(debug=True)
# debug = True 
# when we make some changes in code it automatically render it 

# this all templates are created in templates folders 