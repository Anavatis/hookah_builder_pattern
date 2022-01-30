class Hose:
    description = None
    length = None  # Centimeteres
    price = None  # RUB

    def __str__(self):
        return "Hose charasteristic:\n" \
               f"{self.description}\n" \
               f"Price: {self.price} RUB\n" \
               f"Length: {self.length} centimeters"


class ClassicAluminiumHose(Hose):
    description = "The Dream Hose or D-Hose for short is made of silicone, " \
                  "and has a long aluminum handle. The long handle makes this " \
                  "_hose very comfortable to hold and compliments many hookahs, " \
                  "from the modern styles to the traditional. Upgrade your hookah " \
                  "for an entirely new smoking experience. This _hose will work on " \
                  "glass hookahs as well as traditional hookahs such as Khalil" \
                  " Mamoon or Magdy Zidan. When used with a traditional hookah " \
                  "you will need a hookah _hose grommet to fit it properly. Give " \
                  "your hookah the upgrade it deserves with this elegant Silicone Hookah Hose."
    price = 1900
    length = 150


class DisbosableHose(Hose):
    description = 'These Disposable Hoses are a great budget friendly replacement ' \
                  'that fit practically any hookah or can be an alternative to ' \
                  'personal mouth tips when smoking with friends. Although they ' \
                  'are considered to be disposable, they can also be washed and ' \
                  'reused multiple times.  They are made of a lightweight durable ' \
                  'plastic that can be cleaned with simply hot _water.  The _hose ' \
                  'handle measures at about 11" with a total length of the ' \
                  '_hose measuring at approximately 80" in length.'
    price = 210
    length = 203

