from flask import Flask, request, redirect, flash, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def start_page():
  """Show start page with survey title and instructions"""
  responses.clear()
  title = survey.title
  instructions = survey.instructions

  return render_template('start.html', title=title, instructions=instructions)

@app.route('/answer', methods = ['POST'])
def handle_question():
  """Save answer to list and redirect to next question."""
  answer = request.form['answer']
  responses.append(answer)

  if(len(responses) == len(survey.questions)):
    return redirect('/complete')
  else:
    return redirect(f'/questions/{len(responses)}')
  
@app.route('/questions/<int:question_id>')
def show_question(question_id):
  """Display current question."""
  question = survey.questions[question_id]
  choices = survey.questions[question_id].choices

  if(responses is False):
    return redirect('/')
  
  if(len(responses) == len(survey.questions)):
    return redirect('/complete')
  
  if(question_id != len(responses)):
    flash(f'Invalid question id: {question_id}')
    return redirect(f'/questions/{len(responses)}')

  return render_template('questions.html', question=question, question_id=question_id, choices=choices)

@app.route('/complete')
def complete():
  """Survey complete. Show completion page."""
  return render_template('complete.html')

  