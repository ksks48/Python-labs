print("Визначення дня тижня:\n--------------------------------------------")
n = int(input("Введіть ціле число від 1 до 365: "))
if n < 1 or n > 365:
    print("Помилка!")
else:
    smth_good = n % 7
    if smth_good == 1:
        print("Понеділок")
    if smth_good == 2:
        print("Вівторок")
    if smth_good == 3:
        print("Середа")
    if smth_good == 4:
        print("Четвер")
    if smth_good == 5:
        print("П'ятниця")
    if smth_good == 6:
        print("Субота")
    if smth_good == 0:
        print("Неділя")