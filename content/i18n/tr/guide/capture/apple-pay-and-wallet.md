---
title: Apple Pay ve Wallet ödemeleri
summary: Kart ödemelerini gerçekleştikleri anda ekleyin.
order: 40
---

# Apple Pay ve Wallet ödemeleri

Apple Pay ile ödediğinizde veya kartınızı temassız okuttuğunuzda Wallet ödemeyi hemen bilir. Bir Wallet İşlemi otomasyonu her ödemeyi gerçekleştiği anda Damla’ya gönderir; böylece ödeme sizin için kaydedilir.

## Ne zaman kullanılır

- Kartlarınız Apple Wallet’a ekli ve Damla’nın yaptığınız her ödemeyi o anda kaydetmesini istiyorsunuz.
- Bankanızın ödemeyle ilgili mesajı geç geliyor ya da hiç gelmiyor ve ödemenin yine de kaydedilmesini istiyorsunuz.
- Satıcının, Wallet’ın bildirdiği şekliyle kaydedilmesini istiyorsunuz.

## Hangi eylemler kullanılır

Her ikisi de Shortcuts uygulamasındaki Damla eylemleridir ve aynı işi yapar:

- **Damla’ya ekle** — Metin alanı ödemeyle ilgili tek satırlık bir cümleye, Kaynak alanı ise Wallet ödemesi’ne ayarlanır.
- **Damla’ya kart ödemesi ekle** — satıcıyı, tutarı ve kartı doğrudan Wallet işleminden alır.

Tutar para birimiyle birlikte gelir; bu yüzden ayrı bir para birimi alanı yoktur ve hiçbir dönüşüm tahmin edilmez.

## Adım adım

Apple Wallet’a eklediğiniz her kart için bir otomasyon kurulur.

1. Damla’yı açın, sonra Ayarlar’a, sonra Banka mesajları ve ekstreler’e, sonra Otomasyonlar (Shortcuts)’a gidin.
2. “Apple Pay ödemeleri” bölümünün altına kartınızın son 4 hanesini yazın ve Ekle’ye dokunun.
3. Kart için tam adımları görmek üzere listede kartın kaydına dokunun. Adımları kopyalayabilir veya Shortcuts uygulamasının Apple Intelligence’ına yapıştırmak için bir istem kopyalayabilirsiniz.
4. Shortcuts’ı açın, Otomasyon’a, sonra artı düğmesine dokunun, sonra Wallet Transaction’ı seçin ve kartı belirleyin.
5. Hemen Çalıştır’ı seçin, sonra İleri’ye dokunun.
6. New Blank Automation’ı seçin, Add Action’a dokunun, **Damla’ya ekle** araması yapın ve onu seçin.
7. Metin alanını adımların gösterdiği cümleye ayarlayın: *[Amount] tutarında satın alma, kart (haneleriniz) ile, [Merchant] yerinde.* Damla kartınızın hanelerini bu cümleye zaten yazmıştır; yalnızca **Amount** ve **Merchant** köşeli parantez içinde kalır.
8. Metin alanına dokunun ve köşeli parantezlerin yerine Wallet işleminden Amount ve Merchant değerlerini ekleyin.
9. Kaynak’ı Wallet ödemesi olarak ayarlayın.
10. Done’a dokunun.

> **İpucu:** Cümle kartı, tıpkı bir banka kısa mesajı gibi, haneleriyle adlandırır. Haneler, kartın hesap ayrıntılarında kaydettiğiniz son hanelerle eşleşirse Damla ödemeyi hemen o kartın altına işler.

İsterseniz Damla’ya ekle yerine **Damla’ya kart ödemesi ekle** eylemini kullanın. Üç alanı — Satıcı, Tutar ve Kart — değerlerini Wallet işleminden alır.

## Her ödemeye ne olur

- Damla’nın tanıdığı bir karttaki ödeme hemen işlem olarak eklenir.
- Tanınmayan bir karttaki ödeme veya Damla’nın okuyamadığı her şey tek bir dokunuş için Gelen kutusunda bekler.
- Aynı ödeme Damla’ya bir banka kısa mesajından da ulaşırsa yalnızca bir kez kaydedilir. Satıcı adı eşleşen ikinci bir bildirime **Zaten Damla’da** yanıtı verilir. Satıcı farklı adlandırılmışsa ve ikinci bildirim ilkinden sonraki 15 dakika içinde gelirse, bu bildirim olası bir yinelenen kayıt olarak Gelen kutusunda sizin atmanız için bekler.

> **Not:** Telefon kilitliyken kayıtlar okunamaz; bu yüzden Damla ödemeyi saklar ve uygulamanın kilidini bir sonraki açışınızda ekler.

## Bilmekte fayda var

- **Kurulumdan sonra bir deneme ödemesi gönderin.** Otomasyonlar ekranı son mesajın Damla’ya ne zaman ulaştığını gösterir; **Son bildirimler** ise her birini, yapılan işlemle birlikte listeler. Ulaşmadıysa otomasyon büyük olasılıkla Hemen Çalıştır olarak ayarlanmamıştır.
- **Haneler önemlidir.** Son hanelerini hesap ayrıntılarında kaydettiğiniz bir kart otomatik olarak eşleşir. Damla’nın tanımadığı bir kart, hangisi olduğunu ona söylemenizi bekler; bunu kart başına bir kez yaparsınız.
- **Damla salt okunur durumdaysa** — deneme veya abonelik sona erdiği için — eylem bunu söyler ve yeniden abone olana kadar hiçbir şey eklenmez.

## İlgili

- [Banka kısa mesajları ve e-postalar](/guide/capture/bank-texts-and-emails/)
- [Otomatik yakalama nasıl çalışır](/guide/capture/how-automatic-capture-works/)
- [Gelen kutusu](/guide/recording/the-inbox/)
- [Kredi kartları](/guide/accounts/credit-cards/)
