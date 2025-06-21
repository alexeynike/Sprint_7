from dataclasses import dataclass
from typing import List


@dataclass
class OrderModel:
    firstName: str
    lastName: str
    address: str
    metroStation: str
    phone: str
    rentTime: int
    deliveryDate: str
    comment: str
    color: List[str]
