from components.ai import HostileEnemy
from components import consumable, equippable
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
alien = Actor(
    char="A",
    color=(0, 127, 0),
    name="Alien",
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
)
grenade = Item(
    char="#",
    color=(255, 0, 0),
    name="grenade",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    color=(255, 0, 0),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=40),
)

large_health_potion = Item(
    char="!",
    color=(255, 0, 50),
    name="Large Health Potion",
    consumable=consumable.HealingConsumable(amount=120),
)
    
lightning_shocker = Item(
    char="?",
    color=(19, 56, 190),
    name="Lightning Shocker",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

small_knife = Item(char="/", color=(0, 180, 255), name="Small Knife", equippable=equippable.SmallKnife()
)

knife = Item(
    char="/",
    color=(0, 191, 255),
    name="Knife",
    equippable=equippable.Knife()
)

blade = Item(
    char="/",
    color=(0, 191, 235),
    name="Blade",
    equippable=equippable.Blade()
)

sword = Item(
    char="/",
    color=(0, 191, 255),
    name="Sword",
    equippable=equippable.Sword()
)

lightsaber = Item(
    char="~",
    color=(0, 191, 255),
    name="Lightsaber",
    equippable=equippable.Lightsaber(),
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="Chain Mail",
    equippable=equippable.ChainMail()
)

blue_armor_chip = Item(
    char="^",
    color=(0, 95, 200),
    name="Blue Armor Chip",
    equippable=equippable.BlueChip()
)

red_armor_chip = Item(
    char="^",
    color=(255, 95, 0),
    name="Red Armor Chip",
    equippable=equippable.RedChip()
)

green_armor_chip = Item(
    char="^",
    color=(95, 255, 0),
    name="Green Armor Chip",
    equippable=equippable.GreenChip()
)