# 3B Varlik Üretim Takipçisi – Ödev Raporu Taslağı

## 1. Problem ve hedef kullanıcı

Küçük bir dijital oyun geliştirme ekibinde çok sayıda 3B model aynı anda hazırlanabilir. Varlığın kim tarafından yapıldığı ve üretimin hangi aşamada olduğu kolayca unutulabilir. Bu durum, ekip üyelerinin ilerlemeyi takip etmesini ve tamamlanmamış işleri görmesini zorlaştırır. Bu proje, bu bilgileri tek bir listede saklayan basit bir komut satırı uygulaması sunar.

Hedef kullanıcı, temel bilgisayar kullanımı olan ancak özel proje yönetim yazılımına ihtiyaç duymayan küçük bir oyun ekibi üyesidir. Programlama dersi açısından uygulama; değişkenleri, listeleri ve sözlükleri, koşulları, döngüleri, fonksiyonları, kullanıcı girdisini ve CSV dosyalarını bir arada kullanır. Varlık kaydı ad, kategori, sanatçı ve 0–100 arası tamamlanma yüzdesinden oluşur. Kategoriler Character, Environment ve Prop olarak tutulur.

## 2. Uygulama tasarımı ve sözde kod

Varlıklar Python sözlüklerinden oluşan bir listede tutulur. Böylece her varlığın alanları bir arada kalır ve kayıtlar kolayca eklenebilir, listelenebilir veya güncellenebilir. `get_non_empty_text`, `get_category` ve `get_completion` fonksiyonları kullanıcıdan veri alırken doğrulama yapar. Girdi geçersiz olduğunda açıklayıcı uyarı gösterilir ve döngü aynı bilgiyi yeniden ister. Tamamlanma yüzdesi önce tam sayıya çevrilir; harf gibi sayısal olmayan girişler yakalanır ve 0–100 aralığı denetlenir.

Menü, kullanıcı çıkış seçeneğini seçene kadar çalışan bir döngü içindedir. Her seçenek bir `if/elif/else` yapısıyla yönlendirilir. Varlıklar proje klasöründeki `assets.csv` dosyasından okunur; ekleme ve güncelleme sonrasında dosyaya yazılır. Bozuk CSV satırları atlanır ve kullanıcı bilgilendirilir. Üretim özeti tamamlanan, devam eden ve başlamayan kayıtları sayar. Ortalama, toplam varlık sayısı sıfır değilse hesaplanır; boş listede sıfır gösterilir.

**Sözde kod**

```text
CSV dosyasini oku; bulunamiyorsa bos varlik listesi olustur
KULLANICI cikis seceneğini secene kadar:
    menuyu goster ve secimi al
    eger secim yeni varlik eklemekse:
        adi, kategoriyi, sanatciyi ve yuzdeyi dogrulayarak al
        kaydi listeye ekle ve CSV'ye kaydet
    degilse eger secim listelemekse: tabloyu goster
    degilse eger secim guncellemekse:
        adi ara; bulunursa dogrulanmis yuzdeyi ata ve kaydet
        bulunamazsa uyari goster
    degilse eger secim ozetse:
        tamamlanan (%100), devam eden (%1-99) ve baslamayan (%0)
        varliklari ayri ayri say
        ortalama tamamlanma yuzdesini hesapla
        sayilari ve ortalamayi goster
    degilse eger secim cikissa: kaydet ve donguden cik
    aksi halde: gecersiz secim uyarisi goster
```

## 3. Yapay zekâ geliştirme süreci

Çalışma, istenen uygulama ve teslim dosyalarını tanımlayan başlangıç istemiyle başladı. GitHub Copilot kodu ve proje belgelerini oluşturdu. Ardından kod ödev gereksinimlerine göre incelendi; menüdeki karar yapısına ek olarak üretim özetinde ikinci bir açık `if/elif/else` zinciri eklendi. `show_summary` fonksiyonunun sınıflandırma ve ortalama hesabı kontrol edildi. README'deki Python kurulumu açıklaması resmi indirme bağlantısı, Windows'ta `Add Python to PATH` ve sürüm doğrulama adımlarıyla tamamlandı. Başlangıç ve takip istemleri `PROMPTLAR.md` dosyasında belgelendi.

İstem günlüğü hazırlanırken Copilot'un `PROMPTLAR.md` dosyasındaki ek istem ve kişisel değerlendirme alanlarını başlangıçta boş bırakmış olduğu dosyayı incelerken fark edildi. Bu, istenen belge içeriğinin ilk hazırlamada tamamlanmamasına ilişkin somut bir eksiklikti. Daha sonra gerçekleşen ek istemler, yanıt özetleri ve kararlar günlüğe kaydedilerek eksiklik giderildi; kişisel görüş gerektiren alan ise kullanıcıya bırakıldı.

## 4. Test ve hata ayıklama

