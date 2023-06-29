from flask import Blueprint, session, request, render_template, redirect, url_for, jsonify
from post import model
from .model import Post
from db import db

post_bp= Blueprint("post", __name__)

#read all posts
@post_bp.route("/")
def index():
    #Get all the rows from post table.abs
    #convert db row to json
    #send the json to template to display in ui

    posts = Post.query.all()
    serialized_posts = [{'post_id': post.post_id, 'post_title': post.post_title, 'post_body': post.post_body, 'post_tags': post.post_tags, 'user_id': post.user_id} for post in posts]
    
    return render_template("post/index.html", posts=serialized_posts)



#to display a post by post_id
@post_bp.route("<int:post_id>")
def read_post(post_id):
    #query data from database table post by post_id
    post =Post.query.get(post_id)
    
    #render html page and send post data to html page
    return render_template("post/display_post.html", post=post)

#create post
@post_bp.route("/", methods=["GET", "POST"])
def create_post():
    #when request is get then display crete form
    #check whether user is logged in, otherwise redirect the user to login page.
    if request.method == "GET":
        if 'user' in session:
            message = request.args.get('message')
            if message==None:
                message=""

            return render_template("create_post.html", message=message)
        else:
            return redirect(url_for("user.login"))
        
    elif request.method == "POST":
        form_data = request.form
        post_title = form_data["post_title"]
        post_body = form_data["post_body"]
        post_tags = form_data["post_tags"]
        
        #get the userid from session, since user is already logged in and the user name and id is saved in session
        userSession=session.get("user")
        user_id = userSession.get('user_id')


        post = model.Post( post_title=post_title, post_body=post_body, post_tags=post_tags, user_id=user_id)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('post.create_post', message="your post has been successfully saved"))

   

@post_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):

    post_details = Post.query.get(post_id)

    if request.method=="GET":
        return render_template("post/edit_post.html", post=post_details)

    elif request.method=="POST":
        form_data = request.form

        post_title = form_data["post_title"]
        post_body = form_data["post_body"]
        post_tags = form_data["post_tags"]

        post_details.post_title=post_title
        post_details.post_body=post_body
        post_details.post_tags=post_tags
        
        db.session.commit()

        return redirect(url_for("post.read_post", post_id=post_id))

