from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import components.inventory
from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Quantifiable(BaseComponent):
    parent: Item
    
    def __init__(
        self,
        quantity: int = 3,
    ):
        self.quantity = quantity
        
class SmallKnife(Quantifiable):
    def __init__(self) -> None:
        super().__init__(quantity = 3)
        
class Clip(Quantifiable):
    def __init__(self) -> None:
        super().__init__(quantity = 5)