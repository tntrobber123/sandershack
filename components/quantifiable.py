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
    quantity: int = 0,
    stackable: str = "True"
    ):
    
    	class SmallKnife(stackable, quantity):
    		def __init__(self) -> None:
    		    super().__init__(stackable = False, quantity = 0)

        class Clip(stackable, quantity):
        	def __init__(self) -> None:
                super().__init__(stackable = True, quantity = 5)
    
    		
