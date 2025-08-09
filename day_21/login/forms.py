from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length


# creating the class which helps to validate the form 

# inherit from the FlaskForm
class Form_validation(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=8)])
    submit = SubmitField("Register")

# this class helps to validate the form 
# we cal costumize the validate message 
# validator= [DataReuired("Please enter the message")]
    