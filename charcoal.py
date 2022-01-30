class Charcoal:
    description = None
    price = None  # RUB
    size = None  # Milimeters
    coal_counts = None

    def __str__(self):
        return "Bowl charasteristic:\n" \
               f"{self.description}\n" \
               f"Price: {self.price} RUB\n" \
               f"size: {self.size} milimeters"


class CocoNaraCharcoal(Charcoal):
    description = "CocoNara Natural coals became very popular in the Middle East" \
                  " among hookah smokers because of their long burning time and " \
                  "low ash production. CocoNara coals are eco-friendly, clean burning, " \
                  "odorless and tasteless. They burn 3x longer than regular coals " \
                  "and are effort-free to light and maintain throughout your " \
                  "hookah session. If you are looking for the best hookah experience, " \
                  "let CocoNara be part of it."
    price = 1000
    size = 22
    coal_counts = 120


class BlackDiamondCharcoal(Charcoal):
    description = "Black Diamond Hookah Coals are 100% natural made from " \
                  "coconut shells. No chemicals, glues or fillers were used " \
                  "in manufacturing this product. Black Diamond coals are over " \
                  "sized cubes (25mm) and will last a minimum of 1 hour once lit. " \
                  "Enjoy your hookah with these eco friendly coals. " \
                  "These coals are a bargain since you are getting double the amount " \
                  "of the other brands at the same price without compromising quality"
    price = 1200
    size = 25
    coal_counts = 144


class LavooCharcoal(Charcoal):
    description = "Lavoo charcoal"
    price = 350
    size = 25
    coal_counts = 45