import  time
count = input("Какая сумма счета?")
try:
    count = float(count)
except ValueError:
    print("Ошибка: введите числовое значение для суммы счета.")
    exit()
tax = input("сколько вы хотите оставить чаевых 10,15,20").strip().lower()
if tax ==  "10":
        print("вы выбрали оставить 10% от счета")
        print("введеться подчет...")
        time.sleep(3)
        tip = count * 0.10
        print(f"сумма чаявых состовляет: {tip:.2f}")
elif tax == "15":
    print("вы выбрали оставить 15% от счета")
    print("введеться подсчет...")
    time.sleep(4)
    tip = count * 0.15
    print(f"сумма чаявых состовляет: {tip:.2f}")
elif tax == "20":
    print("вы выбралм 20% от счета")
    print("введеться подсчет...")
    time.sleep(5)
    tip = count * 0.20
    print(f"сумма чаявых составила:{tip:.2f}")