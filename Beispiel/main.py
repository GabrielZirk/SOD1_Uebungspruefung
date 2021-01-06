import abc
from typing import List, Dict
import math

class Instrument:
    def __init__(self, name: str, lautstaerke: float):
        self.name = name
        self.lautstaerke = lautstaerke

    def __repr__(self):
        return f"{self.name}"

class Musikant(abc.ABC):
    def __init__(self, anzahl_beine: int, instrument: Instrument):
        self.__anzahl_beine = anzahl_beine
        self.__instrument = Instrument

    @property
    def anzahl_beine(self):
        return self.__anzahl_beine

    @property
    def instrument(self):
        return self.__instrument

    @abc.abstractmethod
    def verscheuche_raeuber(self) -> int:
        pass

    @abc.abstractmethod
    def spiele_musik(self) -> float:
        pass

    def __repr__(self):
        return f"Verscheucht: {self.verscheuche_raeuber()}, Musiziert: {self.spiele_musik()}"

class Esel(Musikant):
    def __init__(self, anzahl_beine: int, instrument: Instrument, tritt_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__anzahl_beine = anzahl_beine
        self.__instrument = instrument
        self.__tritt_kraft = tritt_kraft

    @property
    def anzahl_beine(self):
        return self.__anzahl_beine

    @property
    def instrument(self):
        return self.__instrument
    @property
    def tritt_kraft(self):
        return self.__tritt_kraft

    def __repr__(self):
        return f"{__class__.__name__} {self.__tritt_kraft}: {super().__repr__()}"

    def verscheuche_raeuber(self) -> int:
        return math.floor(self.__tritt_kraft * self.__anzahl_beine)

    def spiele_musik(self) -> float:
        return self.__instrument.lautstaerke


class Hund(Musikant):
    def __init__(self, anzahl_beine: int, instrument: Instrument, bell_lautstaerke: float):
        super().__init__(anzahl_beine, instrument)
        self.__anzahl_beine = anzahl_beine
        self.__instrument = instrument
        self.__bell_lautstaerke = bell_lautstaerke

    @property
    def anzahl_beine(self):
        return self.__anzahl_beine
    @property
    def instrument(self):
        return self.__instrument
    @property
    def bell_lautstaerke(self):
        return self.__bell_lautstaerke

    def __repr__(self):
        return f"{__class__.__name__} {self.__bell_lautstaerke}: {super().__repr__()}"

    def verscheuche_raeuber(self) -> int:
        if self.__instrument.lautstaerke > self.__bell_lautstaerke:
            return math.floor(self.__instrument.lautstaerke)
        else:
            return math.floor(self.__bell_lautstaerke)

    def spiele_musik(self) -> float:
        return (self.__instrument.lautstaerke+self.__bell_lautstaerke)/2

class Katze(Musikant):
    def __init__(self, anzahl_beine: int, instrument: Instrument, kratz_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__anzahl_beine = anzahl_beine
        self.__instrument = instrument
        self.__kratz_kraft = kratz_kraft

    @property
    def anzahl_beine(self):
        return self.__anzahl_beine

    @property
    def instrument(self):
        return self.__instrument

    @property
    def kratz_kraft(self):
        return self.__kratz_kraft

    def verscheuche_raeuber(self) -> int:
        if self.__anzahl_beine == 4:
            return math.floor(self.__kratz_kraft)
        elif self.__anzahl_beine == 3:
            return math.floor(self.__kratz_kraft)/2
        elif self.__anzahl_beine <= 2:
           return 1

    def spiele_musik(self) -> float:
        return self.__instrument.lautstaerke

    def __repr__(self):
        return f"{__class__.__name__} {self.__kratz_kraft}: {super().__repr__()}"

class Hahn(Musikant):
    def __init__(self, anzahl_beine: int, instrument: Instrument, flug_weite: float):
        super().__init__(anzahl_beine, instrument)
        self.__anzahl_beine = anzahl_beine
        self.__instrument = instrument
        self.__flug_weite = flug_weite
    @property
    def anzahl_beine(self):
        return self.__anzahl_beine
    @property
    def instrument(self):
        return self.__instrument
    @property
    def flug_weite(self):
        return self.__flug_weite

    def __repr__(self):
        return f"{__class__.__name__} {self.__flug_weite}: {super().__repr__()}"

    def verscheuche_raeuber(self) -> int:
        if self.__flug_weite < 2:
            return math.floor(self.__instrument.lautstaerke)
        elif self.__flug_weite == 2:
            return 6
        elif self.__flug_weite == 3:
            return 5
        elif self.__flug_weite == 4:
            return 4
        elif self.__flug_weite == 5:
            return 3
        elif self.__flug_weite == 6:
            return 2
        elif self.__flug_weite > 6:
            return 1

    def spiele_musik(self) -> float:
        return round(((self.__instrument.lautstaerke + 2)/self.__flug_weite),2)

class Quartett:
    def __init__(self):
        self.__musikanten = []

    def add(self, Musikant: Musikant):
        self.__musikanten.append(Musikant)

    def ist_quartett(self) -> bool:
        if len(self.__musikanten) == 4:
            return True
        else:
            return False

    def gemeinsam_raeuber_verscheucht(self) -> int:
        verscheuchte_raeuber = 0
        for artist in self.__musikanten:
            verscheuchte_raeuber += artist.verscheuche_raeuber()
        return verscheuchte_raeuber

    def durchschnittliche_lautstaerke(self) -> float:
        sum_artist_lautstaerke = 0
        for artist in self.__musikanten:
            sum_artist_lautstaerke += artist.spiele_musik()
        return sum_artist_lautstaerke/len(self.__musikanten)

    def get_musikanten_in_lautstaerke_bereich(self, von: float, bis: float) -> List[Musikant]:
        artist_lautstaerke_von_bis = []
        for artist in self.__musikanten:
            if (artist.spiele_musik() > von) and (artist.spiele_musik() < bis):
                artist_lautstaerke_von_bis.append(artist)
        return artist_lautstaerke_von_bis

    def get_anzahl_musikanten_mit_bein_anzahl(self) -> Dict[int, int]:
        dict_anzahl_haxn = dict()
        for i in self.__musikanten:
            #print(i.anzahl_beine)
            if i.anzahl_beine in dict_anzahl_haxn.keys():
                dict_anzahl_haxn[i.anzahl_beine] += 1
            else:
                dict_anzahl_haxn[i.anzahl_beine] = 1
        return dict_anzahl_haxn

if __name__ == '__main__':
    floete = Instrument("Floete", 9.0)
    mundh = Instrument("Mundharmonika", 5.0)
    quetschn = Instrument("Ziehharmonika", 15.0)
    bassdrum = Instrument("Bassdrum drum drum", 10.0)
    ia = Esel(4, floete, 10.0)
    wuff = Hund(4, bassdrum, 15.0)
    miau = Katze(4, quetschn, 20.0)
    kikariki = Hahn(2, mundh, 3)
    print(ia)
    print(wuff)
    print(miau)
    print(kikariki)
    quart = Quartett()
    quart.add(ia)
    print(quart.ist_quartett())
    quart.add(wuff)
    print(quart.ist_quartett())
    quart.add(miau)
    print(quart.ist_quartett())
    quart.add(kikariki)
    print(quart.ist_quartett())
    #print(quart.ist_quartett())
    #print(quart.gemeinsam_raeuber_verscheucht())
    #print(quart.durchschnittliche_lautstaerke())
    #print(quart.get_musikanten_in_lautstaerke_bereich(12.0, 18.0))
    print(quart.get_anzahl_musikanten_mit_bein_anzahl())

