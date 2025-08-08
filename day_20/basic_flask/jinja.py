# this is the simple flask which helps to render the html page

from flask import Flask,render_template,request

# Creating the instance of Flask class
app = Flask(__name__)

# create a route to get the age from the users
@app.route('/age/<int:age>')
def check_age(age):
    message = ''
    if age > 18:
        message = 'You are eligible to marry'
    else:
        message = ' You are not eligible to marry'
    return render_template('eligible.html',message=message) 
#returing the eligible.html template with message 


# entry point to the app
if __name__ == "__main__":
    app.run(debug=True)
# debug = True 
# when we make some changes in code it automatically render it 

# this all templates are created in templates folders 