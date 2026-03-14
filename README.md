*python ve r dosyaları scripts alt klasörünün içindedir.

-mail taslağı-

Konu: Barcode77 Veri Seti - İlk Aşama Analiz ve Kalite Kontrol Raporu

Sayın Profesör Kılıç,

Barcode77 örneğine ait uzun okuma (Long-read) verilerinin analizini tamamladım. Analiz sürecinde verilerin yinelenebilirliğini sağlamak amacıyla Snakemake tabanlı bir biyoinformatik boru hattı (pipeline) kurguladım ve hem Python hem de istatistiksel doğrulama için R dillerini kullandım.

Analiz sonuçlarına dair değerlendirmelerim şöyledir:

1- Okuma Uzunlukları
Toplam 81,011 okuma için ortalama uzunluğu 1038.24 bp olarak hesapladım. Okuma uzunluğu dağılım grafiğine baktığımızda, uzun okuma verilerinde görmeye alışık olduğumuz asimetrik (sağa çarpık) bir dağılım söz konusu. Bu durum, dizileme öncesi kütüphane hazırlığının sağlıklı geçtiğine işaret ediyor.

2- Baz Doğruluğu ve Kalite
Ortalama kalite skorunu (phred) 17.90 olarak tespit ettim. Bu değer, baz çağrım doğruluğunun yaklaşık %98.38 seviyesinde olduğu anlamına gelmektedir. Verilerin genel baz doğruluğu, ileri aşama analizler için oldukça güven verici bir seviyededir.

3- GC İçeriği ve Örnek Temizliği
Veri setinin genel GC içeriği %53.00 civarında ve oldukça dar bir aralıkta seyretmektedir. GC dağılımında anormal bir sapma veya çift tepe (bimodalite) gözlemlemedim, bu da örneğimizde belirgin bir kontaminasyon riskinin düşük olduğunu gösteriyor.

Sonuç ve Öneri:
Elde ettiğim bu kalite metrikleri ışığında, verinin bir sonraki aşama olan Hizalama (Alignment) adımı için uygun olduğunu düşünüyorum. 
Analiz kodlarıma ve grafiklerin detaylarına ekteki GitHub repomdan ulaşabilirsiniz.

Saygılarımla,

Büşra Kozan
