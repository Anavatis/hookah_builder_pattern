class Tray:
    description = None
    price = None  # RUB
    large = None  # Centimeters

    def __str__(self):
        return "Tray charasteristic:\n" \
               f"{self.description}\n" \
               f"Price: {self.price} RUB\n" \
               f"Large: {self.large} centimeters"


class LuleTurkeyTray(Tray):
    description = "This hand-crafted hookah _tray will fit all KM hookahs and " \
                  "other hookahs which have a platform for a _tray to sit on. " \
                  "It is hand crafted in Turkey and is made of the finest material. " \
                  "The amount of detail in this _tray will bring out the beauty " \
                  "in any hookah. Complete your hookah with the finest and most " \
                  "intricately designed _tray. Match your hookah with any of the " \
                  "available colors or contrast it with a different color for " \
                  "an extra special and unique look."
    price = 2400
    large = 25


class KhalilMamoonHookahTray(Tray):
    description = "Khalil Mamoon Hookah Tray Matt Black"
    price = 1400
    large = 20