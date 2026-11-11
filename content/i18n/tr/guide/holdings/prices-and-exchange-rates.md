---
title: Fiyatlar ve döviz kurları
summary: Damla internette neyi sorgular, ne zaman, ve kendi değerinizi nasıl yazarsınız.
order: 40
---

# Fiyatlar ve döviz kurları

Piyasa verileri, Damla'nın kendi kendine yaptığı tek sorgulamadır: kullandığınız para birimleri için döviz kurları ve takip etmeyi seçtiğiniz varlıklar için fiyatlar. İkisi de isteğe bağlıdır ve Damla tamamen çevrimdışı çalışır.

## Ne zaman kullanılır

- Başka bir para biriminde bir hesabınız ya da kartınız var ve dönüştürmeyi yapan kurun güncel kalmasını istiyorsunuz.
- Bir hisseyi ya da fonu takip ediyorsunuz ve her seferinde yazmak yerine fiyatının getirilmesini istiyorsunuz.
- Bir kur ya da fiyat yanlış görünüyor ve bir yenilemenin ne getirdiğini görmek ya da gün için kendi değerinizi yazmak istiyorsunuz.

## Ne gönderilir — fazlası değil

- Kurlar için Damla yalnızca para birimi kodları gönderir.
- Fiyatlar için Damla yalnızca varlıklarınız için ayarladığınız sembolleri gönderir.
- Tutar, ad ya da kişisel veri gönderilmez. Uygulamanın başka yerindeki banka adıyla logo araması yalnızca siz ona dokunduğunda çalışır.

## Ne zaman yenilenir

- Yaklaşık günde bir kez: veriler bir günden eskiyse uygulamayı açtığınızda ve bir gün sonra geri döndüğünüzde yeniden.
- Uygulama kapalıyken arka planda, iOS izin verdiğinde. Bunun olup olmayacağına ve ne zaman olacağına iOS karar verir, bu yüzden güvenilecek olan açılıştaki yenilemedir.
- Ayarlar'da **Şimdi yenile**'ye her dokunuşunuzda; dokunuşlar arasında kısa bir en az bekleme süresi vardır, başarısızlıktan sonra bu bekleme daha uzundur.

Her kaynak kendi başına getirilir: biri başarısız olursa öteki verisini korur.

## Adım adım

### Fiyatları açmak

1. Varlığın sayfasını açın ve sembolünü girin. Sembolleri Ayarlar'da, **Para birimleri ve fiyatlar** altında, **Semboller** bölümünde de ayarlayabilirsiniz.
2. **Varlıklar için fiyat sorgula** seçeneğini açın (aynı Ayarlar sayfasında, **Piyasa verileri** altında). Fiyat sorgulama kapalı başlar.

### Bir yenilemeyi kontrol etmek ya da kendi değerinizi yazmak

1. Ayarlar'ı, sonra **Para birimleri ve fiyatlar**'ı açın.
2. **Şimdi yenile**'ye dokunun. **Ne değişti** başlıklı bir rapor her kaynağı — **Döviz kurları** ve **Fiyatlar** — listeler; her biri **Güncellendi**, **Atlandı** ya da **Başarısız** olarak işaretlenir:
   - **Güncellendi**, öğe başına bir satırla birlikte: yeni kur ya da fiyat ve öncesinde neydi (ya da *yeni*, ya da *değişmedi*).
   - **Atlandı**, gerekçesiyle: fiyat sorgulama kapalı, sembol ayarlanmamış, günlük kur güncellemeleri kapalı, ya da yalnızca ana para biriminizi kullanıyorsunuz.
   - **Başarısız**, hatayla birlikte. Bir servis meşgulse biraz bekleyin ve yeniden deneyin.
3. Raporun sonu, yenilemenin rakamlarınıza ne yaptığını gösterir: net değer ve 90 gündeki en düşük nokta, önce ve sonra.
4. **Döviz kurları** altında, her yabancı para birimi geçerli olan kuru, **Getirildi** mi yoksa **Sizin kurunuz** mu olduğunu tarihıyla birlikte gösterir. Kendi kurunuzu belirlemek için **Kendi kurunuzu belirleyin** altına yazın ve **Kaydet**'e dokunun.

Anahtarların altında Damla, her kaynağın son ne zaman güncellendiğini, yoksa **Hiç güncellenmedi**'yi gösterir; fiyat sorgulama kapalıyken fiyatlar satırında ayrıca **Kapalı** yazar.

## Hangi değer kazanır

- En güncel kur ya da fiyat geçerli olandır.
- Girdiğiniz bir kur ya da fiyat, girdiğiniz gün kazanır. Sıradaki yenileme onun yerine daha yeni getirilmiş olanı koyar. Rapor, kendi değerinizin ne zaman hâlâ kullanımda olduğunu söyler.
- Pence cinsinden yazılan fiyatlar sterline çevrilir.

## Bilmekte fayda var

> **Note:** Başka bir para biriminde yapılan kart alışverişleri, en güncel döviz kuru artı bankanızın uyguladığı yüzde farkıyla tahmin edilir — uygulamadıysanız %2,5 — ve ekstre tutarı kesinleştirene kadar ≈ ile işaretlenir. Farkı Ayarlar'da, **Para birimleri ve fiyatlar** altında, **Başka para biriminde kart alışverişleri** bölümünde ayarlarsınız.

> **Limit:** Otomatik bir yenileme en fazla günde bir kez çalışır. Bunun ötesinde yalnızca **Şimdi yenile**'ye dokunduğunuzda yenileyin. Yenilemeden sonra kur ya da fiyat değişmediyse raporu okuyun: neyin güncellendiğini, atlandığını ya da başarısız olduğunu ve bugün yazdığınız bir değerin hâlâ kullanılıyor mu olduğunu söyler.

> **Note:** Kurlar exchangerate-api.com'dan gelir. Fiyatlar herkese açık bir borsa servisinden gelir.

> **Note:** Damla, kendi defterlerinizden bilgi ve tahmin verir. Yatırım ya da finansal tavsiye vermez.

## İlgili

- [Yatırımlar ve varlıklar](/guide/holdings/investments/)
- [Kredi kartları](/guide/accounts/credit-cards/)
- [Gizlilik ve verileriniz](/guide/data/privacy-and-your-data/)
- [Sorun giderme](/guide/help/troubleshooting/)
