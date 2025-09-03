class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return all pets that have this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Validate that the pet is a Pet instance
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        pet.owner = self


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name} type={self.pet_type} owner={self.owner.name if self.owner else None}>"

# Adding method to get sorted pets by name for an Owner instance
def get_sorted_pets(self):
    return sorted(self.pets(), key=lambda pet: pet.name)

# Attach the method to Owner class
setattr(Owner, "get_sorted_pets", get_sorted_pets)
