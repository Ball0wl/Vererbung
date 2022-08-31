class Tier():
    """ Klasse für das Erstellen von Säugetieren """

    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe = farbe
        self.alter = alter
        self.schlafdauer = 0

    def tut_schlafen(self, dauer):
        print(self.rufname, " schläft jetzt ", dauer, " Minuten")
        self.schlafdauer += dauer
        print(self.rufname, " Schlafdauer insgesamt: ", self.schlafdauer, "Minuten")

    def tut_reden(self, anzahl = 1):
        print(self.rufname, "sagt: ", anzahl*"Miau ")


""" super() = oberklasse. dadurch wird eine verbindung zwischen der vererbende(eltern)
 und erbenden(kinder) klasse her """


class BauplanKatzenKlasse(Tier):
    """ Klasse für das Erstellen von Katzen, in Klammer die erbende Klasse """

    def __init__(self, rufname, farbe, alter):
        """ Initalisieren über Eltern-Klasse """
        super().__init__(rufname, farbe, alter)


class Hund(Tier):
    """ Klasse für das Erstellen von Hunden, in Klammer die erbende Klasse """

    def __init__(self, rufname, farbe, alter):
        """Initalisieren über Eltern-Klasse"""
        super().__init__(rufname, farbe, alter)

    def tut_reden(self, anzahl = 1):
        print(self.rufname, "sagt: ", anzahl*"WAU ")


katze_sammy = BauplanKatzenKlasse("Sammy", "Orange", 6)
print(katze_sammy.rufname, katze_sammy.farbe, katze_sammy.alter)

hund_waldi = Hund("Waldi", "Gold", 4)
print(hund_waldi.rufname, hund_waldi.farbe, hund_waldi.alter)

hund_waldi.tut_schlafen(15)
katze_sammy.tut_schlafen(30)
katze_sammy.tut_schlafen(45)

katze_sammy.tut_reden(3)
hund_waldi.tut_reden(3)

