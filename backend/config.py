import datetime

class Config:
    SECRET_KEY = "your-super-secret-key-that-is-at-least-32-characters-long-for-security"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "jwt-secret-key-that-is-also-long-enough-for-proper-security-requirements"
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=1)  # Default: 1 hour
    JWT_ACCESS_TOKEN_EXPIRES_LONG = datetime.timedelta(days=30)  # Remember Me: 30 days
