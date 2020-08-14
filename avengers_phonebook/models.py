from avengers_phonebook import app,db,login 
from werkzeug.security import generate_password_hash, check_password_hash 

from datetime import datetime 

#Imports for User Mixin
#To make implementing a user class easier, you can inherit from UserMixin, which provides default implementations for all of #these properties and methods.
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#inheriting from the __init__ db
class User(db.Model, UserMixin):
    # setting id to primary key
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
   
    email = db.Column(db.String(151), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    #Helping to set up the FK a many to one relationship
    phone = db.relationship('Phone', backref='author', lazy=True )

    def __init__(self,username,email,phone_number,password):
        self.username= username
        #self.realname= realname
        self.email = email
        self.phone_number = phone_number
        self.password = self.set_password(password)
    
    # don't want passwords in our database
    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
     

    def __repr__(self):
        return f'{self.username} has been created with {self.email} '

class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    realname = db.Column(db.String(300))
    alt_phone = db.Column(db.String(15))
    #ALWAYS SAVE DATETIME AS UTC TIME  saves issues down the road.
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, realname, alt_phone, user_id):
        self.realname = realname
        self.alt_phone = alt_phone
        self.user_id = user_id

    #this will print in terminal 99% of the time
    def __repr__(self):
        return f'Actual name is {self.realname} \n and the contact number is {self.alt_phone}'


