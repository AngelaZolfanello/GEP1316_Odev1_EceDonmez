# Yapay zekâ geliştirme istemleri ve değerlendirme

## Geliştirme sırasında kullanılan istem

Aşağıdaki istem bu çalışma sırasında kullanıcı tarafından sağlandı. Bu belgede, kullanıcı istemi dışında gerçekleşmemiş konuşmalar eklenmemiştir.

```text
I need you to CREATE THE COMPLETE UNIVERSITY ASSIGNMENT in my currently open VS Code workspace. I am a complete beginner and cannot write Python code myself. Do not just explain or suggest code. Actually create and edit all necessary files in the workspace.

PROJECT NAME: 3D Asset Production Tracker
PURPOSE:
A beginner-friendly command-line application for a small digital game development team to manage 3D asset production tasks.

APPLICATION FEATURES:
1. Add a new asset:
- Asset name
- Asset category (Character, Environment, Prop)
- Assigned artist
- Completion percentage (0–100)
2. List all registered assets in a readable, formatted table.
3. Update an existing asset's completion percentage.
4. Display a production summary:
- Total assets
- Completed assets (100%)
- In-progress assets (1–99%)
- Not started assets (0%)
- Overall average completion percentage
5. Save asset records to a CSV file.
6. Load previously saved assets from the CSV file when the program starts.
7. Include a menu that repeats until the user chooses Exit.

IMPORTANT INPUT VALIDATION:
Never allow the program to crash because of incorrect user input.
Validate ALL inputs:
- Empty asset names must be rejected.
- Empty artist names must be rejected.
- Invalid categories must be rejected.
- Completion percentage must accept only integers from 0 to 100.
- Letters instead of numbers must not crash the program.
- Negative numbers and numbers above 100 must be rejected.
- Invalid menu selections must display a warning and return to the menu.
- Updating an asset that does not exist must display a helpful warning.
- Missing or damaged CSV files must be handled safely.
When input is invalid, explain the error and ask the user again.

PYTHON ASSIGNMENT REQUIREMENTS:
Make sure the final application explicitly includes:
- At least 3 different user inputs with validation.
- At least 2 if/elif/else decision structures.
- At least 1 loop.
- At least 3 clearly named functions.
- Lists and/or dictionaries to store asset information.
- Formatted console output.
- CSV file saving and loading.
- Beginner-friendly comments explaining important code sections.

FILES TO CREATE:
1. character_creation.py
Complete working Python application.
2. README.md
Explain the project, its purpose, features, installation, how to run it, and example usage. Include a section indicating where I should add screenshots.
3. PROMPTLAR.md
Document AI prompts used during development. Do not invent conversations that did not happen. Include the current development prompt and leave space for additional prompts and my evaluation of Copilot's answers.
4. TESTLER.md
Create at least 5 test scenarios in a table with input, expected result and actual result. Include at least 2 invalid or edge-case tests. Leave actual results clearly marked for me to fill in after running the tests.
5. RAPOR_TASLAK.md
Prepare a structured 2–3 page assignment report in Turkish, following these sections:
- Problem and target user
- Application design and pseudocode
- AI development process
- Testing and debugging
- Reflection (200–300 words)
- AI usage declaration
- APA 7 reference for GitHub Copilot
IMPORTANT: Do not invent personal experiences, test results, or debugging events. Mark information that requires my own confirmation with [KENDİ DENEYİMİMLE DOLDURULACAK].

DESIGN:
- Use simple Python suitable for a first-year programming student.
- Do not use external Python libraries.
- Use Turkish for user-facing messages and documentation.
- Keep the code readable and avoid unnecessary complexity.
- Use functions instead of repeating code.
- Make sure all paths work from the project folder.

FINAL CHECK:
Before finishing:
1. Check that the Python file has valid syntax.
2. Check that every required feature is implemented.
3. Check that input validation works.
4. Check that CSV saving and loading work.
5. Run the application or tests if possible.
6. Fix any errors you find.
7. Explain in simple Turkish how I can run the program.
Create all these files directly in my open workspace. Do not merely print the code in the chat. Start implementing now.
```

## Ek istemler

Copilot'un yanıt özetleri ve kararlar, kullanıcı tarafından bu belge için bildirilen bilgilere dayanır. İstem metinleri anlamı korunarak özetlenmiştir.

| Tarih | İstem | Copilot yanıtının kısa özeti | Karar | Karar nedeni |
|---|---|---|---|---|
| 15.11.2026 | Başlangıç istemi: oluşturulması istenen 3B varlık takipçisi uygulamasını ve README, PROMPTLAR, TESTLER ve rapor dosyalarını belirtilen gereksinimlerle hazırla. | Copilot dosyaları oluşturdu; uygulama çalıştırılarak test edildi. | Kısmen kabul edildi, geliştirmeye devam edildi. | Copilot istenen dosyaları oluşturdu ve uygulama çalıştı. Ancak gereksinimlerin tamamını karşıladığından emin olmak için kod ve belgeler ayrıca incelendi, tespit edilen eksikler için ek istemler verildi. |
| 15.11.2026 | `character_creation.py` dosyasını değiştirmeden gereksinimlere göre incele ve sonuçları bildir. | Gereksinimlerin çoğunun karşılandığını, iki ayrı açık `if/elif/else` zinciri şartının belirsiz kaldığını belirtti. | Kabul edildi. | Olası eksikliği tespit etti. |
| 15.11.2026 | İkinci açık `if/elif/else` yapısını ekle; hangi iki yapının şartı karşıladığını açıkla. | `main()` menüsünün seçimleri, `show_summary()` fonksiyonunun tamamlanma durumlarını yönettiğini bildirdi; sözdizimi kontrolü temiz geçti. | Keep ile kabul edildi. | İkinci karar yapısı eklendi ve doğrulama başarılı oldu. |
| 15.11.2026 | `show_summary` fonksiyonundaki sınıflandırma ve ortalama hesabını dosyaları değiştirmeden incele. | 0, 1, 99 ve 100 yüzdeleri, boş liste ve %45/%31 örneği kontrol edildi; hesap doğru bulundu. | Kabul edildi. | Sınıflandırma sınırları ve ortalama hesabı kontrollerde doğru sonuç verdi. |
| 15.11.2026 | README dosyasını ödev gereksinimlerine göre incele. | Python kurulum açıklamasının eksik, diğer temel bölümlerin mevcut olduğunu belirtti. | Kabul edildi. | Eksik kurulum açıklamasını doğru biçimde tespit etti. |
| 15.11.2026 | README'ye resmi Python indirme bağlantısını, Windows'ta `Add Python to PATH` bilgisini ve sürüm doğrulama adımlarını ekle; mevcut çalıştırma talimatlarını koru. | İstenen kurulum bilgileri eklendi ve mevcut çalıştırma talimatları korundu. | Keep ile kabul edildi. | İstenen bilgiler eklendi, çalıştırma talimatları değişmeden kaldı. |

## Copilot yanıtlarına ilişkin kişisel değerlendirme

Bu çalışmada Copilot dosyaları oluşturdu; uygulama çalıştırılarak test edildi. Kullanıcı tarafından bildirilen testlerde varlık ekleme, geçersiz yüzde girdileri, listeleme, özetleme, güncelleme ve yeniden açınca kayıtların korunması denendi.

[KENDİ DENEYİMİMLE DOLDURULACAK: Copilot yanıtlarına ilişkin kişisel görüşünüzü, size en çok yardımcı olan önerileri ve kendi kabul, düzenleme ya da reddetme kararlarınızın nedenlerini ekleyin.]
