# this is the costume module which helps to check the strength of password
""" A module is simply a .py file containing Python code — functions, classes, variables, etc. """

# this function use to check the password strenght 
def is_password_strong(pswd):
    # if password length is smaller the 6 it is weak password
    if len(pswd) < 6:
        return "weak"
    if not any(x.isdigit() for x in pswd): #check there is digit or not
        return "weak"
    if not any(y.islower() for y in pswd): #check is there any char are in small letter
        return "weak"
    if not any(z.isupper() for z in pswd): #check any char are in captial or not
        return "weak"
    special_char = "!@#$%^&**()~+_"
    if not any(a in special_char for a in pswd): # this will check the special character
        return "weak"
    else:
        return "Strong"
    
