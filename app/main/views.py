from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import *
from ..import db,photos
from ..models import User,Game,Marvel,Role,Music,Anime,Score
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
@login_required
def gaming():
    questions = Game.query.all()



    title="Gaming"
    return render_template('gaming.html',title=title,questions=questions)

@main.route("/marvel",methods=['GET','POST'])
@login_required
def marvel():
    questions = Marvel.query.all()

    title="Marvel"
    return render_template('marvel.html',title=title,questions=questions)

@main.route("/music",methods=['GET','POST'])
@login_required
def music():
    questions = Music.query.all()

    title="Music"
    return render_template('music.html',title=title,questions=questions)

@main.route("/anime",methods=['GET','POST'])
@login_required
def anime():
    questions = Anime.query.all()

    title="Anime"
    return render_template('anime.html',title=title,questions=questions)

@main.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"

@main.route('/add_points')
def add_points():

    user = current_user.email
    points=current_user.points
    point_new = points+1
    current_user.points = point_new

    db.session.add(current_user)
    db.session.commit()

    print(user)
    print(point_new)
    print(points)
    return "nothing"

@main.route('/add_gaming')
def add_gaming():

    username = current_user.username
    score = current_user.points
    category ="Gaming"
    badge ="Veteran Badge"

    current_user.points=0
    db.session.add(current_user)
    db.session.commit()

    new_score = Score(username=username,score=score,category=category,badge=badge)
    db.session.add(new_score)
    db.session.commit()

    print(new_score)
    return "nothing"

@main.route('/add_marvel')
def add_marvel():

    username = current_user.username
    score = current_user.points
    category ="Marvel"
    badge ="S.H.I.E.L.D Badge"

    current_user.points=0
    db.session.add(current_user)
    db.session.commit()

    new_score = Score(username=username,score=score,category=category,badge=badge)

    db.session.add(new_score)
    db.session.commit()

    print(new_score)
    return "nothing"

@main.route('/add_anime')
def add_anime():

    username = current_user.username
    score = current_user.points
    category ="Anime"
    badge ="Warrior Badge"

    current_user.points=0
    db.session.add(current_user)
    db.session.commit()

    new_score = Score(username=username,score=score,category=category,badge=badge)

    db.session.add(new_score)
    db.session.commit()

    print(new_score)
    return "nothing"

@main.route('/add_music')
def add_music():

    username = current_user.username
    score = current_user.points
    category ="Music"
    badge ="Music Master Badge"

    current_user.points=0
    db.session.add(current_user)
    db.session.commit()

    new_score = Score(username=username,score=score,category=category,badge=badge)

    db.session.add(new_score)
    db.session.commit()

    print(new_score)
    return "nothing"
