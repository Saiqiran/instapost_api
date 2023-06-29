from flask import Flask
from db import db
from config import config
from user import router as user_router
from post import router as post_router
from employee import router as employee_router

def create_app():
    print("inside create app")
    app = Flask(__name__)

    #set secret key
    app.secret_key="abc1234!@#$"

    #Connect Database
    app.config.from_object(config)
    db.init_app(app)

    #Configure routers
    app.register_blueprint(user_router.user_bp, url_prefix="/user")
    app.register_blueprint(post_router.post_bp, url_prefix="/post")
    app.register_blueprint(employee_router.employee_bp, url_prefix="/employee")
    return app


app=create_app()


if __name__=="__main__":
    app.run()