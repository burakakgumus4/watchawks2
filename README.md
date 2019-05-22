# watchawks2
Projenin Adı: Aktif Güvenlik Radar Sistemi 
Projenin Amacı: İşyeri,müze ve fabrika gibi yerlerde güvenliğin aktif bir şekilde sağlanması.
Projede kullanılan malzemeler:
 1.Raspberry Pi 3
 2.Breadboard
 3.Jumper Kablo
 4.1 adet 1K, 1 Adet 2K direnç
 5.Buzzer 
 6.MG90 Servo Motor
 7.HC-SR04 Ultrasonik Mesafe Sensörü
 
Projede kullanılan yazılım dili: Python 2

Projenin çalışma mantığı:
  Raspberry Pi kartımızdan HC-SR04 sensörümüze sinyal gitmekte, echo ucundan nesneye çarpıp sinyalimiz geri gelmektedir. Gelen sinyalim  gerilimi Raspberry Pi kartımıza zarar vermemesi için gerilim bölücü devre ile azaltılmaktadır.Bunun sonucunda sinyal analiz edilip mesafe algılanmaktadır.180 derecelik tarama için servo motora bağlı olan ultrasonik sensör her derece için 1 mesafe algılamakta ve bunu ekranda arayüz yardımı ile şeritler halinde göstermektedir.Mesafe sensörümüz sürekli yaptığı taramalar arasında aynı açıda farklı mesafeler okursa bu durumda cismin hareket ettiği anlaşılacak ve sistem bunu kullanıcıya alarm yardımı ile bildirecektir.  
 


















Projeye ait video linki https://www.youtube.com/watch?v=-jG5fUuodjQ&feature=share&fbclid=IwAR2W3YC2kVLemrlVaNFFNwwved6L3XdHN8AgNBZrDgLQ1nVdK-czSgoD-Ec



