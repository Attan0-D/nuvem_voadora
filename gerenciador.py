from localidade import SSA, FEN, MIA, BER, SYD, DXB
from voo import vooDec
from reserva import Reserva
from agencia import Agencia


class Gerenciador:
    _instancia = None


    #utilização do singleton para instancias únicas
    @staticmethod
    def get_instance():
        if Gerenciador._instancia is None:
            Gerenciador._instancia = Gerenciador()
            return Gerenciador._instancia

    def __init__(self):
        self.ag = Agencia("Azul")

        voo1 = vooDec(SSA(), BER())

        voo2 = vooDec(SSA(), BER(), FEN())

        voo3 = vooDec(MIA(), SYD())

        voo4 = vooDec(MIA(), SYD(), BER(), DXB())

        self.voos_disponiveis = [voo1, voo2, voo3, voo4]


    def reservar(self, voo, classe):
        for index in self.voos_disponiveis:
            if index == self.voos_disponiveis[voo-1]:
                res = Reserva(index.origem, index.destino, classe, *index.escalas)
                self.ag.realizar_reserva(res)
                return res.num_reserva

    def obter_dados_reserva(self, num_reserva):
        return self.ag.buscar_reserva(num_reserva)




