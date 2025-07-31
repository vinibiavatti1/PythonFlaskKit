from app.entities.entity import Entity
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class UserFilter(Entity):
    name: str | None = field(default=None)
    email: str | None = field(default=None)
    role: str | None = field(default=None)
    password_hash: str | None = field(default=None)
    email_verified: int | None = field(default=None)
    hash: str | None = field(default=None)
