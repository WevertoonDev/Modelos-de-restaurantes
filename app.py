from modelos.restaurante import Restaurante 
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

Restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00,'grande')
prato_paozinho = Prato('Paozinho', 2.00,'O melhor pao da cidade')
Restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
Restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)


def main():
    print (bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
