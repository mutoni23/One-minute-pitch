from flask import render_template,request,redirect,url_for
from . import main
# from .forms import ReviewForm
from ..models import User
from flask_login import login_required

@main.route('/')
@login_required
def index():
    return render_template('index.html')