class Water:
    description = None
    price_per_liter = None  # Rub
    density = None  # kg/m3

    def __str__(self):
        return "Bowl charasteristic:\n" \
               f"{self.description}\n" \
               f"Price per liter: {self.price_per_liter} RUB\n" \
               f"density: {self.density} kg/m3"


class JustWater(Water):
    description = "Just tap _water"
    price_per_liter = 0.032
    density = 997


class Wine(Water):
    description = "Wine?"
    price_per_liter = 1500
    desnity = 1080
