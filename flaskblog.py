from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = '447cc3d7257853eafabc30fd9c373ff8'

posts = [
    {
        'author': 'Joe Skvarna',
        'title': 'What I Think',
        'content': 'My name is Joe. This is what I think!!!',
        'date_posted': 'January 19, 2022'
    },
    {
        'author': 'Bob Mcdonald',
        'title': 'Hello World',
        'content': 'Hellow World, my name is Bob',
        'date_posted': 'January 12, 2022'
    }
]

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form=form)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)