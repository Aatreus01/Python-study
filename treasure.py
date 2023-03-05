print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
sec1 = input("Önünde 2 yol var, ne tarafa gideceksin? (Sağ veya sol yaz)\n").lower()
if sec1 == "sol":
  sec2 = input("Bir göle denk gelene kadar yürüdün. Yüz veya bekle. Seçim senin (Yüz veya bekle yaz)\n").lower()
  if sec2 == "bekle":
    sec3 = input("Biraz bekledin ve gölden 3 kapısı olan bir ev yükseldi. Mavi, kırmızı veya sarı kapı. Seçim senin.\n").lower()
    if sec3 == "sarı":
      print("Tebrikler! Hazineyi buldun la helal valla")
    elif sec3 == "mavi":
      print("Mavi kapıdan içeri girdiğin anda büyük bir canavar üzerine çullanıyor. Kebap oldun")
    elif sec3 == "kırmızı":
      print("Kapıyı açtığın anda içerden alevler dışarıya doğru saçılıyor. Tüm ada yanıp kül oluyor, dolayısıyla sen de")
    else:
      print("Kalp krizi geçirip ölüyorsun. Doğru seçeneği yazamamaktan olsa gerek.")
  else:
    print("Gölden kocaman bir balık atlayıp seni tek lokmada midesine indiriyor")
else:
  print("Ayağın kaydı ve kafana daşa vurup öldün. Zaa mal")
