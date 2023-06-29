from flask import Blueprint, session, request, render_template, redirect, url_for
from user import models
from db import db


user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def index():
    users = models.User.query.filter_by(status='ACTIVE').all()
    for user in users:
        print(user.user_name)
    return "I am index"

@user_bp.route("/signup", methods=["GET", "POST"])
def signup():
        if request.method == "GET":
            return render_template("user/signup.html")
        elif request.method == "POST":
            print("testtttt")
            form_data = request.form
            user_name = form_data["user_name"]
            user_password = form_data["user_password"]
            confirm_password = form_data["confirm_password"]
            mobile_number = form_data["mobile_number"]
            email = form_data["email"]

            signup = models.User(user_name=user_name, user_password=user_password, mobile_number=mobile_number, status="ACTIVE", registered_on="2023/01/02",email=email)
            db.session.add(signup)
            db.session.commit()

            return "your User has been successfully saved"

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if 'user' in session:
            return redirect(url_for('user.profile'))

        return render_template("user/login.html")
    elif request.method == "POST":
        form_data = request.form
        username = form_data["username"]
        password = form_data["password"]

        user = models.User.query.filter_by(user_name=username, user_password=password).first()

        
        if user:
            session['user'] = {
                "user_id" : user.user_id,
                "user_name" : user.user_name
            }
            return redirect(url_for('user.profile'))
        else:
            print("No user with given input")

        return render_template("user/login_data.html", data=form_data)



@user_bp.route("/profile")
def profile():

    message = request.args.get('message')

   

    if 'user' in session:
        user_id=session['user']['user_id']
        user = models.User.query.filter_by(user_id=user_id).first()

        return render_template("profile.html", data=user, message=message)

    else:
        return "User is not found"


@user_bp.route("/profile/edit", methods=["GET", "POST"])
def profile_edit():
    if request.method == "GET":
        if 'user' in session:
            user_id=session['user']['user_id']
            user = models.User.query.filter_by(user_id=user_id).first()

            return render_template("user/profile_edit.html", data=user)

    if request.method=="POST":
        if 'user' in session:
            user_id=session['user']['user_id']

            form_data = request.form

            user_name = form_data["user_name"]
            email = form_data["email"]
            mobile_number = form_data["mobile_number"]
            status = form_data["status"]
            print(mobile_number)

            user = models.User.query.get(user_id)

            if user:
                # Update columns
                user.user_name = user_name
                user.email = email
                user.mobile_number=mobile_number
                user.status=status
                
                # Commit the changes to the database
                db.session.commit()

                return redirect(url_for('user.profile', message="Your profile has been updated"))

    
       

