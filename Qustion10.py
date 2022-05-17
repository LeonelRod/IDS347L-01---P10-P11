#pregunta 10

#Variable to got the number to convert "NC= Number to convert "
NC = int (input("Please, put the number you want to convert "))

#Variables that have the numbers we need to convert
Thousands: int = (int(NC/1000))*1000
Hundreds = int((NC - Thousands)/100)*100
Tens = (int(NC - Thousands - Hundreds)/10)*10
Units = int((NC - Thousands - Hundreds - Tens))

#Variable to put the numbers on int, convert to Romans
NRomans = str()

#Validation Thousands section
if Thousands == 3000:
    NRomans += "MMM"
elif Thousands == 2000:
    NRomans += "mm"
elif  Thousands == 1000:
    NRomans += "M"

#Validation Hundreds section
if Hundreds == 100:
    NRomans += 'C'
elif Hundreds == 200:
    NRomans += 'CC'
elif Hundreds == 300:
    NRomans += 'CCC'
elif Hundreds == 400:
    NRomans += 'CD'
elif Hundreds == 500:
    NRomans += 'D'
elif Hundreds == 600:
    NRomans += 'DC'
elif Hundreds == 700:
    NRomans += 'DCC'
elif Hundreds == 800:
    NRomans += 'DCCC'
elif Hundreds == 900:
    NRomans += 'CM'

#Validation Tens section
if Tens == 10:
    NRomans += 'X'
elif Tens == 20:
    NRomans += 'XX'
elif Tens == 30:
    NRomans += 'XXX'
elif Tens == 40:
    NRomans += 'XL'
elif Tens == 50:
    NRomans += 'L'
elif Tens == 60:
    NRomans += 'LX'
elif Tens == 80:
    NRomans += 'LXX'
elif Tens == 90:
    NRomans += 'XC'

#Validation units section
if Units == 1:
    NRomans += 'I'
elif Units == 2:
    NRomans += 'II'
elif Units == 3:
    NRomans += 'III'
elif Units == 4:
    NRomans += 'IV'
elif Units == 5:
    NRomans += 'V'
elif Units == 6:
    NRomans += 'VI'
elif Units == 7:
    NRomans += 'VII'
elif Units == 8:
    NRomans += 'VIII'
elif Units == 9:
    NRomans += 'IX'

#is printed the variable that have the convertion
print (NRomans)