from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Entity(ABC):
    id: int = field(default=0)
    created_at: datetime | None = field(default=None)
    updated_at: datetime | None = field(default=None)
    active: int = field(default=1)
