from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane',
        'title': 'Blog Post 1',
        'content': 'Jane post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)