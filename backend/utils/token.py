from itsdangerous import URLSafeTimedSerializer
from config import Config

serializer = URLSafeTimedSerializer(Config.SECRET_KEY)

def generate_reset_token(email):
    return serializer.dumps(email, salt='password-reset-salt')

def verify_reset_token(token, expiration=3600):
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=expiration)
        return email
    except:
        return None
