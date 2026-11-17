import random
MATNLAR = [
 "Texnologiya hayotimizning ajralmas qismiga aylandi va har kuni yangi imkoniyatlar eshigini ochmoqda.",
 "Yaxshi o‘qituvchi o‘quvchisiga javobni emas, javob topish yo‘lini ko‘rsatadi.",
 "Tog‘lar orasidan oqib o‘tadigan daryo bahor kelishi bilan yanada toshib, vodiyni sug‘orishga tayyorlanadi.",
 "Kitob o‘qish insonning fikrlash doirasini kengaytiradi va unga dunyoga boshqacha qarashni o‘rgatadi.",
 "Dasturlashni o‘rganishda eng muhimi har kuni oz-ozdan mashq qilish va xatolardan qo‘rqmaslikdir.",
 "Ertalab erta turib, bir piyola issiq choy ichish kunni xotirjam boshlashning eng oddiy yo‘li.",
 "Kompyuter xotirasi qanchalik katta bo‘lmasin, yaxshi yozilgan dastur har doim kam resurs sarflaydi.",
 "Bog‘dagi olma daraxtlari kuzda mo‘l hosil beradi, ammo buning uchun yoz bo‘yi parvarish qilish kerak.",
 "Sabr va mehnat bilan erishilgan natija har doim ko‘proq quvonch va g‘urur bag‘ishlaydi.",
 "Maktab kutubxonasida ko‘plab qiziqarli kitoblar bor, ularni o‘qigan o‘quvchi bilimini boyitadi.",
 "Internet tarmog‘i orqali dunyoning istalgan nuqtasidagi odam bilan bir zumda bog‘lanish mumkin.",
 "Oilaviy kechki ovqat kun davomidagi charchoqni unutib, yaqinlar bilan suhbatlashish uchun yaxshi fursat.",
 "Tabiatni asrash har birimizning burchimiz, chunki kelajak avlodlar ham ozoda havodan nafas olishi kerak.",
 "Klaviaturada ko‘r-ko‘rona yozishni o‘rganish uchun barmoqlarni to‘g‘ri joylashtirish birinchi qadamdir.",
 "Yangi tilni o‘rganish uchun har kuni bir necha yangi so‘z yodlash va ularni gapda qo‘llash foydali.",
 "Shahar ko‘chalarida tong otishi bilan odamlar ishga shoshilib, mashinalar esa uzun saf tortadi.",
 "Ilm olish uchun yoshning ahamiyati yo‘q, qiziqish va intilish bo‘lsa, har kim yangi narsani o‘rganadi.",
 "Dasturchi yozgan kodini boshqalar ham tushunishi uchun uni sodda va tartibli qilib yozishi lozim.",
]
def tasodifiy_matn(n=10):
    return " ".join(random.sample(MATNLAR, min(n, len(MATNLAR))))
