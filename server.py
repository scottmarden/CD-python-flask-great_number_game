from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "Test"
import random

@app.route('/')
def index():
	if 'num' not in session:
		session['num'] = random.randrange(0, 101)
		print session['num']
	if 'response' not in session:
		session['response'] = ""
	return render_template('index.html', num=session['num'], response=session['response'])

@app.route('/guess', methods=['POST'])
def guess():
	guess = int(request.form['guess'])
	if guess == session['num']:
		#success
		# print "Got it!"
		session['response'] = str(session['num']) + "  was the number!"
	elif guess > session['num']:
		#too high!
		# print "Too high!"
		session['response'] = "Too high!"
	elif guess < session['num']:
		#too low!
		# print "Too low!"
		session['response'] = "Too low!"
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('num')
	session.pop('response')
	return redirect('/')


app.run(debug=True)
