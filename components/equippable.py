from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        power_bonus: int = 0,
        defense_bonus: int = 0,
        xp_mod: int = 1,
    ):
        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.xp_mod = xp_mod


class SmallKnife(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=20)

class Knife(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=30)
        
class Blade(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=40)
        
class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=50)
        
class Lightsaber(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.LEGANDARY, power_bonus=100)

class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=10)

class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=30)
        
class BlueChip(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.AMULET, defense_bonus=10)
        
class RedChip(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.AMULET, power_bonus=10)
        
class GreenChip(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.AMULET, xp_mod=2)