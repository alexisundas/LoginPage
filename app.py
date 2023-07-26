import csv
import os
import time
from flask import Flask,render_template,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired,Email,Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user




app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(28)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def get_user(ident):
    return User.query.get(int(ident))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.errorhandler(404)
def not_found(e):
    flash("Looks like the page doesn't exist.")
    return render_template('404.html')

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(120))
    email = db.Column(db.String(50), unique=True, nullable=False)



class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=6,max=80)])

class RegisterForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(),Email(message="Invalid E-mail"),Length(max=80)])
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=6,max=80)])


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password ,form.password.data):
                login_user(user)
                return redirect(url_for('home'))
        else:
            flash("Invalid e-mail or password", "info")
            return redirect("404")       
    return render_template('login.html', form=form)


@app.route('/220194',methods=['GET','POST'])
def signup():
    form = RegisterForm()
    hashed_password = generate_password_hash(form.password.data,method='sha256')
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html',form=form)

@app.route('/')
@login_required
def home():
    reader = csv.reader(open('groups.csv', 'r'))
    group_list = []
    for row in reader:
        group_list.append({
        row[0]: row[1],
        })
    return render_template('index.html', name=current_user.username ,group=group_list)

@app.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('login'))


@app.route('/404')
def error():
    return render_template("404.html")

@app.route('/help')
@login_required
def help():
    return render_template("help.html",name=current_user.username)

@app.route('/contact')
def contact():
    return render_template('contact.html')

  
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=80) 


