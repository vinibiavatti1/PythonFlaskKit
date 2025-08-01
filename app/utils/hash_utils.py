from hashlib import sha256
import os


def hash(data: str) -> str:
    data_bytes = (data + os.getenv('SALT', '')).encode('utf-8')
    hasher = sha256()
    hasher.update(data_bytes)
    return hasher.hexdigest()
