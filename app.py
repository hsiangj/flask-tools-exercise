from flask import Flask, request, redirect, flash, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def start_page():
  """Show start page with survey title and instructions"""
  title = satisfaction_survey.title
  instructions = satisfaction_survey.instructions

  return render_template('start.html', title=title, instructions=instructions)