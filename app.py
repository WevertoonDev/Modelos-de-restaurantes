from modelos.restaurante import Restaurante 

Restaurante_praca = Restaurante('praça', 'Gourmet')
Restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
Restaurante_japones = Restaurante ('Japa', 'japonesa')

Restaurante_mexicano.alternar_estado()
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()