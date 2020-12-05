class Agencia:
    def __init__(self, nome):
        self.nome = nome
        self._nome = []

    def realizar_reserva(self, reserva):
        self._nome.append(reserva)

    def buscar_reserva(self, number):
        for reserva in self._nome:
            if number == reserva.num_reserva:
                return reserva.get_info_reserva()

        return 'Reserva Não Encontrada.'

