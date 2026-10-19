from dataclasses import dataclass

@dataclass(eq=True, order=True)
class Canzone:
    _titolo : str
    _artista : str
    _anno : int (compare=False) # Esclude il campo da ordin.
    _durata : str # "mm:ss"

    # Se diciamo alla dataclass di creare
    # anche i metodi di confronto ed ordinam.
    # vengono creati __eq()__ e __lt()__
    # che usano TUTTI GLI ATTRIBUTI

c = Canzone("T", "A", "1999", "5:23")
print(c)