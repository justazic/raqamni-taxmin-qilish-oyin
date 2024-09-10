import random

pastki_chegara = int(input("Pastki chegarani kiriting: "))
yuqori_chegara = int(input("Yuqori chegarani kiriting: "))

tasodifiy_son = random.randint(pastki_chegara, yuqori_chegara)
harakatlar_soni = 0

print(f"Tasodifiy son tanlandi! {pastki_chegara} va {yuqori_chegara} orasidagi sonni toping!")

while True:
    harakatlar_soni += 1
    taxmin = int(input("Sizning taxminingiz: "))

    if taxmin > tasodifiy_son:
        print("Qayta urinib koring! Siz juda yuqori taxmin qildingiz.")

    elif taxmin < tasodifiy_son:
        print("Qayta urinib koring! Siz juda kichik taxmin qildingiz.")

    else:
        print(f"Tabriklaymiz! Siz {harakatlar_soni} urinishda sonni taxmin qila oldingiz!")
        break