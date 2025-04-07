class Musica:
    nome = ''
    artista = ''
    duracao= int 
    

musica1 = Musica()
musica1.artista ='Bohemian Rhapsody'
musica1.nome = 'Queen'
musica1.duracao =355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234


#Represtação de como fazer classes e prenchelas e em python

#Print com fstring
print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')


print(vars(musica1))
print(vars(musica2))
print(vars(musica3))
