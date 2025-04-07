class Avaliacao:
   def __init__(self,cliente, nota):
       self._cliente = cliente
       self._nota = nota
       
    
@property
def media_avaliacao(self):
        if not self.avaliacao:
            return 0
        soma_das_notas=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media