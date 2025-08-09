from flask import Flask,flash,url_for,redirect,render_template
from forms import Form_validation

# creating object of Flask
app = Flask(__name__)

app.secret_key = "Apple_ball"

@app.route('/register',methods=["POST","GET"])
def register():
    form  = Form_validation()
    if form.validate_on_submit():
        email = form.email.data
        print(email)
        return redirect(url_for('dash_board'))
    return render_template('register.html',form=form)

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/dashboard')
def dash_board():
    return render_template('main.html')
if __name__ == "__main__":
    app.run(debug=True)