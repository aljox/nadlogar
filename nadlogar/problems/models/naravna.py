from .meta import *


class DeliteljVeckratnik(Problem):
    """Problem za izračun največjega skupnega delitelja in najmanjšega skupnega večkratnika danega števila."""

    minimalna_vrednost = models.PositiveSmallIntegerField(
        "minimalna vrednost",
        help_text="Najmanjša možna vrednost katerega izmed števil",
        default=20,
    )

    maksimalna_vrednost = models.PositiveSmallIntegerField(
        "maksimalna vrednost",
        help_text="Največja možna vrednost katerega izmed števil",
        default=500,
    )

    maksimalni_prafaktor = models.PositiveSmallIntegerField(
        "maksimalni prafaktor",
        help_text="Zgornja meja za prafaktorje števil",
        default=11,
    )

    class Meta:
        verbose_name = "največji skupni delitelj in najmanjši skupni večkratnik"

    def generate(self):
        stevilo1 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        stevilo2 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        if not (
            max(*sympy.factorint(stevilo1).keys(), *sympy.factorint(stevilo2).keys())
            <= self.maksimalni_prafaktor
            and stevilo1 != stevilo2
        ):
            raise GeneratedDataIncorrect
        najvecji_delitelj = sympy.gcd(stevilo1, stevilo2)
        najmanjsi_veckratnik = sympy.lcm(stevilo1, stevilo2)

        return {
            "stevilo1": stevilo1,
            "stevilo2": stevilo2,
            "najvecji_delitelj": najvecji_delitelj,
            "najmanjsi_veckratnik": najmanjsi_veckratnik,
        }


class EvklidovAlgoritem(Problem):
    """Problem za izračun največjega skupnega delitelja dveh števil z evklidovim algoritmom."""

    class Meta:
        verbose_name = "evklidov algoritem"

    def generate(self):
        stevilo_malo = random.randint(50, 199)
        stevilo_veliko = random.randint(200, 1000)
        if not (
            stevilo_veliko % stevilo_malo != 0
            and stevilo_malo % (stevilo_veliko % stevilo_malo) != 0
        ):  # Da se ne konča že v prvih dveh korakih
            raise GeneratedDataIncorrect
        najvecji_delitelj = sympy.gcd(stevilo_malo, stevilo_veliko)
        return {
            "stevilo1": stevilo_malo,
            "stevilo2": stevilo_veliko,
            "najvecji_delitelj": najvecji_delitelj,
        }
