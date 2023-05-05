TempoInicio = int(input("Hora do início do jogo: "))
TempoFim = int(input("Hora do fim do jogo: "))
Duracao = TempoFim - TempoInicio

if TempoInicio < TempoFim:
    print("O jogo durou",Duracao,"horas!")
else:
    print("O jogo durou",24 - TempoInicio + TempoFim,"horas!")

