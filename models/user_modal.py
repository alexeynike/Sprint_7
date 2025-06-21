from dataclasses import dataclass
from typing import Optional


@dataclass
class UserModel:
    login: str
    password: str
    firstName: Optional[str] = None

