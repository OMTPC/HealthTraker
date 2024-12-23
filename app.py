from flask import Flask, flash, render_template, request, redirect, url_for
from forms import HealthDataForm, RegistrationForm, LoginForm, MyForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect unauthorized users to the login page
login_manager.login_message = 'Please log in to access this page.'

# User model
class User(UserMixin, db.Model):  # Inherit UserMixin for Flask-Login
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# HealthData model
class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    meditation = db.Column(db.Integer, nullable=False)
    sleep = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key for user

    def __repr__(self):
        return f'<HealthData {self.id}>'

# Flask-Login loader for user sessions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
@login_required  # Protect this route
def form():
    form = HealthDataForm()
    if form.validate_on_submit():
        # Create a new health data entry
        new_data = HealthData(
            date=form.date.data,
            exercise=form.exercise.data,
            meditation=form.meditation.data,
            sleep=form.sleep.data,
            user_id=current_user.id  # Associate with the logged-in user
        )
        db.session.add(new_data)
        db.session.commit()
        flash('Health data added successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if the username or email already exists
        existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        if existing_user:
            if existing_user.username == form.username.data:
                flash('Username already taken. Please choose a different one.', 'danger')
            elif existing_user.email == form.email.data:
                flash('Email already registered. Please use a different email or log in.', 'danger')
            return redirect(url_for('register'))
        # Hash the password
        hashed_password = generate_password_hash(form.password.data)
        
        # Create a new user
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)  # Log the user in
            flash('Login successful!', 'success')
            next_page = request.args.get('next')  # Redirect to the intended page
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout', methods=['POST'])  # Handle only POST requests for logout
@login_required  # Protect this route
def logout():
    logout_user()  # Log the user out
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))  # Redirect to the login page

@app.route('/dashboard')
@login_required  # Protect this route
def dashboard():
    # Retrieve health data for the logged-in user
    user_data = HealthData.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
import logging
