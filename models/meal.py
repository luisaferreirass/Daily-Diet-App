class Meal:
    def __init__(self, id, name, description, date, hour, inTheDiet) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.hour = hour 
        self.inTheDiet = inTheDiet
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "hour": self.hour,
            "inTheDiet": self.inTheDiet
        }
        