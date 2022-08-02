from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {  "apiKey": "AIzaSyAcbDxtC0jlPqyEH_GuUc0hzgPD7LTrAE8",
  "authDomain": "fir-lab-81cd8.firebaseapp.com",
  "projectId": "fir-lab-81cd8",
  "storageBucket": "fir-lab-81cd8.appspot.com",
  "messagingSenderId": "140815701353",
  "appId": "1:140815701353:web:cdf0f5c658c28ec4a019f8",
  "measurementId": "G-4Y8H1V4R17", "databaseURL" : "https://fir-lab-81cd8-default-rtdb.europe-west1.firebasedatabase.app/"}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

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
		user = {'username' : request.form['username'], 'fullname' : request.form['fullname'], 'bio' : request.form['bio']}
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			db.child("Users").child(login_session['user']['localId']).set(user)
			return redirect(url_for('add_tweet'))
		except:
			error = "Authentication failed"
	return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
	if request.method == 'POST':
		try:
			tweet = {"title" : request.form['title'], "text" : request.form['text'], "uid" : login_session['user']['localId']}
			db.child("tweets").push(tweet)
			return redirect(url_for('add_tweet'))
		except:
			error = "Authentication failed"
	return render_template("add_tweet.html")
@app.route('/all_tweets',)
def tweets():
	tweet_val = db.child("tweets").child(login_session['user']['localId']).get().val()
	return render_template('tweetes.html', tweet_val = tweet_val)

if __name__ == '__main__':
	app.run(debug=True)