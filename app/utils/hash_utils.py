from app.props import props
from hashlib import sha256


def hash(data: str) -> str:
    data_bytes = (data + str(props['salt'])).encode('utf-8')
    hasher = sha256()
    hasher.update(data_bytes)
    return hasher.hexdigest()
