print("Podaj dzień masz do wyboru: poniedziałek, wtorek, środa, czwartek, piątek, sobota, niedziela")
today=input()
if today == "sobota":
    print("impreza!!!")
elif today == "niedziela":
    condition = input()
    if condition=='ból głowy':
        print('rekonwalescencja, potem odpoczynek')
    else:
        print('odpoczynek')
else:
    print("praca, praca, praca")