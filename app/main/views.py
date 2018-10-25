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

@main.route("/leaderboard",methods=['GET','POST'])
@login_required
def leaderboard():

    marvel = Score.query.filter_by(category="Marvel").order_by(Score.username,Score.score.asc()).distinct(Score.username).all()
    gaming = Score.query.filter_by(category="Gaming").order_by(Score.username,Score.score.asc()).distinct(Score.username).all()
    anime = Score.query.filter_by(category="Anime").order_by(Score.username,Score.score.asc()).distinct(Score.username).all()
    music = Score.query.filter_by(category="Music").order_by(Score.username,Score.score.asc()).distinct(Score.username).all()

    title="Leaderboard"
    return render_template('leaderboard.html',title=title,marvel=marvel,gaming=gaming,anime=anime,music=music)

@main.route("/profile",methods=['GET','POST'])
@login_required
def profile():

    marvel = Score.query.filter_by(username=current_user.username).order_by(Score.username,Score.score.asc()).all()
    gaming = Score.query.filter_by(username=current_user.username).order_by(Score.username,Score.score.asc()).all()
    anime = Score.query.filter_by(username=current_user.username).order_by(Score.username,Score.score.asc()).all()
    music = Score.query.filter_by(username=current_user.username).order_by(Score.username,Score.score.asc()).all()



    title="Profile"
    return render_template('profile.html',title=title,marvel=marvel,gaming=gaming,anime=anime,music=music,user=current_user)


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

    if score>4:
        if score==5:
            badge="Veteran"
        elif score>5 and score<11:
            badge="Surveyor"
        elif score>10 and score<21:
            badge="Hardcore"
        elif score>20 and score<31:
            badge="Defier"
        elif score>30:
            badge="Lost Soul"
        else:
            badge="No badge acquired"

        new_score = Score(username=username,score=score,category=category,badge=badge)
        db.session.add(new_score)
        db.session.commit()

    else:
        return "nothing"

    current_user.points=0
    db.session.add(current_user)
    db.session.commit()


    print(new_score)
    return "nothing"

@main.route('/add_marvel')
def add_marvel():

    username = current_user.username
    score = current_user.points
    category ="Marvel"

    if score>4:
        if score==5:
            badge="Veteran"
        elif score>5 and score<11:
            badge="Surveyor"
        elif score>10 and score<21:
            badge="Hardcore"
        elif score>20 and score<31:
            badge="Defier"
        elif score>30:
            badge="Lost Soul"
        else:
            badge="No badge acquired"

        new_score = Score(username=username,score=score,category=category,badge=badge)
        db.session.add(new_score)
        db.session.commit()

    else:
        return "nothing"

    current_user.points=0
    db.session.add(current_user)
    db.session.commit()


    print(new_score)
    return "nothing"

@main.route('/add_anime')
def add_anime():

    username = current_user.username
    score = current_user.points
    category ="Anime"

    if score>4:
        if score==5:
            badge="Veteran"
        elif score>5 and score<11:
            badge="Surveyor"
        elif score>10 and score<21:
            badge="Hardcore"
        elif score>20 and score<31:
            badge="Defier"
        elif score>30:
            badge="Lost Soul"
        else:
            badge="No badge acquired"

        new_score = Score(username=username,score=score,category=category,badge=badge)
        db.session.add(new_score)
        db.session.commit()

    else:
        return "nothing"

    current_user.points=0
    db.session.add(current_user)
    db.session.commit()


    print(new_score)
    return "nothing"

@main.route('/add_music')
def add_music():

    username = current_user.username
    score = current_user.points
    category ="Music"

    if score>4:
        if score==5:
            badge="Veteran"
        elif score>5 and score<11:
            badge="Surveyor"
        elif score>10 and score<21:
            badge="Hardcore"
        elif score>20 and score<31:
            badge="Defier"
        elif score>30:
            badge="Lost Soul"
        else:
            badge="No badge acquired"

        new_score = Score(username=username,score=score,category=category,badge=badge)
        db.session.add(new_score)
        db.session.commit()

    else:
        return "nothing"

    current_user.points=0
    db.session.add(current_user)
    db.session.commit()



    print(new_score)
    return "nothing"
