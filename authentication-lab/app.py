from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {  "apiKey": "AIzaSyAcbDxtC0jlPqyEH_GuUc0hzgPD7LTrAE8",
  "authDomain": "fir-lab-81cd8.firebaseapp.com",
  "projectId": "fir-lab-81cd8",
  "storageBucket": "fir-lab-81cd8.appspot.com",
  "messagingSenderId": "140815701353",
  "appId": "1:140815701353:web:cdf0f5c658c28ec4a019f8",
  "measurementId": "G-4Y8H1V4R17", "databaseURL" : ""}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
         try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
         except:
           error = "Authentication failed"
    return render_template("signin.html")


    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
           login_session['user'] = auth.sign_in_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
        except:
           error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)