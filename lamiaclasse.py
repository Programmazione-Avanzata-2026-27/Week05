
# In un modulo dovrebbero esserci le definizioni
# dei miei dati/tipo di dati, le mie funzioni, ...

LA_MIA_COSTANTE = 67

class LaMiaClasse:
    def __init__(self, attributo):
        self._attributo = attributo

    def funzione(self):
        print("Funzione invocata")


# print("Questa istruzione è contenuta nel file lamiaclasse.py")

# Codice di test della classe, che però non voglio
# venga eseuito quando importo il modulo da un
# altro programma: basta usare if __name__ ...
if __name__ == "__main__":
    prova = LaMiaClasse(56)
    prova.funzione()

