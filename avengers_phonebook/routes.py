from avengers_phonebook import app, db, Message, mail
from flask import render_template, request, redirect, url_for

#Import the form
from avengers_phonebook.forms import UserInfoForm
from avengers_phonebook.forms import LoginForm
from avengers_phonebook.forms import PhoneForm

#Import from Models
from avengers_phonebook.models import User, Phone, check_password_hash


#Import for Flask-logins - loginrequired, current usaer and logout _user
from flask_login import login_required, login_user, current_user, logout_user


#Home page route
@app.route('/')  # decorator
def home():
    phones = Phone.query.all()
    return render_template("home.html", phones = phones)



#Register route
@app.route('/register', methods= ['GET','POST'])  # decorator
def register():
    form = UserInfoForm()
    #form.validate is checking the CSFR token thing, if the request is a GET it just renders the form
    # if the request == post then the user info entered is SENT
    if request.method == 'POST' and form.validate():
        #Get Information
        username = form.username.data
        email = form.email.data
               
        password = form.password.data     
        print("\n", username, email,  password)  # this will print out in terminal
        #Create and instance of User-- look at the __init__ in models
        user = User(username, email, password)
        #Open and insert into db - connecting to db like an insert statement
        db.session.add(user)
        # lik git add and then commit Save info to db
        db.session.commit()

        #Flask email sender
        msg = Message(f'Thanks for signing up, {username}', recipients= [email])
        msg.body= ('Congrats on signing up!')
        msg.html = ('<h1>Great to have your contact info</h1>' '<p> I can do this all day</p>')
        mail.send(msg)

    return render_template("register.html", form=form)



#Add phone route
@app.route('/add_phone', methods= ['GET','POST'])  # decorator
@login_required 
def add_phone():
    form = PhoneForm()
    #form.validate is checking the CSFR token thing, if the request is a GET it just renders the form
    # if the request == post then the user info entered is SENT
    if request.method == 'POST' and form.validate():
        #Get Information
        realname = form.realname.data        
        alt_phone = form.alt_phone.data
        print("\n", realname,alt_phone)  # this will print out in terminal

        #Create and instance of User-- look at the __init__ in models
        user_id = current_user.id 
        phone = Phone(realname,alt_phone, user_id)
        #Open and insert into db - connecting to db like an insert statement
        db.session.add(phone)
        # lik git add and then commit Save info to db
        db.session.commit()
        return redirect(url_for('add_phone'))

    return render_template("add_phone.html", form=form)



@app.route('/phones/<int:phone_id>')
@login_required
def phone_detail(phone_id):
    phone = Phone.query.get_or_404(phone_id)  # get_or404 throws and exception if your post_id does not exist, 404 is a clinet error
    return render_template('phone_detail.html',phone=phone)



@app.route('/phones/update/<int:phone_id>', methods=['GET', 'POST'])
@login_required
def phone_update(phone_id):
    phone = Phone.query.get_or_404(phone_id)
    update_form = PhoneForm()

    if request.method == 'POST' and update_form.validate():
        realname= update_form.realname.data
        alt_phone= update_form.alt_phone.data
        user_id = current_user.id
        
        #Update post with more info
        phone.realname = realname
        phone.alt_phone = alt_phone
        phone.user_id = user_id

        #Commit changes, we don't do add because we are just updating
        db.session.commit()
        return redirect(url_for('phone_update', phone_id=phone.id))

    return render_template('phone_update.html', update_form=update_form) 



@app.route('/phones/delete/<int:phone_id>', methods=['POST'])
@login_required
def phone_delete(phone_id):
    phone = Phone.query.get_or_404(phone_id)
    db.session.delete(phone)
    #Commit changes, we don't do add because we are just updating
    db.session.commit()
    return redirect(url_for('home'))  



# Login route
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm() # create instance of login form
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
         # runs the same hash method on the entered password and then matches
         #  the hash  - returns True or false
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login')) # this is a GET request, like a refresh
        
    return render_template('login.html', form = form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

