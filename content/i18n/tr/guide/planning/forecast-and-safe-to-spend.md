---
title: Tahmin ve güvenli harcama
summary: Damla'nın güvenli harcama tutarını nasıl hesapladığı ve grafiğin nasıl okunacağı.
order: 10
---

# Tahmin ve güvenli harcama

Tahmin, kitaplarınızda zaten olanlardan yola çıkarak bakiyenizi önünüzdeki günler için gün gün gösterir. Güvenli harcama, bakiyenizin gelecek dönem boyunca herhangi bir anda minimumunuzun altına düşmemesi için bugün en fazla harcayabileceğiniz tutardır.

![Tahmin.](damla-forecast.png)

## Ne zaman kullanılır

- Bakiyenizin ne kadar ve ne zaman düştüğünü, seçtiğiniz aralıkta görmek için: 3M, 6M, 1Y, 2Y ya da 5Y.
- Bugün "Paranız kısa kalabilir" derken, bunun hangi günde olacağını bulmak için.
- Bir geliri, bir faturayı ya da bir vade tarihini değiştirdikten sonra, haftaların artık nasıl göründüğünü görmek için.

## Adım adım

1. Tahmin'i Bugün'ün üstündeki turkuaz kartın grafikinden açın.
2. Üstteki seçiciyle bir aralık seçin; grafik bu aralık için bakiyenizi çizer, minimumunuz ise kesikli kırmızı bir çizgidir.
3. Noktayı hareket ettirmek için grafik boyunca dokunun ve sürükleyin. Küçük bir kutu günün tarihini, bakiyesini ve hareketlerini gösterir; altındaki kart bunları toplamlarıyla birlikte Gelen para ve Giden para olarak listeler.
4. Üstteki pankartı okuyun: bakiye minimumunuzun altına düşerse bunun ne zaman olacağını, ya da minimumunuzun üzerinde kaldığını gösterir.
5. Bir değişikliği denemek için sağ üstteki **Ya olursa**'ya dokunun: harcamak, para almak, sürekli bir ödemeyi ya da planı atlamak ya da bir taksit planı eklemek. Güvenli harcamaya ve en düşük noktaya etkisini görürsünüz. Kitaplarınıza hiçbir şey kaydedilmez.

## Sayı nasıl hesaplanır

- Plan, Gelir ve faturalardaki gelirler ve faturalar kendi takvimlerine göre sayılır; kaydettikleriniz ya da attıklarınız tekrar sayılmaz.
- Kart faturaları: kesilmiş bir ekstre gerçek tutarını vade tarihinde kullanır. Henüz kesilmemiş bir ekstre, kartın tipik bir ayını kullanır — son aylarının ortalaması, Ayarlar'daki Beklenen kart harcaması ayarı ya da kartın Ayrıntıları'nda verdiğiniz sayı. Kesilmiş bir ekstrenin gerçek tutarı devralır. Her kartın sayısı, Bu tahminin içinde neler var altındaki Kartlar grubunda listelenir.
- Taksit planları, aşamalı ödemeler, bildirimlerle duyurulan faturalar ve kişilere yapılan geri ödemeler kendi tarihlerinde sayılır.
- Banka hesaplarınızdan günlük harcamalar tahmin edilmez; tamponunuz onları karşılar.
- Güvenli harcama, en az Önden bak ayarının gösterdiği kadar ileriye bakar ve sonraki gelirinizi de bu döneme sayar; böylece maaştan hemen sonra gelen büyük bir ödeme sayıyı düşürür. Sayı, o dönemdeki en düşük bakiye eksi minimumdur.

## Hesaplanmış bir örnek

Hayali bir hane, 9 Kasım. Para birimi AED, minimum bakiye AED 1,000, önden bakış en az 30 gün.

| Neler sayılır | Değer |
|---|---|
| Günlük hesap (banka) | Bugün AED 29,600 |
| Birikimler | AED 40,000, tahminde yok olarak işaretli |
| İnternet, her ayın 12'sinde | AED 350 çıkış |
| Kira, her ayın 16'sında | AED 8,000 çıkış |
| Maaş, her ayın 27'sinde | AED 25,000 giriş |

Bugün gösterir: bugünkü bakiye AED 29,600, en düşük nokta Pzt 16 Kasım'da AED 21,250, güvenli harcama AED 20,250 — en düşük nokta eksi AED 1,000 minimum. Pencere 9 Kasım'dan 9 Aralık'a sürer, Cum 27 Kasım'daki maaşı geçer; maaştan sonra gelenler de sayılır. Birikimler bu sayılarda yoktur.

Gün gün bakiye (beklenen çizgi; temkinli burada aynıdır, çünkü her kalem sabittir):

| Tarih | Bakiye | Neden |
|---|---|---|
| 9–11 Kasım | AED 29,600 | |
| 12 Kasım | AED 29,250 | İnternet 350 |
| 16 Kasım | AED 21,250 | Kira 8,000 (en düşük nokta) |
| 27 Kasım | AED 46,250 | Maaş 25,000 |

Tek seferlik ödeme sınırları (tek ödeme, minimumu koruyarak):

| Ödeme tarihi | En fazla ödeyebileceğiniz | Rahat tutar |
|---|---|---|
| 10 Kasım, 13 Kasım ya da 19 Kasım | AED 20,000 | AED 16,000 |
| 29 Kasım (maaştan sonra) | AED 36,500 | AED 29,500 |

Maaştan önce, ilk satırdaki tutarlara kadar bir ödeme bakiyeyi hiçbir zaman AED 1,000 minimumun altına düşürmez. Maaş gününden sonra sınır daha büyüktür.

## Bilmekte fayda var

> **Note:** Grafik iki çizgi çizer: Beklenen ve Temkinli. Temkinli, sabit olmayan geliri geciktirir ya da keser; güvenli harcama o çizgiyi kullanır. Gidenler asla geciktirilmez ve tahmini bir tutar daha az lehte olan ucunda sayılır. Planınızda hiçbir şey belirsiz olmadığında çizgiler üst üste biner.

> **Limit:** Bir kartın hiçbir tahmini yoksa, grafiğin üstünde bir uyarı belirir ve tahmin fazla iyimserdir: kartın sonraki ekstrelerinden sonraki harcamalarını dışarıda bırakır. Karta Ayrıntıları'nda tipik bir ay verin ya da ekstre aktarın. Ayarlar'da Beklenen kart harcaması kapalıysa, yalnızca kartlarınızda zaten olan sayılır. Hesabı tahminde yer almayan para üstte adlandırılır.

> **Note:** Bilgi ve tahminler, finansal tavsiye değildir.

## İlgili

- [Ya olursa](/guide/planning/what-if/)
- [Tekrarlayan gelir ve faturalar](/guide/planning/income-and-bills/)
- [Damla'ya sorun](/guide/planning/ask-damla/)
- [Damla ile bir gün](/guide/start/a-day-with-damla/)
