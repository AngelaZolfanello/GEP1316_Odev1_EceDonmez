"""Küçük bir ekip için 3B varlık üretim takip uygulaması."""

import csv
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "assets.csv"
CATEGORIES = {
    "character": "Character",
    "karakter": "Character",
    "environment": "Environment",
    "çevre": "Environment",
    "cevre": "Environment",
    "prop": "Prop",
    "obje": "Prop",
}
CSV_COLUMNS = ["name", "category", "artist", "completion"]


def get_non_empty_text(prompt, field_name):
    """Kullanıcı boş metin girmediğinde değeri döndür."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"Uyarı: {field_name} boş bırakılamaz. Lütfen tekrar deneyin.")


def get_category():
    """Desteklenen kategorilerden birini iste; Türkçe adları da kabul et."""
    while True:
        answer = input(
            "Kategori (Character/Karakter, Environment/Çevre, Prop/Obje): "
        ).strip().casefold()
        if answer in CATEGORIES:
            return CATEGORIES[answer]
        print("Uyarı: Geçersiz kategori. Listelenen kategorilerden birini girin.")


def get_completion(prompt="Tamamlanma yüzdesi (0-100): "):
    """0-100 aralığında bir tam sayı iste."""
    while True:
        answer = input(prompt).strip()
        try:
            percentage = int(answer)
        except ValueError:
            print("Uyarı: Tamamlanma yüzdesi bir tam sayı olmalıdır.")
            continue

        # Sayıya dönüştürmek yeterli değildir; istenen aralığı da kontrol et.
        if 0 <= percentage <= 100:
            return percentage
        print("Uyarı: Yüzde 0 ile 100 arasında olmalıdır.")


def load_assets(csv_path=CSV_FILE):
    """Geçerli kayıtları yükle ve eksik/bozuk dosyayı güvenle ele al."""
    assets = []
    try:
        with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            # Beklenen sütunlar yoksa dosya bu uygulamanın kayıt biçiminde değildir.
            if not reader.fieldnames or not set(CSV_COLUMNS).issubset(
                reader.fieldnames
            ):
                print(
                    "Uyarı: CSV başlıkları eksik veya dosya bozuk. "
                    "Kayıtlar yüklenmedi."
                )
                return assets

            for row_number, row in enumerate(reader, start=2):
                try:
                    name = (row.get("name") or "").strip()
                    category = (row.get("category") or "").strip()
                    artist = (row.get("artist") or "").strip()
                    completion = int((row.get("completion") or "").strip())
                except (TypeError, ValueError):
                    print(
                        f"Uyarı: CSV dosyasındaki {row_number}. satır geçersiz; "
                        "bu satır atlandı."
                    )
                    continue

                # Bozuk bir satır diğer doğru kayıtların yüklenmesini engellemez.
                if (
                    not name
                    or not artist
                    or category not in ("Character", "Environment", "Prop")
                    or not 0 <= completion <= 100
                    or any(
                        asset["name"].casefold() == name.casefold()
                        for asset in assets
                    )
                ):
                    print(
                        f"Uyarı: CSV dosyasındaki {row_number}. satır geçersiz; "
                        "bu satır atlandı."
                    )
                    continue

                assets.append(
                    {
                        "name": name,
                        "category": category,
                        "artist": artist,
                        "completion": completion,
                    }
                )
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı. Yeni bir varlık listesiyle başlanacak.")
    except (OSError, UnicodeDecodeError, csv.Error) as error:
        print(f"Uyarı: CSV dosyası okunamadı ({error}). Boş listeyle başlanacak.")

    return assets


def save_assets(assets, csv_path=CSV_FILE):
    """Tüm kayıtları CSV dosyasına yaz ve işlemin sonucunu bildir."""
    try:
        with open(csv_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_COLUMNS)
            writer.writeheader()
            writer.writerows(assets)
    except (OSError, csv.Error) as error:
        print(f"Hata: Varlıklar CSV dosyasına kaydedilemedi ({error}).")
        return False

    print("Varlıklar CSV dosyasına kaydedildi.")
    return True


def add_asset(assets):
    """Her girişi doğrulayarak yeni bir varlık ekle."""
    name = get_non_empty_text("Varlık adı: ", "Varlık adı")
    if any(asset["name"].casefold() == name.casefold() for asset in assets):
        print("Uyarı: Bu adda bir varlık zaten kayıtlı.")
        return False

    category = get_category()
    artist = get_non_empty_text("Atanan sanatçı: ", "Sanatçı adı")
    completion = get_completion()
    # Her varlığın bilgilerini tek bir sözlükte saklayıp listeye ekle.
    assets.append(
        {
            "name": name,
            "category": category,
            "artist": artist,
            "completion": completion,
        }
    )
    print(f"'{name}' varlığı listeye eklendi.")
    return True


def list_assets(assets):
    """Tüm varlıkları okunabilir bir tabloda göster."""
    if not assets:
        print("Henüz kayıtlı varlık yok.")
        return

    headers = ("Varlık adı", "Kategori", "Sanatçı", "Tamamlanma")
    rows = [
        (
            str(asset["name"]),
            str(asset["category"]),
            str(asset["artist"]),
            f"%{asset['completion']}",
        )
        for asset in assets
    ]
    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    ]

    def format_row(values):
        return "| " + " | ".join(
            f"{value:<{widths[index]}}" for index, value in enumerate(values)
        ) + " |"

    print(format_row(headers))
    print("+-" + "-+-".join("-" * width for width in widths) + "-+")
    for row in rows:
        print(format_row(row))


def update_asset(assets):
    """Varlığı ada göre bul ve tamamlanma yüzdesini güncelle."""
    if not assets:
        print("Güncellenecek varlık yok.")
        return False

    name = get_non_empty_text(
        "Güncellenecek varlığın adı: ", "Varlık adı"
    )
    for asset in assets:
        if asset["name"].casefold() == name.casefold():
            asset["completion"] = get_completion(
                "Yeni tamamlanma yüzdesi (0-100): "
            )
            print(f"'{asset['name']}' varlığının ilerlemesi güncellendi.")
            return True

    print(f"Uyarı: '{name}' adında bir varlık bulunamadı.")
    return False


def show_summary(assets):
    """Varlık sayılarını ve ortalama tamamlanma yüzdesini göster."""
    total = len(assets)
    completed = 0
    in_progress = 0
    not_started = 0
    for asset in assets:
        if asset["completion"] == 100:
            completed += 1
        elif asset["completion"] > 0:
            in_progress += 1
        else:
            not_started += 1

    # Boş listede sıfıra bölünme olmaması için ortalamayı ayrıca hesapla.
    average = (
        sum(asset["completion"] for asset in assets) / total if total else 0
    )

    print("\n--- Üretim Özeti ---")
    print(f"Toplam varlik: {total}")
    print(f"Tamamlanan (%100): {completed}")
    print(f"Devam eden (%1-99): {in_progress}")
    print(f"Başlamayan (%0): {not_started}")
    print(f"Ortalama tamamlanma: %{average:.1f}")


def main():
    """Kullanıcı çıkışı seçene kadar tekrar eden menüyü çalıştır."""
    assets = load_assets()
    while True:
        print(
            "\n=== 3B Varlık Üretim Takipçisi ===\n"
            "1. Yeni varlık ekle\n"
            "2. Varlıkları listele\n"
            "3. Tamamlanma yüzdesini güncelle\n"
            "4. Üretim özetini göster\n"
            "5. Çıkış"
        )
        choice = input("Seçiminiz (1-5): ").strip()

        # Her seçenek ayrı bir dalda işlenir; geçersiz seçim döngüyü bitirmez.
        if choice == "1":
            if add_asset(assets):
                save_assets(assets)
        elif choice == "2":
            list_assets(assets)
        elif choice == "3":
            if update_asset(assets):
                save_assets(assets)
        elif choice == "4":
            show_summary(assets)
        elif choice == "5":
            save_assets(assets)
            print("Programdan çıkılıyor. Görüşmek üzere!")
            break
        else:
            print("Uyarı: Geçersiz menü seçimi. Lütfen 1-5 arasında seçin.")


if __name__ == "__main__":
    main()