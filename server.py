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
	if 'marker' not in session:
		session['marker'] = ""
	if 'guessing' not in session:
		session['guessing'] = "visible"
	if 'reseting' not in session:
		session['reseting'] = "invisible"
	return render_template('index.html', num=session['num'], response=session['response'], marker=session['marker'], guess_class=session['guessing'], reset_class=session['reseting'])

@app.route('/guess', methods=['POST'])
def guess():
	guess = int(request.form['guess'])
	if guess == session['num']:
		#success
		print "Got it!"
		session['response'] = str(session['num']) + "  was the number!"
		session['marker'] = "box_right"
		session['guessing'] = "invisible"
		session['reseting'] = "visible"
	elif guess > session['num']:
		#too high!
		print "Too high!"
		session['response'] = "Too high!"
		session['marker'] = "box_wrong"
	elif guess < session['num']:
		#too low!
		print "Too low!"
		session['response'] = "Too low!"
		session['marker'] = "box_wrong"
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('num')
	session.pop('marker')
	session.pop('response')
	session.pop('guessing')
	session.pop('reseting')


	return redirect('/')





app.run(debug=True)
