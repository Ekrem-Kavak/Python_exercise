# SORU - 1: 1500 ile 2700 arasında 7'ye bölünebilen ve 5'in katları olan sayıları bulan bir Python programı yazınız.

numbers = []

for x in range(1500,2701):
    if (x % 7 == 0) and (x % 5 == 0):
        numbers.append(str(x))           
print(",".join(numbers))       

# SORU - 2: 1 ile 9 arasında bir sayı tahmin eden Python programını yazınız.    

import random 
target_number = random.randint(1,10) 

number = int(input("Bir sayı giriniz: "))

while True:
    if (number == target_number):
        print("İyi tahmin")
        break
    elif (number != target_number):
        print("Başka tahminde bulununuz.")
        number = int(input("Bir sayı giriniz: "))
        
# SORU - 3: Python kodu ile sağa bakan üçgen çizginiz.      

n = 5
for i in range(n):
    for j in range(i):
        print("*", end = "")
    print("")

for i in range(n,0,-1):
    for j in range(i):
        print("*", end = "")
    print("")
        

# SORU - 4: Kullanıcıdan bir kelime alan ve o kelimeyi ters çeviren kodu yazınız. 

# 1. yol
word = input("Bir kelime giriniz: ")

for char in range(len(word) - 1, -1, -1):
      print(word[char], end= "")
print("\n")


# SORU - 5: Kullanıcıdan alınan sayı dizisindeki tek ve çift sayıları sayan programı yazınız.

numbers = (1,2,3,4,5,6,7,8,9)
even_numb = 0 # çift
odd_numb = 0 # tek

for x in numbers:
    if (x % 2 == 0):
        even_numb += 1
    elif (x % 2 == 1):
        odd_numb += 1

print("Dizideki tek sayılar:", odd_numb)
print("Dizideki çift sayılar:", even_numb)

