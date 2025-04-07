
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante(nome= "praça", categoria= "Gourmet")
restaurante_mexicano = Restaurante (nome= "Mexican Food" , categoria="Mexicano")
restaurante_japones = Restaurante (nome= "Djapa" , categoria="Japonesa")


restaurante_japones.alternar_estado()
restaurante_praca.receber_avaliacao("Ju",10)
restaurante_praca.receber_avaliacao("Lala",8)
restaurante_praca.receber_avaliacao("123",7)



def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
    

 