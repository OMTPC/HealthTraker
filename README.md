# Health Tracker

The **Health Tracker** is a Flask-based web application designed to help users monitor their daily health activities, including exercise, meditation, and sleep. It features user authentication and a dashboard for tracking health data, making it a practical project for showcasing full-stack development skills.

## Features

- **User Registration and Login**: Secure authentication system with hashed passwords.
- **User-Specific Health Data**: Each user can log and view their own health data.
- **Add and Track Health Activities**:
  - Exercise (in minutes)
  - Meditation (in minutes)
  - Sleep (in hours)
- **Dashboard**: Displays all logged health data for the current user.
- **Responsive and Secure**: Protects routes using user authentication.

## Technologies Used

- **Back-end**: Flask (Python), Flask-Login for user authentication, Flask-Migrate for database migrations.
- **Database**: SQLite for lightweight and efficient storage.
- **Front-end**: HTML, CSS (custom or framework-based templates, if applicable).
- **Other**: Werkzeug for password hashing, Flask-WTF for forms.

## How to Set Up the Project

### Prerequisites

- Python 3.7+ installed on your system.
- A virtual environment (recommended).
- Flask and other dependencies installed (see below).

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Health-Tracker.git
   cd Health-Tracker
Set Up a Virtual Environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
pip install -r requirements.txt
Initialise the Database:

bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Run the Application:

bash
flask run
Access the App: Open your browser and go to http://127.0.0.1:5000.

#Project Structure
graphql


#Health-Tracker/
├── app.py                # Main application file
├── forms.py              # Forms for registration, login, and health data
├── templates/            # HTML templates for rendering pages
├── static/               # Static files (CSS, JS, images, etc.)
├── migrations/           # Database migrations
├── mydatabase.db         # SQLite database file (created after migration)
├── requirements.txt      # List of project dependencies
├── venv/                 # Virtual environment (optional)
└── README.md             # Project documentation

#Usage
#Register: Create an account with a username, email, and password.
#Log In: Access your dashboard with your registered email and password.
#Log Health Data: Input your daily exercise, meditation, and sleep hours via the form.
#View Dashboard: Monitor your logged activities in a user-friendly dashboard.

##Limitations
This project is for educational purposes only and is not intended for deployment in production environments.
Data persistence is limited to SQLite, which is suitable for small-scale applications.
Logging and Debugging
This project includes basic logging for debugging and monitoring. Ensure debug=True is only used during development.

##Contribution
Contributions to enhance this project are welcome! Feel free to:

##Fork the repository.
Submit pull requests with bug fixes or new features.

##License
This project is for educational purposes only and is not licensed for commercial use. No explicit licence is provided.

