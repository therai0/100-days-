
from flask import Flask,request,render_template,redirect,url_for,flash


# creating the object of Flask class
app = Flask(__name__)

app.secret_key = 'hello world'
# login page
@app.route('/login')
def login_user():
    return render_template('login.html')


# let's create route
@app.route('/authenticate',methods=["POST","GET"])
def authenticate_page():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash('Please enter the password or username')
            return redirect(url_for('login_user'))
        return render_template('home.html',username=username)

# entry point
if __name__ == "__main__":
    app.run(debug=True)