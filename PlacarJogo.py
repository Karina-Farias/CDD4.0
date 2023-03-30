Time1 = input("Time:")
GolsTime1 = input("Gol:")
Time2 = input("Time:")
GolsTime2 = input("Gol:")

if GolsTime1 != GolsTime2:
    if GolsTime1 > GolsTime2:
        print(Time1,"foi o Vencedor com", GolsTime1,"Gols contra o",Time2,"!")
    else:
        print(Time2,"foi o Vencedor com",GolsTime2,"Gols contra o",Time1,"!")
else:
    print("Empate do", Time1,"X",Time2,"!")