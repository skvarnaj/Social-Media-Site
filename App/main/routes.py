from flask import Blueprint
from flask import render_template, request
from App.models import Post

main = Blueprint('main', __name__)

@main.route("/home")
@main.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page = 5)
    return render_template('home.html', posts=posts)

@main.route("/news")
def news():
    return render_template('news.html', title = 'News')
