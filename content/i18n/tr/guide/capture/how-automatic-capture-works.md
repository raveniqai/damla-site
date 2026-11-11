---
title: Otomatik kayıt nasıl çalışır
summary: Banka metinleri, e-postalar, Wallet ödemeleri ve hesap özetleri; Damla'nın her biriyle ne yaptığı.
order: 10
---

# Otomatik kayıt nasıl çalışır

Otomatik kayıt, bir banka mesajının siz hiçbir şey yazmadan bir işleme dönüşmesinin yoludur. Damla kendisine ulaşan metinleri, e-postaları, Wallet ödemelerini ve hesap özeti dosyalarını okur, her birinin ne olduğunu anlar; sonra ya ekler, ya size sorar, ya da dokunmaz.

## Mesajlar Damla'ya nasıl ulaşır

iOS, uygulamalara mesajlara veya e-postalara erişim vermez; bu yüzden Damla onları kendi kendine asla okumaz. Bir şey Damla'ya yalnızca siz gönderdiğinizde ulaşır, üç yoldan biriyle:

- **Kurduğunuz bir Shortcut**, yeni gelen her metni, e-postayı veya Wallet ödemesini geldiği anda Damla'ya iletir.
- **Paylaş menüsü**: bir mesajı seçip Damla'ya paylaşırsınız.
- **Dosya seçici**: içe aktarmak için hesap özeti dosyalarını seçersiniz.

Her şey telefonda okunur. Hiçbir şey yüklenmez.

## Bir mesaja ne olur

Damla her mesajı aynı kural listesiyle, bu sırayla karşılaştırır ve uyan ilk kuralda durur.

1. **Tek kullanımlık ve onay kodları atılır.** Mesajın sözleri hiç saklanmaz, böylece bir kod sonradan geri okunamaz. Geriye kalan tek şey, günlükte "Tek kullanımlık kod: asla saklanmaz" diyen bir satırdır.
2. **Bir fatura bildirimi fatura olarak hatırlanır.** "Faturanız hazır" bir ödeme değildir: para henüz hareket etmedi. Damla bunu beklenen bir fatura olarak tutar; onu daha sonra ödeyen kart yükü tek gerçek işlemdir.
3. **Reklamlar, limit ve kur bildirimleri, hatırlatmalar ve duyurulan gelecek yüklemeler atlanır.** Bir tutar anılır ama para hareket etmemiştir. Böyle bir mesaj parayla ilgiliyse Damla ilk sözlerini günlüğe yazar; böylece yanlış bir karar verdiyse görürsünüz.
4. **Net bir banka bildirimi hemen eklenir.** Kart veya hesap haneleri hesaplarınızdan biriyle eşleşen bir alışveriş, iade ya da gelir doğrudan işlem olur. Kart ödemeleri, iadeler ve havaleler tanınır. Kategori, o alıcıyı daha önce nasıl sınıflandırdığınıza göre gelir; harcamalar için **Diğer**'e, giren para için **Diğer gelir**'e düşer.
5. **Net olmayan her şey Gelen Kutusu'nda** bir dokunuş için bekler. Bir taahhüt yaratan hiçbir şey — bir fatura, bir kredi, bir taksit planı — onayınız olmadan eklenmez.
6. **Parayla hiç ilgisi olmayan bir mesaj atılır.** Saklanmaz ve günlüğe yazılmaz; böylece özel bir mesaj asla gelen kutusuna ya da günlüğe düşmez.

## Ne olduğunu nereden kontrol edersiniz

- **Son bildirimler** (Ayarlar > Banka mesajları ve hesap özetleri) son 50 bildirimin günlüğüdür, en yenisi önce; her birinde kısa bir gerekçe vardır: Eklendi, Gelen kutusunda bekliyor (ve nedeni), Zaten kayıtlı, Yok sayıldı ya da yaklaşan bir fatura not edildi. Bir banka mesajı geldiği hâlde burada hiçbir şey görünmüyorsa, Shortcut çalışmamıştır.
- **Gelen Kutusu**, Bugün üzerinde **N onayınızı bekliyor** olarak görünür. Bir öğeye dokunup **Cümleyle ekle**'de açın; kontrol etmeniz için orada sizin için yeniden okunur. Kaydettiğinizde Gelen Kutusu'ndan çıkar; **Vazgeç** ise hiçbir şey eklemeden onu çıkarır.
- Damla'nın işlem yaptığı bir bildirim geri alınabilir: Son bildirimler'de satırda sağa kaydırıp **Geri al**'a dokunun. Eklediği işlem silinir ya da not ettiği fatura unutulur.

## Bilmenizde fayda var

- **Aynı bildirim iki kez gelirse bir kez eklenir.** Bankanın metni, e-postası ya da Wallet tarafından yeniden bildirilen bir alışveriş zaten kayıtlı görünür. Aynı tutarın birkaç dakika içindeki ikinci bildirimi, karar vermeniz için Gelen Kutusu'nda bekler.
- **Yeni bir karttan gelen ilk bildirim Gelen Kutusu'nda bekler**, çünkü Damla o kartın son hanelerini henüz bilmez. Bir kez tamamlayın, Damla onları öğrenir.
- **Telefon kilitliyken gelen bir mesaj** bekler ve telefonun kilidini açtıktan sonra uygulamayı bir sonraki açışınızda eklenir. Defterleriniz salt okunursa, tekrar düzenleyebilir hâle gelene kadar o kuyrukta kalır.
- **Bir hesap özeti PDF'i**, Shortcut ile gönderildiyse kuyruğa alınır. Bugün, "Hesap özetleri veya ekran görüntüleri. Siz onaylayana kadar hiçbir şey eklenmez" notuyla **N incelenmeyi bekliyor** gösterir; hiçbir şey eklenmeden önce siz onu incelersiniz.
- **Telefonda Apple Intelligence bulunduğu durumlarda**, model metinden yalnızca alanlar okuyabilir. Döndürdüğü her sayı ve ad metinde geçmek zorundadır, aksi hâlde yok sayılır; okuduğu şey siz görmeden asla kaydedilmez.
- **Okuma ifadeye göredir ve kusursuz değildir.** Ödeme gibi ifade edilmiş bir teklif arada geçebilir; alışılmadık bir ifade ise eklenmek yerine Gelen Kutusu'nda bekleyebilir. Her Shortcut'u bankanızın göndericisine ya da konusuna sınırlayın; böylece alakasız mesajlar asla Damla'ya gönderilmez.

## İlgili

- [Otomasyon kurulum sihirbazı](/guide/capture/setup-wizard/)
- [Gelen kutusu](/guide/recording/the-inbox/)
- [Damla'nın yok saydıkları ve bir bildirimi geri alma](/guide/capture/what-damla-ignores/)
- [Hesap özeti içe aktarma](/guide/capture/importing-statements/)

![Ayarlar > Banka mesajları ve hesap özetleri > Otomasyonlar.](damla-automations.png)
