from flask import Flask, request, redirect, flash, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def start_page():
  """Show start page with survey title and instructions"""
  title = survey.title
  instructions = survey.instructions

  return render_template('start.html', title=title, instructions=instructions)


@app.route('/questions/<int:question_id>', methods = ['POST'])
def question_page(question_id):
  question = survey.questions[question_id]
  choices = survey.questions[question_id].choices
  return render_template('questions.html', question=question,question_num=question_id, choices=choices)

@app.route('/answer', methods = ['POST'])
def handle_question():
  """Save answer to list and redirect to next question."""
  answer = request.form['answer']
  responses.append(answer)
  import pdb
  pdb.set_trace()
  return redirect(f'/questions/{len(responses)}') 
  #not working - method not allowed. tried redirecting to homepage. tried using pdb debugger.

  