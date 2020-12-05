from gerenciador import Gerenciador

ger = Gerenciador.get_instance()
global opc

def main():
    opc = -1
    while opc != 3:
        try:
            opc = int(input('Olá. O Que deseja fazer na Agência Nuvem Voadora?\n'
                        '1) Reservar Vôo \n'
                        '2) Ver dados da reserva \n'
                        '3) Sair \n'))
        except ValueError:
            print("Informe apenas um números inteiros.")
        else:
                if opc == 1:
                    fazer_reserva()
                elif opc == 2:
                    visualizar_reserva()
                elif opc == 3:
                    print('Obrigado por utilizar o Sistema Nuvem Voadora! \n Boa Viagem!')
                else:
                    print("Informe um número válido.")

def fazer_reserva():
   try:
            opc_2 = int(input('Escolha o Vôo:\n'
                                             '1. SSA - BER (Direto)\n'
                                             '2. SSA - BER (Escala em FEN)\n'
                                             '3. MIA - SYD (Direro)\n'
                                             '4. MIA - SYD (Escala em BER e DXB)\n'
                                             '5. Voltar \n'))

            while not  1 <= opc_2 <= 5:
                opc_2 = int(input('Opção inválida, escolha um dos voos abaixo, ou volte ao menu'
                                  ' \n\nEscolha o Vôo:\n'
                                  '1. SSA - BER (Direto)\n'
                                  '2. SSA - BER (Escala em FEN)\n'
                                  '3. MIA - SYD (Direro)\n'
                                  '4. MIA - SYD (Escala em BER e DXB)\n'
                                  '5. Voltar \n'))



   except ValueError:
            print("Informe Apenas Números")

   else:

        if opc_2 != 5:
             opc_3 = input('Escolha a classe que deseja viajar: \n '
                                   'X - Classe Executiva \n'
                                   'Outra Tecla - Classe Econômica\n'
                                   'Digite "cancelar" para cancelar a operação.\n')

             if opc_3 != 'cancelar':
                print('Reserva Concluida! \n N° da Reserva: ', ger.reservar(opc_2, opc_3))

             else:
                print('\nReserva Cancelada')

        else:
             print('\nReserva Cancelada!')


def visualizar_reserva():
    try:
        opc3 = int(input('Informe o número da reserva para consulta: '))

    except ValueError:
        print('Valor Inválido')

    else:
        print(ger.obter_dados_reserva(opc3))



main()