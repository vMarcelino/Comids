import secrets
import string
import datetime
import jwt
import hashlib

# Local
from constants import CONSTANTS


def generate_cryptographically_random_string(len: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(len))


def get_missing_fields(json, fields) -> set:
    missing_fields = set()
    if json:
        for field in fields:
            if field not in json:
                missing_fields.add(field)
    else:
        missing_fields = set(fields)

    return missing_fields


def are_fields_missing(json, *fields):
    missing_fields = get_missing_fields(json, fields)
    if missing_fields:
        msg = 'Missing fields: ' + ', '.join(missing_fields)
        print(msg)
        return True, msg

    return False, None


def generate_jwt(user_vertex):
    payload = {
        'sub': user_vertex.graph_value.id,
        'name': user_vertex.Properties['name'],
        'iat': datetime.datetime.utcnow()
    }
    return jwt.encode(payload=payload, key=CONSTANTS.key, algorithm='HS256').decode()


def hash_with_salt(payload, salt):
    return hashlib.sha512((payload + salt).encode()).hexdigest()