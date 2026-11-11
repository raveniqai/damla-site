---
title: Yedekleme ve geri yükleme
summary: Seçtiğiniz bir klasöre şifreli yedekler ve nasıl geri yükleneceği.
order: 20
---

# Yedekleme ve geri yükleme

Yedek, Damla'nın tuttuğu her şeyi içeren tek bir şifreli dosyadır: hesaplarınız, işlemleriniz, planlarınız ve ayarlarınız. Defterlerinizi güvende tutmak ve uygulamayı silerseniz geri yükleyebilmek için bir yedek alırsınız.

## Ne zaman kullanılır

- Uygulamayı silmeden önce. Uygulamayı silmek verisini de siler.
- Kayıtlarınızda büyük bir değişiklik yapmadan önce ya da uygulamanın bir test veya ön sürümünü kurmadan önce.
- Damla'nın her gün, sorulmadan yaptığı bir kopya istediğinizde.
- Defterlerinizin eksiksiz bir kopyasını, uygulamanın dışında ve elinizde tutmak istediğinizde.

Yedekler Ayarlar'da bulunur. Bugün ekranını açın, sağ üstteki dişliye dokunun, sonra **Yedek ve verileriniz**'e dokunun. **Yedek** altındaki her şey telefonda olur; her dosyanın nereye kaydedileceğini siz seçersiniz.

## Adım adım

### Bir yedek dosyası oluşturun

1. Ayarlar'ı açın, sonra **Yedek ve verileriniz**.
2. **Şifreli yedek dışa aktar**'a dokunun.
3. En az 8 karakterli bir parola yazın ve **Dışa aktar**'a dokunun.
4. Beliren paylaş düğmesine dokunun. Dosyayı Files ya da iCloud Drive'a kaydedin veya Mac'inize gönderin.

> **Careful:** Parola, dosyanın tek anahtarıdır. Damla'nın geliştiricisi dahil kimse onsuz yedeği açamaz ve Damla onu kurtaramaz. İfadeyi güvenli, dosyadan ayrı bir yerde saklayın.

> **Note:** Geri yükleme, bu telefondaki her şeyin yerine yedeği koyar. Bir yedeği zaten var olanla birleştiremezsiniz.

### Bir yedeği geri yükleyin

1. Ayarlar'ı açın, sonra **Yedek ve verileriniz**.
2. **Yedekten geri yükle**'ye dokunun ve `damlabackup` dosyasını seçin.
3. O yedeğin parolasını yazın.
4. Damla sizi, bunun bu telefondaki tüm verinin yerine koyacağı konusunda uyarır. Devam etmek için **Her şeyin yerine koy**'a dokunun.

Manuel bir yedekle otomatik olan aynı türden dosyadır ve **Yedekten geri yükle** ikisini de açar. Geri yükleme herhangi bir şifreli yedek dosyasından çalışır.

### Damla'yı kendi kendine yedeklemeye bırakın

Otomatik yedeklemeler, seçtiğiniz bir klasöre aynı türden şifreli dosyayı günde en fazla bir kez yazar.

1. Ayarlar'ı açın, sonra **Yedek ve verileriniz**, sonra **Otomatik yedekleme**.
2. **Bir klasör seçin ve başlayın**'a dokunun ve Files seçicisinden bir klasör seçin.
3. En az 8 karakterli bir parola yazın ve **Başla**'ya dokunun. Damla ilk dosyayı hemen yazar.

O andan sonra, günde bir kez, uygulamadan ayrıldığınızda o klasöre şifreli bir kopya kaydedilir.

> **Note:** Otomatik yedekleme parolasını bu telefonun Keychain'inde tutar, böylece onu yeniden yazmak zorunda kalmazsınız. Ama geri yükleme için yine de ona ihtiyacınız olacak; bu yüzden bir kopyasını telefonun dışında da bir yerde saklayın.

**Otomatik yedeklemeyi durdur** ile kapatmak, o ana kadar yazılmış dosyaları silmez.

## Faydalı bilgiler

> **Limit:** Otomatik yedekleme yalnızca uygulamadan ayrıldığınızda çalışır. Birkaç gün Damla'yı açmazsanız, bu sürede hiçbir şey yedeklenmez.

- Elle dışa aktardığınız bir yedek, `Damla-` ile başlayan, ardından bugünün tarihi gelen ve `.damlabackup` ile biten bir ad alır.
- Otomatik bir yedeğin dosya adı `Damla-auto-` ile başlar, ardından tarih gelir ve `.damlabackup` ile biter. Bugünün dosyası aynı günün öncekini değiştirir.
- iCloud Drive'daki bir klasör, otomatik yedeği bu telefonun dışında da tutar.
- **Otomatik yedekleme** ekranında klasörü ve son yedeğin ne zaman çalıştığını görebilir, hemen bir yedek almak için **Şimdi yedekle**'ye dokunabilirsiniz.
- En yeni 7 otomatik yedek tutulur; daha eskileri kendiliğinden kaldırılır.
- Son otomatik yedek en az üç gün eskiyse, Damla Bugün ekranında bir hatırlatıcı gösterir. Hiç otomatik yedekleme kurmadıysanız ve bir süredir kayıt tutuyorsanız, Bugün bunun yerine "Verilerinizi yedekleyin" satırını gösterir.
- Bir deneme ya da abonelik bitmişse, Damla salt okunur olur; ama yedek dışa aktarma ve geri yükleme çalışmaya devam eder.
- Var olan bir yedeğin parolası kaybedilirse dosya açılamaz. Dosyaya güvenmeden önce onu hâlâ hatırladığınızdan emin olun.

## İlgili

- [Ayarlar, sayfa sayfa](/guide/data/settings-map/)
- [Dışa aktarma ve aile görüntüsü](/guide/data/export-and-family-snapshot/)
- [Gizlilik ve verileriniz](/guide/data/privacy-and-your-data/)
- [Sorun giderme](/guide/help/troubleshooting/)
