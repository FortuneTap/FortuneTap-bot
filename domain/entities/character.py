from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Attributes:
    strength: int
    speed: int
    intellect: int
    willpower: int
    awareness: int
    presence: int

@dataclass_json
@dataclass
class Defenses:
    physical: int
    cognitive: int
    spiritual: int
    deflect: int

@dataclass_json
@dataclass
class Resources:
    health: int
    health_max: int
    focus: int
    focus_max: int
    investiture: int
    investiture_max: int
    movement: int
    recovery_die: int
    senses_range: int

@dataclass_json
@dataclass
class Skill:
    proficiency: int
    modifier: int

@dataclass_json
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

@dataclass_json
@dataclass
class Character:
    character_id: str
    avatar: str
    name: str
    ancestry: str
    paths: List
    attributes: Attributes
    defenses: Defenses
    resources: Resources
    skills: Skills
    expertises: List[str]
    actions: List
    equipament: List
    goals: List


