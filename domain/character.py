import json

class Character:
    def __init__(self, name, attributes, skills):
        self.name = name
        self.attributes = attributes  # Un diccionario con los atributos
        self.skills = skills          # Un diccionario con las habilidades

    def to_json(self):
        """Convierte el objeto Character a formato JSON."""
        return json.dumps({
            "name": self.name,
            "attributes": self.attributes,
            "skills": self.skills
        })

    @classmethod
    def from_json(cls, json_data):
        """Crea un objeto Character a partir de un JSON."""
        data = json.loads(json_data)
        return cls(
            name=data["name"],
            attributes=data["attributes"],
            skills=data["skills"]
        )
