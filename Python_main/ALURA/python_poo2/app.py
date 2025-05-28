from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida("Suco de Melancia", 5.00 , "Grande")
bebida_suco.aplicar_desconto()
prato_paozinho = Prato ("Pãozinho", 2.00, "O melhor pão da cidade")
prato_paozinho.aplicar_desconto()
sobremesa = Sobremesa("Sorvete de Morango", 12.00, "Massa", "Grande", "Sorvete de Morango com calda")
sobremesa.aplicar_desconto
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa)


def main():
   restaurante_praca.exibir_cardapio
    
    
if __name__ == '__main__':
    main()

    