---
title: Alıcılar ve kategoriler
summary: Damla'nın paranın nereye gittiğini nasıl öğrendiğini ve bunu nasıl değiştireceğinizi anlatır.
order: 60
---

# Alıcılar ve kategoriler

Bir alıcı, paranın gittiği dükkân, şirket veya kişidir. Bir kategori, harcamasının veya gelirinin girdiği kümedir; örneğin Market veya Maaş. Bu sayfa, Damla'nın her alıcıyı ilk kez nasıl dosyaladığını, sonrasında neyi hatırladığını ve bunlardan herhangi birini nasıl değiştireceğinizi anlatır.

## Ne zaman kullanılır

- Bir banka uyarısı veya yapıştırılmış mesaj yanlış kategoriye kaydedildi ve sonrakilerin doğru olmasını istiyorsunuz.
- Kendi kategoriniz istiyorsunuz ya da bir kategoriye daha iyi bir ad veya simge istiyorsunuz.
- Bir ekstre içe aktardınız ve Damla bazı satırlar hakkında "Bunlar kim?" diye soruyor.
- İçgörü sekmelerine güvenmeden önce kayıtların nasıl sıralandığını kontrol etmek istiyorsunuz.

## Adım adım

Bugün ekranındaki dişli simgesine dokunarak Ayarlar'ı açın, sonra **Kategoriler**'e dokunun.

1. Üstte, anahtarla hangi listeyi istediğinizi seçin: **Harcama** veya **Gelir**.
2. Yeni bir kategori oluşturmak için **Ekle**'ye dokunun.
3. **Ad**'ı yazın. Simge, yazarken adı izler: birçok harcama türü (spor salonu, evcil hayvanlar, çocuklar, sigorta, tamirat ve daha fazlası) kendi kendine eşleşen bir resim alır.
4. Kendi resminizi seçmek için **Simge** başlıklı ızgaradan birine dokunun. Ad alanının altındaki metin daha sonra "Kendi simgeniz. Başka birini seçin ya da öneriye dönmek için aynı olana dokunun." der.
5. **Kaydet**'e dokunun. Kaydetmeden çıkmak için **Vazgeç**'e dokunun.

Aynı ekranda:

- Yeniden adlandırmak veya simgesini değiştirmek için herhangi bir kategoriye dokunun, aynı sayfada yapılır. Her iki yerde de aynı sayfa açılır; başlığı **Yeni kategori** veya **Kategori**'dir.
- Bir kategoriyi emekliye ayırmak için kaydırın ve **Kaldır**'a dokunun.

Bir kategoriyi anında da oluşturabilirsiniz: herhangi bir kayıt formunda Kategori seçicinin altında **Yeni kategori…**'ye dokunun. Hemen seçilir.

## Damla bir alıcıyı nasıl öğrenir

Bir alıcısı olan bir işlemi bir kategoride kaydettiğinizde, Damla bu çifti kaydeder. Aynı dükkândan veya kişiden gelen sonraki uyarı ya da mesaj, hiçbir soru sorulmadan kendi kendine o kategoriye kaydedilir.

Bunun işlemesi için iki alışkanlık:

- Alıcı alanını doldurun. Kayıt formu etiketi harcama için **Kime ödendi (isteğe bağlı)**, gelir için **Kimden (isteğe bağlı)** koyar.
- Ödeme türü değişirse, onu yeni kategoride kaydedin. Aynı alıcının önceki işlemleri başka bir kategorideyse, Damla onlara dokunmadan önce sorar: "Diğer N *alıcı* değişsin mi?" — **\<kategori\> olarak değiştir** veya **Yalnızca bu** seçenekleriyle. Bundan sonra yenilerinin kendi kendine yeni kategoriye gideceğini açıklar.

Damla, her şeyi kapsayan kategori için bir istisna yapar: formda kaydettiğinizde kategori **Diğer** ise (gelir için **Diğer gelir**), çift hatırlanmaz. Orada bırakılan bir kayıt ona hiçbir şey öğretmez.

## İçe aktarma sırasında: alıcı başına bir soru

Bir ekstre içe aktardığınızda (bir CSV dosyası, PDF veya ekran görüntüsü), Damla satırları bilinmeyen alıcılara gruplar; böylece satır başına değil, alıcı başına bir kez cevap verirsiniz. Bölümün başlığı **Bunlar kim? (N kaldı)**'dır ve hiçbir şey içe aktarılmadan önce cevaplanır.

Her soru, alıcının adını, kaç satırı kapsadığını, bir örnek satırı ve giren ya da çıkan paranın toplamını gösterir. Üzerinde **Seç…**'e dokunun ve şunlardan birini seçin:

- **mevcut kategorilerinizden** biri (liste, paranın yönüne uyar),
- **Öneriyi kullan: …**, Damla'nın önerdiği seçim,
- **Kredi kartlarımdan biri**, satırlar bir karta yapılan ödemelerse,
- **Başka bir hesabım**, para kendi hesaplarınız arasında hareket ediyorsa,
- **Ödemesini yaptığım bir mülk ya da varlık**,
- **Bir kişi (borç verme/alma)**,
- **Bunları içe aktarma**, satırları dışarıda bırakmak için.

Öneriler, yaygın satırlar için düz ifade kurallarından gelir: maaş, nakit çekme, banka masrafları, komisyon, EMI, otomatik ödeme talimatı, faiz vb. iPhone'un Apple Intelligence'ı desteklediği yerlerde, cihazdaki model de bir kategori önerebilir. Model, alıcının ifadesini, birkaç örnek satırı, alıcının kaç satırı kapsadığını ve paranın çoğunlukla girdiğini mi yoksa çıktığını mı okur — asla bakiyeleri veya tutarları değil. Kod, modelin söylediğini kullanmadan önce kontrol eder. Alıcı metnindeki bir kart numarası ya da ekstre başlığındaki kendi adınız, model tarafından değil kod tarafından eşleştirilir.

Cevabınız o satırlar için gerçek sayılır ve Damla, öğrenilen çiftleri bir sonraki sefer için saklar.

## Bilmeniz iyi olur

- İki öğrenilmiş desen de uyarsa, en uzun eşleşme kazanır; böylece "XYZ Market" kuralı, düz bir "Market" kuralını yener.
- Kategoriler sizin şekillendirmenize bağlıdır: uygulamadaki hiçbir şey belirli bir ada bağlı değildir.
- Bir kategoriyi kaldırmak onu seçicilerinizden çıkarır. Eski kayıtlar kategorilerini korur. Uygulamanın taksit planı ücretleri için ada göre ihtiyaç duyduğu tek kategori eksikse kendi kendine yeniden oluşturulur.
- Model adımı isteğe bağlıdır ve cihazınızda çalışır. Cihaz onu çalıştıramıyorsa, ifade kuralları yine de işi görür ve her şey dokunuşunuzu bekler.
- Damla bilgi ve tahmin verir. Paranın hangi kategoriye ait olduğu sizin kendi defter tutma kararınızdır.

## İlgili

- [Form doldurun](/guide/recording/fill-a-form/)
- [Bir cümle yazın](/guide/recording/type-a-sentence/)
- [Bir ekstre içe aktarmak](/guide/capture/importing-statements/)
- [Paranın nereye gittiği](/guide/insights/where-the-money-went/)
