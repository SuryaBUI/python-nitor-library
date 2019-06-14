#models.py
from project import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# from flask import render_template, url_for

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__='users'
    id= db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(64), unique= True, index=True)
    username=db.Column(db.String(64), unique= True, index=True)
    password_hash=db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.username=username
        self.email=email
        self.password_hash= generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Employee(db.Model):

    __tablename__ = 'employees'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.Text)
    department= db.Column(db.Text)
    # book_id=db.Column(db.Integer, db.ForeignKey('book.id'))
    hr=db.relationship('HumanResources', backref='emplo', uselist=False)
    bk=db.relationship('Book', backref='emplo',  uselist=True)


    def __init__(self, name, department, username, password):
        self.name=name
        self.department=department
        self.username=username
        self.password=password

    def __repr__(self):
        #print(dir(self), self.bk)
        # return redirect(url_for('display.html'))

        if self.bk and self.hr:
            #print("both")
            a='\n'
            return f" Employee Name:- {self.name}, Department:- {self.department}, Id:- {self.id}, HR-SPOC:- {self.hr.name}, Book Details:- {self.bk} !"
        elif self.bk:
            #print("self.book ")
            a='\n'
            return f" Employee Name:- {self.name}, Department:- {self.department}, Id:- {self.id}, HR-SPOC:- NA , Book Details:- {self.bk} !"

        elif self.hr:
            return f"Employee Name:- {self.name}, Department:- {self.department}, Id:- {self.id}, HR-SPOC:- {self.hr.name} , Book Details:- NA!"


        else:
            #print("blank")
            return f"Employee Name:- {self.name}, Department:- {self.department}, Id:- {self.id} HR:- NA, Books:- NA"

class HumanResources(db.Model):

    __tablename__="hrtable"

    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    emplo_id=db.Column(db.Integer, db.ForeignKey('employees.id'))


    def __init__(self,name, emplo_id):
        self.name=name
        self.emplo_id=emplo_id

    def __repr__(self):
        return f"HR SPOC is {self.name}"

class Book(db.Model):

    __tablename__="book"

    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text, unique= True, index=True)
    emplo_id=db.Column(db.Integer, db.ForeignKey('employees.id'))
    # emp=db.relationship('Employee', backref='boo', uselist=False)
    dateissue=db.Column(db.String)
    datesubmit=db.Column(db.String)

    def __init__(self,name, dateissue, datesubmit, emplo_id):
        self.name=name
        self.emplo_id=emplo_id
        self.dateissue=dateissue
        self.datesubmit=datesubmit

    def __repr__(self):
        return f"Name:- {self.name}, Emp_Id:- {self.emplo_id}, Issued Date:- {self.dateissue} !"
