from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

temlate_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(temlate_dir),autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/",methods = ['GET'])
def main():
    #template = jinja_env.get_template('singup.html')
    return render_template('singup.html')


@app.route("/register" ,methods = ['POST'])
def user_name():
    # form request object with username, password, verify_password, verify_email
    user_name = request.form['username'] 
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    if (   
       user_name == '' and password == '' and
       verify == '' 
   ):
       # user_name = request.form['username'] 
        error = 'This field is required'
        return render_template('singup.html' , blank_error = error,password_error = error , verify_error = error,user = user_name,e_mail = email)
        #return redirect("/?error=" + error)
        #templates = jinja_env.get_template('welcome.html')
    if (user_name == '' and password == ''):
        error = 'This field is required'
        return render_template('singup.html' , blank_error = error,password_error = error,user = user_name,e_mail = email)
    if (password == '' and verify == ''):
        error = 'This field is required'
        return render_template('singup.html' , password_error = error,verify_error = error ,user = user_name,e_mail = email)
    if verify == '' and user_name == '':
        error = 'This field is required'
        return render_template('singup.html' , verify_error = error,blank_error = error,user = user_name,e_mail = email)
    if user_name == '':
        error = 'This field is required'
        return render_template('singup.html' , blank_error = error,user = user_name,e_mail = email)
    if password == '':
        error = 'This field is required'
        return render_template('singup.html' , password_error = error,user = user_name,e_mail = email)
    if verify == '':
        error = 'This field is required'
        return render_template('singup.html' , verify_error = error,user = user_name,e_mail = email)


    if (len(user_name) <= 3 or len(user_name) > 20 or " " in user_name) :
        error = 'username is not valid'
        return render_template('singup.html' , user_error = error,user = user_name,e_mail = email)

    if (len(password) <= 3 or len(password) > 20) or " " in password:
        error = 'password is not valid'
        return render_template('singup.html' , pass_error = error,user = user_name,e_mail = email)
    if password != verify:
        error = "please verify your password"
        return render_template('singup.html' , v_error = error,user = user_name,e_mail = email)
    if ((email.count('@') >1 or email.count('@') <1 ) or (email.count('.') > 1 or email.count('.') < 1 ) or (len(email) > 20 or (len(email) >0 and len(email) <= 3))):
        error = "email address is not valid"
        return render_template('singup.html' , e_error = error)

    return render_template('welcome.html' , username = user_name)
    





#@app.route("/password")
#def password():

#@app.route("/email")
#def email():
    


if __name__ == "__main__":
    app.run() 


