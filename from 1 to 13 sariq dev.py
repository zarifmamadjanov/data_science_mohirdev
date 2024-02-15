#lesson 5

"""print(22%4)
print('yuzasi ', 125**2, ' ga teng')
print('perimetri esa ', 125 * 4, ' ga teng')
print('dumaloq yuzasi', 3.14*(12/2)**2,'ga teng')
print('katetus raven', (6**2 + 7**2)**(1/2))"""

"""ism="Abdulloh"
print(ism)
ism="Zarif"
print(ism)"""

"""greeting="Hello World!"
print(greeting)"""

"""adius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)"""

"""ism = "Zarif"
shahar = "Qo'qon"
Viloyat = "Farg'ona"
kimdir='tovuq'
print("Mening ismim "  + shahar)"""

"""ism = "zarif"
sharif = "mamadjanov"
ism_sharif = f"{ism} {sharif}"
ism_sharif=ism_sharif.upper()
print(ism_sharif.capitalize())"""

"""ism=input("your name man : ")
print("Assalomu aleykum, " + ism.title() +  "!")"""

"""kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
print(kocha, "kochasi, ", mahalla, "mahallasi, ", tuman, "tumani, ", viloyat, "viloyati")
"""
"""kocha=input("kocha " )
mahalla=input("mahalla ")
tuman=input("tuman ") 
viloyat=input("viloyat ")
print(kocha, "kochasi, ", "\n", mahalla, "mahallasi, ","\n", tuman, "tumani, ","\n", viloyat, "viloyati")"""


"""kocha=input("kocha " )
mahalla=input("mahalla ")
tuman=input("tuman ") 
viloyat=input("viloyat ")
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil.upper())"""


#### Lesson 6
"""radius = 20
PI = 3.14159
diametr= 2 * radius
print("Uzunlidi de aylana is ", diametr*PI)"""

"""t_yil = int(input("tell me your birthday year: "))
yosh = 2024 - t_yil
print("Hey man your age is ", yosh)
print(str(yosh))"""
#practice
"""a=int(input("give me the number: "))
print("Then the square of your number is ", a**2)
print("The cube is ", a**3);"""

"""b=int(input("your age man ? "))
print("Yo nigga your year is ", 2024-b)"""

"""a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}x{b}=", a*b)
print(f"{a}/{b}=", a/b)"""

#lesson 7

"""mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narhlar = [12000, 10000, 10900, 22000, 25000, 36000, -25, 63.2]
sonlar = ['bir', 'ikki', 3, 4, 5]
ismlar = []
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)
print("Man " + mahsulot + " sotib oldim")
print("Olinmaganlar bular: ", bozorlik)"""

# lesson 8

""""cars=['bmw', 'mercedez benz', 'volvo', 'general motors', 'tesla','audi']
toys = ('bus','car','bear','dino','snake','lizard')
markaziy_osiyo=['Ozbekiston', 'Tojikiston','Qirgiziston','Turkmaniston','Qozoqston']
len(markaziy_osiyo)"""

#lesson 9

"""mehmonlar=['Ali','Vali','Hasan','Husan','Olim']
for mehmon in mehmonlar:
    print('Salom', mehmon)   
    
mehmonlar=['Ali','Vali','Hasan','Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 2 mart kuni nahorga oshga taklif etamiz")
    print("Hurmat bilan, Pelvonchieyvlar oilasi \n")
    
sonlar=list(range(1,11))
for son in sonlar:
        print(f"{son} ning kvadrati {son**2} ga teng \n")

sonlar=list(range(11))
sonlar_kvadrati=[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar, sonlar_kvadrati)

dostlar=[]
print("5 ta eng yaqin do'stingiz kim ? ")
for n in range(5):
    dostlar.append(input(f"{n+1} - dostingizning ismini kiriting - "))
print(dostlar)"""
#practice
"""ismlar=['qw','we','er','rt','ty']
for i in ismlar:
    print(f"what's up nigga {i}")
print(f"nigganul {len(ismlar)} raz")

toqlar=list(range(11,100,2))
for i in toqlar:
    print(f"{i} ning kubi {i**3} ga teng \n")
    
kinolar=[]
for i in range(5):
    kinolar.append(input("Sevimli kinoyingiznima ? \n"))
print(kinolar)

odamlar=[]
a=int(input("Nechtasi bilan strelka boldi bugun ? \n"))
for n in range (a):
    odamlar.append(input(f"{n+1} chisini isma nima ? \n"))
print(odamlar)"""

#lesson 10

"""avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar :
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())
        
ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")
    
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')
    
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2024-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2024-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")"""
#practice
"""cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for auto in cars:
    if auto != 'gm':
        print(auto.title())
    else:
        print(auto.upper())
        
login = input("Ismin nima bolakay ? \n")
if login.lower() == "admin":
    print("Xush kelibsiz Admin janoblari")
else:
    print("Xush kordik,", login)

a=float(input("son etin bacham "))

if a>0:
    print(a**(1/2))
else:
 print('ne kipeshuy prosto napishi musbat son ')"""
 
 #lesson 11
 
"""yosh=int(input("tell me the truth: "))
if yosh<=4:
    print("you are free of charge ")
elif yosh<=12:
    print("Pay Pal 5000 so'm ")
elif yosh<=18:
    print("8000 so'm, man ")
else:
    print("10000 so'm ")
    
yosh=int(input("tell me the truth: "))
if yosh<=4:
    narh=0
elif yosh<=12:
    narh=5000
elif yosh<=18:
    narh=8000
else:
    narh=10000
print(f"you pay {narh} som for entrance")

kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')
    
narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True #it is possible to put 1
salat = False #it is possible to put 0 
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")

menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunday ovqat yo\'q')
    
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")"""
#practice
"""a=int(input("give the juft number: "))
if a%2==0:
    print("Rhamt! ")
else:
    print("Tell me the juuft, man")

yosh=int(input("tell me the truth: "))
if yosh<=4 or yosh>=60:
    narh=0
elif yosh<=18:
    narh=10000
elif yosh>=18:
    narh=20000
print(f"you pay {narh} som for entrance")

a = float(input("first number : "))
b = float(input("second number: "))
if a>b:
    print(f"{a}>{b} ")
elif a<b:
    print(f"{a}<{b}")
else:
    print(f"{a}={b}")
    
mahsulot=['gosh','tovuq','sut','tuxum','yog','un','sabzavotlar','mevalar','shakar','tuz']
savat=[]
for i in range (5):
    savat.append(input(f"Savatga {i+1} chi mahsulotni kiriting: "))
print(savat)
for element in savat:
    if element in mahsulot:
        print(f"{element} dokonimizda bor ")
    else:
        print(f"{element} dokonimizda yoq")
        
mahsulotlar=['gosh','tovuq','sut','tuxum','yog','un','sabzavotlar','mevalar','shakar','tuz']
bor_mahsulotlar=[]
mavjud_emas=[]   
savat=[]     
for i in range (5):
    savat.append(input(f"Savatga {i+1} chi mahsulotni kiriting: "))
print("Siz soragan mahsulotlar toplami: ", savat)
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("dokonda quyidagi mahsulotlar mavjud emas: ")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz soraga hammasidan bor")
    
foydalanuvchilar=['qwerty','aegle','shift','bird','po']

login=input("ENter new login: ")
if login.lower() in foydalanuvchilar:
    print("Login is busy, try another one")
else:
    print("Welcome, ",login)
    
yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")"""



    



    
    
        











