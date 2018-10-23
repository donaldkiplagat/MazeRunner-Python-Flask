from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import *
from ..import db,photos
from ..models import User,Question,Role
from flask_login import login_required,current_user
import markdown2
from ..email import mail_message

@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    title="MazeRunner"
    return render_template('index.html',title=title)

@main.route("/gaming",methods=['GET','POST'])
def gaming():
    questions = Question.query.all()
    print(questions)
    title="Gaming"
    return render_template('gaming.html',title=title,questions=questions)
