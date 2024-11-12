from dataclasses import dataclass
from typing import List

@dataclass
class Attributes:
    strength: int
    speed: int
    intellect: int
    willpower: int
    awareness: int
    presence: int

@dataclass
class Defenses:
    physical: int
    cognitive: int
    spiritual: int
    deflect: int

@dataclass
class Derived:
    movement: int
    recovery_die: int
    senses_range: int

@dataclass
class Resources:
    health: int
    health_max: int
    focus: int
    focus_max: int
    investitute: int
    investiture_max: int

@dataclass
class Skill:
    proficiency: int
    modifier: int

@dataclass
class Skills:
    athletics: Skill
    agility: Skill
    heavy_weapons: Skill
    light_weapons: Skill
    stealth: Skill
    thievery: Skill
    crafting: Skill
    deduction: Skill
    discipline: Skill
    intimidation: Skill
    lore: Skill
    medicine: Skill
    deception: Skill
    insight: Skill
    leadership: Skill
    perception: Skill
    persuasion: Skill
    survival: Skill

@dataclass
class Character:
    character_id: str
    name: str
    attributes: Attributes
    defenses: Defenses
    resources: Resources
    derived: Derived
    skills: Skills
    expertises: List[str]
