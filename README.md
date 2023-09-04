# Ev Satın Almak İsteyenler İçin Hızlı Çözüm 🚀
Bilgisayarlarımızın veri kazıma ve veritabanı işlemleriyle heyecan verici bir yolculuğa çıkmasını sağlayacak kodları inceleyelim.

## Proje Tanımı

Bu proje, "hepsiemlak.com" web sitesinden İstanbul'daki satılık ev ilanlarını çeken ve bu verileri bir SQL veritabanına kaydeden bir web kazıma (web scraping) uygulamasını içermektedir. Proje, iki Python dosyasından oluşmaktadır: `pub.py` ve `home_scraping.py`.

## Dosya Yapısı

- `pub.py`: Özel karakterleri temizlemek için kullanılan `publisher` fonksiyonunu içerir.
- `home_scraping.py`: Web kazıma işlemlerini gerçekleştirir ve verileri SQL veritabanına kaydeder.

## `pub.py` Dosyası

### `publisher` Fonksiyonu

```python
def publisher(titlename):
    # Verilen metindeki özel karakterleri temizler ve düzenler.
    # Args:
    #   titlename (str): Temizlenmek istenen metin.
    # Returns:
    #   str: Temizlenmiş metin.
```

Bu fonksiyon, verilen metindeki özel karakterleri kaldırmak ve uygun bir şekilde düzenlemek için kullanılır. Bu temizleme işlemi, SQL veritabanı sütun başlıklarını oluştururken yardımcı olur.

## `home_scraping.py` Dosyası

### `Main` Sınıfı

```python
class Main:
    def __init__(self, url):
        # Yapıcı metodu: URL'yi alır ve gerekli değişkenleri başlatır.
    
    def find(self):
        # İlanların URL'lerini çeker ve `self.links` listesine ekler.
    
    def save(self):
        # İlanlardaki verileri çeker, temizler, SQL tablosuna ekler ve kaydeder.
```

Bu sınıf, web sitesinden veri kazıma işlemlerini yönetir. İşte sınıfın başlıca metotları:

- `find()`: İlanların URL'lerini çeker ve `self.links` listesine ekler.
- `save()`: İlanlardaki verileri çeker, temizler, SQL tablosuna ekler ve kaydeder.

## Kullanım Amacı

Bu proje, "hepsiemlak.com" web sitesinden İstanbul'daki satılık ev ilanlarını çekmek ve bu verileri SQL veritabanına kaydetmek amacıyla oluşturulmuştur. Proje, belirli bir web sitesinin veri yapısına bağlıdır ve bu yapının değişmesi durumunda kodları güncellemek gerekebilir.

## Önemli Notlar

- Bu kodlar, web sitesinin yapısına ve verilerin yerleştirilme biçimine dayanmaktadır. Web sitesi yapısında değişiklik olduğunda kodları güncellemek gerekebilir.
- SQL sunucusu bağlantı bilgileri (sunucu adı, veritabanı adı, kullanıcı adı, şifre) gizli bilgilerdir ve güvenliğinizi sağlamak için korunmalıdır. Bu bilgileri güvenli bir şekilde saklamalısınız.
- Kodlar, web sitesini aşırı yüklememeye dikkat ederek belirli bir hızda istek gönderir.

Bu dökümantasyon, projenizi daha iyi anlamanıza yardımcı olmalı ve kodlarınızı ihtiyaçlarınıza göre özelleştirmenize yardımcı olmalıdır. Projenizin başarılı olmasını dileriz!
