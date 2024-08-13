"""
**Har qanday suniy idrokdan foydalanilgan kodlar uchun imtihon bahosi 0 ga aylantiriladi.**

**Bir biridan kochirilgan holatlardan har bir oquvchi uchun 0 qoyiladi.**

Baholash mezoni:

Baholar har bir funksiya qanchalik toza yozilganligi va aniq ishlayotganiga qarab baholanadi.

Va undan tashqari quyidagi texnalogiyalarni ishlatish ham kerak: 

- thread
- generator
- context managers
- decimal for money
- logging
- decorators
- va boshqalar

**QISMLAR BOYICHA BAHOLASH MEZONI:**

- SUPERADMIN → 20
- ADMIN → 30
- TEACHER → 20
- STUDENT → 20
- TEPADAGI TEXNALOGIYALAR UCHUN → 10

Najot Talimga oxshash bir oquv markaz uchun sistema yaratishingiz kerak. Unda quyidagi imkoniyatlar bolishi kerak.

- 4 xil turdagi foydalanuvchilar
    1. SuperAdmin
    2. Admin
    3. Teacher
    4. Student

SUPERADMIN

Ushbu turdagi foydalanuvchi saytda oldindan mavjud boladi va u admin turdagi foydalanuvchilarni yaratishi mumkin boladi. Buning uchun full_name, username, password

ishlatadi. Va u bergan akaunt orqali admin login qila olishi kerak.

Undan tashqari unda hamma adminlarni korish, ochirish, ozgartirish imkoniyatlari 

ham bolishi kerak.

Undan tashqari oqituvchi yaratish, ochirish, ozgartirish imkoniyati ham bolishi kerak

Quyidagi parametrlar boyicha email habar yuborish.

- hamma uchun
- qizlar
- yigitlar

ADMIN

- Guruh yaratish | name, teacher(tanlashi kerak), max_student, start_time, end_time, status
    
    Guruhlarni korish, ochirish imkoniyati ham bolishi kerak
    
- Yangi student yaratish | full_name, gmail, nomer, gender, age,  login(automatic berilishi kerak), password(automatic berilishi kerak)
    
    studentlarni korish, ochirish imkoniyati ham bolishi kerak
    
- Studentni guruhga qoshish | select student, select group
- Student ismi yoki login boyicha qidirish imkoniyati
- Tolov qabul qilish | select student, amount → siz oddiy qilib studentni akauntiga pul miqdorini qoshib qoysangiz boldi

TEACHER

- Hamma guruhlarini royxatini  korish
- Guruh boyicha studentlarini royxatini korish
- Darsni boshlash | select group
    
    Guruhni tanlagandan keyin yangi menyu ochiladi va unda darsni tugatish va ortga boladi
    

STUDENT

- hamma guruhlarini korish
- balansidagi miqdorni korish
- shaxsiy malumotlarini ozgartira olish imkoniyati
"""