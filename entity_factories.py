from components.ai import HostileEnemy
from components import consumable, equippable, quantifiable
from components import quantifiable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=350, base_defense=0, base_power=45),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

soldier = Actor(
    char="s",
    color=(63, 127, 63),
    name="Soldier",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=100, base_defense=0, base_power=25),
    inventory=Inventory(capacity=1),
    level=Level(xp_given=25),
)
hazekiller = Actor(
    char="H",
    color=(0, 127, 0),
    name="Hazekiller",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=400, base_defense=15, base_power=40),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)

confusion_scroll = Item(
    char="?",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
    stackable=True,
    quantity=quantifiable.ConfusionScroll()
)

health_potion = Item(
    char="!",
    color=(255, 0, 0),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=40),
    stackable=True,
    quantity=quantifiable.HealthPotion(),
)

large_health_potion = Item(
    char="!",
    color=(255, 0, 50),
    name="Large Health Potion",
    consumable=consumable.HealingConsumable(amount=120),
    stackable=True,
    quantity=quantifiable.LargeHealthPotion(),
)

small_knife = Item(
    char="/",
    color=(0, 180, 255),
    name="Small Knife",
    equippable=equippable.SmallKnife(),
)

knife = Item(
    char="/",
    color=(0, 191, 255),
    name="Knife",
    equippable=equippable.Knife(),
    stackable=False,
    quantity=quantifiable.Clip(),
)

blade = Item(
    char="/",
    color=(0, 191, 235),
    name="Blade",
    equippable=equippable.Blade(),
    stackable=False,
    quantity=quantifiable.Clip(),
)

sword = Item(
    char="/",
    color=(0, 191, 255),
    name="Sword",
    equippable=equippable.Sword(),
    stackable=False,
    quantity=quantifiable.Clip(),
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
    stackable=False,
)

chain_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="Chain Mail",
    equippable=equippable.ChainMail(),
    stackable=False,
)

clip = Item(
    char="*",
    color=(212, 175, 55),
    name="Clip",
    consumable=consumable.BulletConsumable(damage=50),
    quantity=quantifiable.Clip()
)
