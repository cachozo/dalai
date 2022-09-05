from flask import Flask, render_template, request, redirect, session
from dalai_app import app
from dalai_app.controllers import users_controller
from dalai_app.controllers import posts_controller
from dalai_app.controllers import likes_controller


if __name__ == "__main__":
    app.run( debug = True )


