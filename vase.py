class Vase:
    description = None
    price = None  # Rub
    volume = None  # Liters

    def __str__(self):
        return "Bowl charasteristic:\n" \
               f"{self.description}\n" \
               f"Price: {self.price} RUB\n" \
               f"Volume: {self.volume} liters"


class BaseProtectorVase(Vase):
    description = "The Glass Vase Protector proves to be a very valuable item " \
                  "if you are going to be using the Hookah frequently. The Glass " \
                  "Vase Protector is very durable, as it protects the bottom of " \
                  "the Glass Vase from breaking and the Hookah from tipping over. " \
                  "The Glass Vase Protector fits most tradition sized Middle " \
                  "Easter bell shaped bases that range from medium to large sized. "
    price = 200
    volume = 1.2


class EgyptianBohoStyleVase(Vase):
    description = "Egyptian Boho Style Hookah Vase"
    price = 1500
    volume = 1.5

