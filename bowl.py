class Bowl(object):
    description = None
    price = None  # RUB
    roominess = None  # Grams

    def __str__(self):
        return "Bowl charasteristic:\n" \
               f"{self.description}\n" \
               f"Price: {self.price} RUB\n" \
               f"Roominess: {self.roominess} grams"


class EgyptianBowl(Bowl):
    description = "This Clay Bowl resembles the Traditional type of Clay Bowl " \
                  "that has been used to smoke Flavored Tobacco for centuries. " \
                  "This glossy brown clay bowl is very sturdy, and will most likely " \
                  "fit on any type of Hookah. This type of Clay Bowl is preferred " \
                  "by Hookah smokers who are looking to cater their Hookah with " \
                  "a more traditional type of bowl. The Clay Bowl provides for " \
                  "many benefits, as it does not stain or rust, is easy to clean, " \
                  "and retains a large amount of heat when smoking with the Hookah."
    price = 312
    roominess = 7


class SiliconeBowl(Bowl):
    description = 'You may be thinking "Wait a Minute... How can I burn Shisha ' \
                  'inside a Silicone Bowl with scorching hot charcoals sitting ' \
                  'on top"? The answer is, that silicone is heat resistant and ' \
                  'can withstand up to 600 degrees Fahrenheit temperatures without' \
                  ' melting. Now you can enjoy your favorite shisha in a bowl which' \
                  ' is practically indestructible and the best part is, you do not ' \
                  'need a rubber grommet since the bowl itself provides a ' \
                  'tight fit around your hookah.'
    price = 720
    roominess = 12


class FunnelBowl(Bowl):
    description = "The Shika Large Clay Funnel Bowl id made in the traditional " \
                  "style of hookah bowl making while taking on a modern hookah bowl" \
                  " design. It holds approximately 40 grams of shisha if packed tightly." \
                  " The Shika Funnel Bowl is great for almost any type of shisha, " \
                  "especial the modern style shisha which tends to be more juicy " \
                  "than the traditional shisha. The Shika funnel bowl is great for " \
                  "shisha brands such as Hookafina, Al Fakher, Starbuzz, Fantasia, Fumari and Haze."
    price = 900
    roominess = 18
