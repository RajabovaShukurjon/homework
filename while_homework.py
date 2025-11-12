
# while True:
#     rang = input("Svetafor qaysi rangda? ").lower()
#     if rang in ['yashil','sariq','qizil']:
#         print("Raxmat, to'g'ri keladi")
#         break
#     else:
#         print("Bu xato rang")
#






# import random
# tasodifiy_son = random.randint(1,10)
# while True:
#     taxmin = int(input("1 dan 10 gacha bo‘lgan sonni toping: "))
#     if taxmin < tasodifiy_son:
#         print("Noto‘g‘ri, son kattaroq! ")
#     elif taxmin > tasodifiy_son:
#         print("Noto‘g‘ri, son kichikroq! ")
#     else:
#         print("Tabriklaymiz , siz topdingiz!")
#         break





# dostlar = []
#
# while True:
#     ism = input("Do‘stingiz ismini kiriting (yoki 'stop' deb yozing): ").title()
#     if ism.lower() == "stop":
#         break
#     dostlar.append(ism)
#
# print("Do‘stlaringiz ro‘yxati:")
# for d in dostlar:
#     print(d)





usd_kurs = 11900
while True:
    summa = input("Summani kiriting (yoki 'exit' deb yozing): ")
    if summa.lower() == "exit":
        print("Dastur yakunlandi ")
        break
    else:
        sum = int(summa)
        usd = sum / usd_kurs
        print(f"{sum} so‘m = {usd:.2f} USD")

