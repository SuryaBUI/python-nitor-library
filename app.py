#app.py at project folder
from project import app, db
from flask import render_template, redirect,request,url_for, flash,abort
from flask_login import login_user, login_required, logout_user
from project.models import User
from project.forms import LoginForm, RegisterForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You Logged Out")
    return redirect(url_for('home'))


@app.route('/login', methods= ['GET','POST'])
def login():
    form= LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('logged in success!')

            next = request.args.get('next')

            if next== None or not  next[0]=='/':
                next= url_for('welcome_user')

            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/register', methods= ['GET','POST'])
def register():

    form= RegisterForm()

    if form.validate_on_submit():
        email= form.email.data
        username= form.username.data
        password= form.password.data
        user= User(email, username, password)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for Registeration!")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
