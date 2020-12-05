from dataclasses import dataclass


@dataclass
class Localidade:
    def __init__(self, nome, sigla, taxa_aeroporto):
        self.nome = nome
        self.sigla = sigla
        self.taxa_aeroporto = taxa_aeroporto



@dataclass
class SSA(Localidade):
    def __init__(self):
        super().__init__('Salvador', 'SSA', 160.00)


@dataclass
class FEN(Localidade):
    def __init__(self):
        super().__init__('F. Noronha', 'FEN', 180.00)


@dataclass
class MIA(Localidade):
    def __init__(self):
        super().__init__('Miami', 'MIA', 200.00)


@dataclass
class BER(Localidade):
    def __init__(self):
        super().__init__('Berlim', 'BER', 220.00)


@dataclass
class SYD(Localidade):
    def __init__(self):
        super().__init__('Sydney', 'SYD', 240.00)


@dataclass
class DXB(Localidade):
    def __init__(self):
        super().__init__('Dubai', 'DXB', 300.00)

