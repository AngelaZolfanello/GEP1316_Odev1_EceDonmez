# Test sonuçları

Aşağıdaki tabloda yalnızca uygulamanın gerçek terminalde denendiği ve kullanıcı tarafından bildirilen testler yer alır. Bildirilen 11 testin tamamı başarılı olmuştur.

| No | Senaryo | Girdi / adımlar | Beklenen sonuç | Gerçekleşen sonuç | Durum |
|---:|---|---|---|---|---|
| 1 | Geçerli varlık ekleme | Ad: `ana karakter`; kategori: `Character`; sanatçı: `Ece`; yüzde: `45` | Varlık başarıyla eklenmeli ve CSV dosyasına kaydedilmeli. | Varlık başarıyla eklendi ve CSV dosyasına kaydedildi. | Başarılı |
| 2 | Sayı olmayan yüzde girişi | Yüzde alanına sırayla `abc`, `zırt zort` ve `zürdürdürü` girildi. | Her geçersiz girdi için tam sayı uyarısı verilmeli, yeniden giriş istenmeli ve program çökmemeli. | Her girişte tam sayı uyarısı verildi ve yeniden giriş istendi; program çökmedi. | Başarılı |
| 3 | 100'den büyük yüzde | Yüzde alanına `150` girildi. | 0–100 aralığı dışında olduğu belirtilerek değer reddedilmeli ve yeniden giriş istenmeli. | `150`, aralık dışında olduğu için reddedildi. | Başarılı |
| 4 | Negatif yüzde | Yüzde alanına `-5` girildi. | 0–100 aralığı dışında olduğu belirtilerek değer reddedilmeli ve yeniden giriş istenmeli. | `-5`, aralık dışında olduğu için reddedildi. | Başarılı |
| 5 | İkinci geçerli varlığı ekleme | Ad: `test karakter`; kategori: `Character`; sanatçı: `ece`; yüzde: `31` | İkinci varlık başarıyla eklenmeli. | İkinci varlık başarıyla eklendi. | Başarılı |
| 6 | Varlıkları listeleme | Varlık listesi görüntülendi. | İki kayıt, girilen bilgilerle doğru biçimde görüntülenmeli. | İki varlık da doğru bilgilerle görüntülendi. | Başarılı |
| 7 | İlk üretim özeti | Üretim özeti görüntülendi. | Toplam 2, tamamlanan 0, devam eden 2, başlamayan 0 ve ortalama %38 gösterilmeli. | Toplam 2, tamamlanan 0, devam eden 2, başlamayan 0 ve ortalama %38 görüntülendi. | Başarılı |
| 8 | Varlık yüzdesini güncelleme | `ana karakter` varlığının yüzdesi `45`'ten `69`'a güncellendi. | Yüzde güncellenmeli ve yeni değer CSV dosyasına kaydedilmeli. | Yüzde %45'ten %69'a güncellendi ve CSV dosyasına kaydedildi. | Başarılı |
| 9 | Güncelleme sonrası özet | Üretim özeti yeniden görüntülendi. | İki varlığın güncel yüzdelerine göre ortalama %50 gösterilmeli. | Ortalama %50 olarak görüntülendi. | Başarılı |
| 10 | Bulunmayan varlığı güncelleme | Kayıtlı olmayan bir varlık adı girildi. | Varlığın bulunamadığını bildiren uyarı gösterilmeli ve uygulama menüye dönmeli. | Uyarı gösterildi ve menüye dönüldü. | Başarılı |
| 11 | Kaydedilmiş kayıtları yeniden yükleme | Program kapatıldı ve yeniden açıldı; ardından üretim özeti görüntülendi. | Kayıtlar CSV'den korunarak yüklenmeli ve özet ortalamayı yeniden %50 göstermeli. | Kayıtlar korundu; özet yeniden %50 gösterdi. | Başarılı |
