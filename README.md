🚀 #Ev Satın Almak İsteyenler İçin Hızlı Çözüm
Bilgisayarlarımızın veri kazıma ve veritabanı işlemleriyle heyecan verici bir yolculuğa çıkmasını sağlayacak kodları inceleyelim.

📂 **Dosya Yapısı**
Projemiz, iki ana Python dosyasından oluşuyor: `pub.py` ve `home_scraping.py`. Şimdi bu dosyaların içeriğine yakından bakalım!

### pub.py
Dosya, 🧹 `publisher` fonksiyonunu içeriyor. Bu fonksiyon, verilerimizi temizlemek ve düzenlemek için harikalar yaratıyor!

🔮 `publisher(titlename)`:
- Açıklama: Verilen metindeki özel karakterleri temizler ve uygun bir şekilde düzenler.
- Kullanım: `titlename` argümanı, temizlenmek istenen metni içerir.
- Dönüş Değeri: Temizlenmiş metni döndürür.

### home_scraping.py
Bu dosya, 🌐 web sitesinden veri kazıma işlemlerini gerçekleştiriyor ve verileri 🗄️ SQL veritabanına kaydediyor.

🚀 `Main` Sınıfı:
- Açıklama: Web sitesinden veri kazıma işlemlerini yöneten ana sınıf.
- İnit (Yapıcı) Metodu: URL'yi alır ve gerekli değişkenleri başlatır.
- 🕵️‍♀️ `find` Metodu: İlanların URL'lerini çeker ve `self.links` listesine ekler.
- 💾 `save` Metodu: İlanlardaki verileri çeker, temizler, SQL tablosuna ekler ve kaydeder.

Projeyi çalıştırmak için, `Main` sınıfı örneği oluşturuyor, ilan URL'lerini buluyor ve verileri kaydediyoruz.

💡 **Önemli Notlar**
- Bu kodlar, web sitesinin yapısına ve verilerin yerleştirilme biçimine dayanıyor. 🏗️ Web sitesi yapısında değişiklik olduğunda kodları güncellememiz gerekebilir.
- SQL sunucusu bağlantı bilgileri 🤐 gizli bilgilerdir ve güvenliğinizi sağlamak için korunmalıdır. Bu bilgileri güvenli bir şekilde saklamalısınız.
- Kodlar, web sitesini aşırı yüklememeye dikkat ederek belirli bir hızda istek gönderiyor. 🚦

Bu projenin heyecan verici bir şekilde çalışması için web sitesinin yapısına ve ihtiyaçlarınıza uygun olarak kodları özelleştirmeniz gerekebilir. Hazır mısınız? 🚀
