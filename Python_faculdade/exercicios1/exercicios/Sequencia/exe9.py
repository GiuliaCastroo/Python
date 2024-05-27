duracao = int(input("Digite a duração do evento em segundos: "))

horas = duracao // 3600  # Número inteiro de horas
duracao %= 3600          # Atualizando a duração para os segundos restantes
minutos = duracao // 60  # Número inteiro de minutos
segundos = duracao % 60  # Número de segundos restantes

print("A duração do evento foi: ", horas, "horas,", minutos, "minutos e", segundos, "segundos")
