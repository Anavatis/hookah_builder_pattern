from abc import ABC, abstractmethod

from bowl import EgyptianBowl, FunnelBowl
from charcoal import LavooCharcoal, BlackDiamondCharcoal
from hose import DisbosableHose, ClassicAluminiumHose
from shisha import SerbetliShisha, AlFakherShisha
from tray import KhalilMamoonHookahTray, LuleTurkeyTray
from vase import BaseProtectorVase, EgyptianBohoStyleVase
from water import JustWater, Wine


class Builder(ABC):
    """ Builder interface """

    @property
    @abstractmethod
    def hookah(self):
        ...

    @abstractmethod
    def set_components(self) -> None:
        ...

    @abstractmethod
    def set_shisha(self) -> None:
        ...

    @abstractmethod
    def fill_water(self) -> None:
        ...

    @abstractmethod
    def light_charcoal(self) -> None:
        ...


class CheapestHookahBuiler(Builder):

    def __init__(self):
        self._reset()

    def _reset(self):
        self._hookah = Hookah()

    @property
    def hookah(self):
        hookah_impl = self._hookah
        self._reset()  # Reset hookah assembly
        return hookah_impl

    def set_components(self):
        bowl = EgyptianBowl()
        hose = DisbosableHose()
        tray = KhalilMamoonHookahTray()
        vase = BaseProtectorVase()

        self._hookah.set_bowl(bowl)
        self._hookah.set_hose(hose)
        self._hookah.set_tray(tray)
        self._hookah.set_vase(vase)

    def set_shisha(self):
        shisha = AlFakherShisha()
        self._hookah.set_shisha(shisha)

    def fill_water(self):
        water = JustWater()
        self._hookah.set_water(water)

    def light_charcoal(self):
        charcoal = LavooCharcoal()
        self._hookah.set_charcoal(charcoal)


class ExpensiveHookahBuilder(Builder):
    def __init__(self):
        self._reset()

    def _reset(self):
        self._hookah = Hookah()

    @property
    def hookah(self):
        return self._hookah

    def set_components(self):
        bowl = FunnelBowl()
        hose = ClassicAluminiumHose()
        tray = LuleTurkeyTray()
        vase = EgyptianBohoStyleVase()

        self._hookah.set_bowl(bowl)
        self._hookah.set_hose(hose)
        self._hookah.set_tray(tray)
        self._hookah.set_vase(vase)

    def set_shisha(self):
        shisha = SerbetliShisha()
        self._hookah.set_shisha(shisha)

    def fill_water(self):
        water = Wine()
        self._hookah.set_water(water)

    def light_charcoal(self):
        charcoal = BlackDiamondCharcoal()
        self._hookah.set_charcoal(charcoal)


class Hookah:

    def __init__(self):
        self._elements_list = []

        self._bowl = None
        self._tray = None
        self._vase = None
        self._hose = None

        self._shisha = None
        self._water = None
        self._charcoal = None

    def set_bowl(self, bowl):
        self._bowl = bowl
        self._elements_list.append(bowl)

    def set_tray(self, tray):
        self._tray = tray
        self._elements_list.append(tray)

    def set_vase(self, vase):
        self._vase = vase
        self._elements_list.append(vase)

    def set_hose(self, hose):
        self._hose = hose
        self._elements_list.append(hose)

    def set_shisha(self, shisha):
        self._shisha = shisha
        self._elements_list.append(shisha)

    def set_water(self, water):
        self._water = water
        self._elements_list.append(water)

    def set_charcoal(self, charcoal):
        self._charcoal = charcoal
        self._elements_list.append(charcoal)

    def get_specification(self):
        print("Hookah specification")
        for el in self._elements_list:
            print('\n', str(el))

    def smoke(self):
        ...


class Director:
    def __init__(self, builder):
        self._builder: Builder = builder

    @property
    def builder(self) -> Builder:
        return self._builder

    def assemble_hookah(self):
        self._builder.set_components()

    def smoke_hookah_prepare(self):
        self._builder.set_components()
        self._builder.fill_water()
        self._builder.set_shisha()
        self._builder.light_charcoal()


if __name__ == '__main__':
    builder = ExpensiveHookahBuilder()
    director = Director(builder)
    director.smoke_hookah_prepare()
    hookah = director.builder.hookah
    hookah.get_specification()

