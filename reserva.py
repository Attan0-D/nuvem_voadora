from random import randint
from voo import vooDec


class Reserva(vooDec):

    num_reserva = []

    def __init__(self, origem, destino, classe, *escalas):
        super().__init__(origem, destino, *escalas)
        self.classe = classe
        self.num_reserva = randint(1, 10000)

        if not self._identificacao in Reserva.num_voo:
            Reserva.num_voo.append(self._identificacao)
        else:
            self._identificacao = randint(1, 10000)

    def get_preco_final(self):
        if self.classe == "X":
            return super().get_taxa() + 200
        return super().get_taxa()

    def get_info_reserva(self):

        return super().get_info_voo() + '| Classe: {} | Preço Final: {} \n' \
            .format("Executiva" if self.classe == "X" else "Econômica",
                    self.get_preco_final())

