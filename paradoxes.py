import random
def Simulate(peoples):
    year={}
    for i in range(1,366):
        year[i]=0
    for i in range(peoples):
        year[random.randint(1,365)]+=1
    return year

def calculate_not_pn(peoples):
    res=1
    for i in range(peoples):
        res*=(1-(i/365))
    return res

while True:

    print(f"Меню:\n"
          f"0 - выход\n"
          f"1 - Смоделировать n эксперементов и посчитать вероятность совпадения дней рождений\n")
    var=int(input())
    if var==0:
        break

    elif var==1:
        peoples = int(input("Введите количество человек в группе"))
        counter=0
        simulate=int(input("Введите количество эксперементов"))
        for i in range(simulate):
            year = Simulate(peoples)
            for j in range(1,len(year)+1):
                if year[j]>1:
                    counter+=1
                    break
        print(f"Теоретическая вероятность совпадения дня рождения(ошибочная): 1/365={1/365}\n"
              f"Смоделированная: {counter/simulate}\n"
              f"Корректный расчет по формуле для парадокса дней рождений:\n"
              f"p(peoples) = 1 - not(p(peoples))\n"
              f"not(p(peoples)) = 1 * (1 - (1/365)) * (1 - (2/365)) * ... * (1 - ({peoples - 1}/365)) = 365!/((365 - peoples)! * 365^{peoples})= {calculate_not_pn(peoples)}\n"
              f"p(peoples) = {1-calculate_not_pn(peoples)}")





