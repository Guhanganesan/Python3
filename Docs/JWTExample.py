"""
JSON Web Tokens (JWT) are a compact and self-contained way to represent information between parties as a JSON object. 
They're often used for authentication and information exchange.

pip install pyjwt
"""

import jwt
import datetime

# Secret key for encoding and decoding JWT
SECRET_KEY = 'your_secret_key' # Don't hard code like this get it from payload

# Function to create a JWT
def create_jwt(payload, secret_key, algorithm='HS256'):
    # Add expiration time to payload
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    # Encode payload to create JWT
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token

# Function to decode a JWT
def decode_jwt(token, secret_key, algorithms=['HS256']):
    try:
        # Decode JWT and return payload
        payload = jwt.decode(token, secret_key, algorithms=algorithms)
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid token.")
    return None

# Example usage
if __name__ == "__main__":
    # Payload with user information
    payload = {'user_id': 123, 'username': 'johndoe'}

    # Create JWT
    token = create_jwt(payload, SECRET_KEY)
    print(f"JWT: {token}")

    # Decode JWT
    decoded_payload = decode_jwt(token, SECRET_KEY)
    print(f"Decoded Payload: {decoded_payload}")