Uygulama kullanıcı tarafından gerçek terminalde denenmiş ve bildirilen 11 testin tamamı başarılı olmuştur. `TESTLER.md` dosyasında kayıtlı denemelerde `ana karakter` adlı Character varlığı Ece sanatçıya atanarak %45 ile eklenmiş ve CSV'ye kaydedilmiştir. Yüzde alanına `abc`, `zırt zort` ve `zürdürdürü` girildiğinde her seferinde tam sayı uyarısı verilmiş, yeniden giriş istenmiş ve program çökmemiştir. `150` ve `-5` değerleri aralık dışında olduğu için reddedilmiştir. `test karakter` adlı ikinci Character varlığı ece sanatçıya atanarak %31 ile eklenmiştir.

Listelemede iki varlık da doğru bilgilerle görüntülenmiştir. İlk özette toplam 2, tamamlanan 0, devam eden 2, başlamayan 0 ve ortalama %38 görülmüştür. `ana karakter` yüzdesi %45'ten %69'a güncellenerek CSV'ye kaydedilmiş; sonraki özette ortalama %50 olmuştur. Kayıtlı olmayan bir varlık adı için uyarı verilmiş ve menüye dönülmüştür. Program kapatılıp yeniden açıldığında CSV kayıtları korunmuş, özet yine %50 göstermiştir. Boş ad, geçersiz kategori ve yanlış menü seçimi bu bildirilen terminal denemeleri arasında yer almamaktadır; bu rapor bunları yapılmış testler olarak sunmaz.

## 5. Yansıtma

Bu projede en kolay bulduğum şey, ChatGPT'ye ne istediğimi anlatıp talimat vermekti. İhtiyacımı açıkça ifade etmek, uygulamanın özelliklerini ve teslim dosyalarını belirlememe yardımcı oldu. Buna karşılık en zorlandığım nokta, GitHub Copilot'un ürettiği kodu ve yaptığı değişiklikleri anlamaktı. Kodun çalışması tek başına yeterli değildi; gereksinimlere uygunluğunu ayrıca incelemek ve test sonuçlarını değerlendirmek gerekiyordu.

Öğrendiğim en önemli şey, ChatGPT ve GitHub Copilot'u insan yönlendirmesiyle birlikte kullanarak basit kod uygulamalarını yaklaşık bir saat içinde oluşturabilmem oldu. Süreçte ChatGPT'den aldığım talimatları Copilot'a, Copilot'un yanıtlarını ise kontrol ve yönlendirme için ChatGPT'ye taşıyarak ilerledim. Bu yöntem üretimi hızlandırdı; ancak ortaya çıkan kodu anlama ve doğrulama sorumluluğunun bende olduğunu da gösterdi. Örneğin, özetteki yüzde sınıflandırmasını ve ortalamayı ayrıca kontrol ettim; terminalde yaptığım denemelerde kayıtların program yeniden açıldığında CSV'den korunduğunu gördüm.

Terminal denemeleri, doğru kayıt ekleme ve güncellemenin yanı sıra metin biçimindeki ve aralık dışındaki yüzde girdilerinin nasıl ele alındığını görmemi sağladı. İki varlığın yüzdeleri üzerinden özet değerini kontrol etmek, uygulamanın hesaplarının beklenen sonuçlarla tutarlı olup olmadığını değerlendirmeme yardımcı oldu. Böylece istem yazmanın yanında, sonucu gerçek kullanımda sınamanın da bu sürecin parçası olduğunu öğrendim.

Uygulama, bir liste ve CSV dosyasıyla temel üretim takibini karşılıyor; ancak kayıtları filtreleme olanağı yok. Bir sonraki sürümde sanatçıya, kategoriye ve tamamlanma yüzdesine göre filtreleme eklemek isterdim. Böylece görevlerin ilerlemesini karşılaştırabilir ve gecikmelerin nedenlerini değerlendirebilirdim. Bu geliştirme, mevcut basit iş akışını korurken ekip için daha anlamlı bir üretim görünümü sağlayabilir.

## 6. Yapay zekâ kullanım beyanı

Bu uygulamanın kodu GitHub Copilot tarafından oluşturulmuştur. ChatGPT, geliştirme istemlerini ve kontrolleri yönlendirmek, Copilot yanıtlarını değerlendirmek ve izlenecek adımları belirlemek için kullanılmıştır. İstemler `PROMPTLAR.md` dosyasında belgelenmiştir. Uygulamayı kendi terminalimde çalıştırarak test ettim; bildirilen test sonuçları `TESTLER.md` dosyasına işlenmiştir. Bu beyan, kodu kişisel olarak yazdığımı veya değiştirdiğimi iddia etmez.

## 7. Kaynakça (APA 7)

GitHub. (n.d.). *GitHub Copilot*. [https://github.com/features/copilot](https://github.com/features/copilot)

OpenAI. (2026). *ChatGPT* [Büyük dil modeli]. https://chatgpt.com/