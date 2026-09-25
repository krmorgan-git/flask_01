# Flask_01

A basic Flask authentication app built with the application factory pattern.

## Features
- User registration, login, and logout
- Password hashing (werkzeug)
- CSRF protection (Flask-WTF / WTForms)
- SQLAlchemy models backed by SQLite

## Getting Started

1. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   flask --app app:create_app run
   ```
4. Visit http://127.0.0.1:5000 and register an account.

## Project Structure
```
app/
  auth/        # login/register/logout blueprint
  main/        # index/about blueprint
  templates/   # Jinja2 templates
  static/css/  # styles
  models.py    # User model
  extensions.py# SQLAlchemy / login manager
```

## Notes
- `SECRET_KEY` defaults to a dev value — set `SECRET_KEY` as an env var in production.
- This is a development demo; do not deploy as-is.