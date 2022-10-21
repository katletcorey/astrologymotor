print("Astrologiya motoruna xoş gəlmisiz.")
day = int(input("Doğum gününüzü daxil edin: "))
month = input("Doğum ayınızı(sözlə) daxil edin: ")
year = int(input("Doğum ilinizi daxil edin: "))
age = 2022-year
residue = year % 12
animal_sign = str("o")
if residue == 0:
    animal_sign = "MEYMUN"
elif residue == 1:
    animal_sign = "XORUZ"
elif residue == 2:
    animal_sign = "İT"
elif residue == 3:
    animal_sign = "QABAN"
elif residue == 4:
    animal_sign = "SİÇAN"
elif residue == 5:
    animal_sign = "ÖKÜZ"
elif residue == 6:
    animal_sign = "PƏLƏNG"
elif residue == 7:
    animal_sign = "DOVŞAN"
elif residue == 8:
    animal_sign = "ƏJDAHA"
elif residue == 9:
    animal_sign = "İLAN"
elif residue == 10:
    animal_sign = "AT"
elif residue == 11:
    animal_sign = "QOYUN"
elif SyntaxError:
    print("Zəhmət olmasa il daxil edin")
if month == 'dekabr':
    astro_sign = 'OXATAN' if (day < 22) else 'OĞLAQ'
elif month == 'yanvar':
    astro_sign = 'OĞLAQ' if (day < 20) else 'DOLÇA'
elif month == 'fevral':
    astro_sign = 'DOLÇA' if (day < 19) else 'BALIQLAR'
elif month == 'mart':
    astro_sign = 'BALIQLAR' if (day < 21) else 'QOÇ'
elif month == 'aprel':
    astro_sign = 'QOÇ' if (day < 20) else 'BUĞA'
elif month == 'may':
    astro_sign = 'BUĞA' if (day < 21) else 'ƏKİZLƏR'
elif month == 'iyun':
    astro_sign = 'ƏKİZLƏR' if (day < 21) else 'XƏRÇƏNG'
elif month == 'iyul':
    astro_sign = 'XƏRÇƏNG' if (day < 23) else 'ŞİR'
elif month == 'avqust':
    astro_sign = 'ŞİR' if (day < 23) else 'QIZ'
elif month == 'sentyabr':
    astro_sign = 'QIZ' if (day < 23) else 'TƏRƏZİ'
elif month == 'oktyabr':
    astro_sign = 'TƏRƏZİ' if (day < 23) else 'ƏQRƏB'
elif month == 'noyabr':
    astro_sign = 'ƏQRƏB' if (day < 22) else 'OXATAN'
print("Sizin bürcünüz :",astro_sign) 
print("Sizin hal hazırda", age, "yaşınız var. Sizin iliniz - "+animal_sign)
#coded by @katletcorey
