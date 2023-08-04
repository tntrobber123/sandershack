from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import components.inventory
from components.base_component import BaseComponent

if TYPE_CHECKING:
	from entity import Actor, Item


class Quantifiable(BaseComponent):
	def __init__(self, quantity: int = 3, change: int = 0):
		self.quantity = quantity
		self.change = change
		
	def modify(quantity, change):
		quantity += change
		return quantity

class SmallKnife(Quantifiable):
	def __init__(self, quantity: int):
		self.quantity = quantity
	
	def modify(self, change):
		quantity = self.parent.quantity
		quantity += change
		return quantity
		
class Clip(Quantifiable):
	def __init__(self):
		self.quantity = 5
		
	def modify(self, change):
		quantity = self.quantity
		quantity += change
		return quantity
