
class Canzone:
    def __init__(self, titolo, artista, anno, durata):
        self._titolo = titolo
        self._artista = artista
        self._anno = anno
        self._durata = durata

    def __str__(self):
        return f"{self._titolo}, {self._artista}, {self._anno}, {self._durata}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(titolo='{self._titolo}', artista='{self._artista}', anno='{self._anno}', durata='{self._durata}')")

    # Per consentire a due oggetti di classe Canzone di confrontarsi con ==
    # devo andare a RIdefinire (in override) nella classe il metodo __eq()__, con l'algoritmo
    # di confronto tra i parametri di self e quelli di other

    def __eq__(self, other):
        if self._titolo == other._titolo and self._artista == other._artista:
            return True
        else:
            return False

    def __hash__(self):
        pass

    # Analogamente, se voglio che oggetti di tipo canzone siano
    # ordinabili, posso andare a RIdefinire (in override) il metodo __lt()__
    def __lt__(self, other):
        if self._anno == other._anno:
            return self._durata > other._durata
        else:
            return self._anno > other._anno