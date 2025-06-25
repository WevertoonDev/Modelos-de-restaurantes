from modelos.restaurante import Restaurante 

Restaurante_praca = Restaurante('praça', 'Gourmet')
Restaurante_praca.receber_avaliacao('Gui', 10)
Restaurante_praca.receber_avaliacao('Lais', 8)
Restaurante_praca.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()