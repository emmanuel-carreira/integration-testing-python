from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
    role: str
    enabled: bool
