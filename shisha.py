class Shisha:
    description = None
    price = None  # Rub
    nicotine_strength = None  # Percent

    def __str__(self):
        return "Shisha charasteristic:\n" \
               f"{self.description}\n" \
               f"Price: {self.price} RUB\n" \
               f"Nicotine strength: {self.nicotine_strength}%"


class AlFakherShisha(Shisha):
    description = "Al Fakher Flavored Shisha Tobacco is Internationally renowned " \
                  "as the best Flavored Shisha Tobacco brand on the market. " \
                  "Al Fakher shisha is a premium brand of flavored shisha " \
                  "_tobacco and is used primarily by experienced Hookah users " \
                  "because of its smooth and unique smoking experience. " \
                  "The Al Fakher brand's 50g boxes allow for Hookah users to " \
                  "sample some of their top flavors at an affordable price. " \
                  "Al fakher shisha comes in an array of flavors ranging from" \
                  " modern to traditional variations.  Al Fakher shisha is probably " \
                  "the most renowned brand world wide and known for " \
                  "it great taste, smoke and consistency. "
    price = 225
    nicotine_strength = 0.05


class SerbetliShisha(Shisha):
    description = "Serbetli Shisha is imported from Turkey and is quite popular " \
                  "in Eruope, Asia and now making its way through the U.S.  " \
                  "It is definitely a shisha to try with its " \
                  "unique flavor profiles and mixes."
    price = 270
    nicotine_strength = 0.05


class NakhlaShisha(Shisha):
    description = "These 50g packs of Nakhla shisha offer a great way to sample " \
                  "many of their most popular flavors while keeping it cost effective. " \
                  "These packs also provide an easy way to try many types of " \
                  "mixes unique to you, buy one to sample or a few to create your own flavor."
    price = 260
    nicotine_strength = 0.1

