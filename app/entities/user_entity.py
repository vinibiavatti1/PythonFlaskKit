from app.entities.entity import Entity
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class UserEntity(Entity):
    name: str = field(default='')
    email: str = field(default='')
    role: str = field(default='user')
    password_hash: str = field(default='')
    last_login: datetime | None = field(default=None)
    email_verified: int = field(default=0)
    hash: str = field(default='')
