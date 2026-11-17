# Pandas Eğitimi (Eğitmen Notları)

Başlangıç seviyesi (Python bilen, numpy/pandas bilmeyen) katılımcılar için 1.5-2 saatlik uygulamalı eğitim. Konu: rastgele öğrenci notlarından çan eğrisi ve bağıl değerlendirme (AA-FF).

## İçerik

| Dosya | Açıklama |
|---|---|
| `slides/egitim.md` | Marp slaytları (Türkçe) |
| `atolye/atolye-rehberi.md` | Katılımcılar için adım adım görevler ve beklenen çıktılar |
| `cozum/cozum.py` | Eğitmen çözümü (baştan sona çalışır) |
| `veri/ogrenciler.csv` | Katılımcılara dağıtılacak hazır veri (`pd.read_csv` ile yüklenir) |
| `veri/uret.py` | CSV'yi üreten eğitmen betiği (katılımcılara verilmez) |
| `docs/superpowers/specs/` | Tasarım dokümanı (İngilizce) |

## Katılımcı kurulumu

```bash
python -m pip install numpy pandas matplotlib
```

(`pip` yerine `python -m pip`: Git Bash'te yanlış Python'a bağlanmayı önler.)

## Slaytları açmak

VS Code'da **"Marp for VS Code"** eklentisini kurun; `slides/egitim.md` dosyasında önizleme düğmesi çıkar. Dışa aktarma (HTML/PDF/PPTX) yine eklentinin komut paletinden: *Marp: Export Slide Deck*.

## Çözümü çalıştırmak

```bash
python cozum/cozum.py     # can_egrisi.png ve sonuclar.csv üretir
```

## Önemli tasarım kararları

- **Tek rastgele API:** `np.random.default_rng(42)` (numpy bölümündeki demo ve `uret.py`). `np.random.seed` ile karıştırmayın, sayılar değişir.
- **Veri hazır verilir:** katılımcılar veri üretmez; `ogrenciler.csv` dosyasını dağıtın (e-posta, USB, repo). Slayt ve rehberde beklenen `df.head()` çıktısı var. Yeniden üretmek için `python veri/uret.py` (seed 42, aynı dosya çıkar).
- **std:** `ddof=0` (popülasyon) her yerde açıkça yazılır. numpy varsayılanı 0, pandas varsayılanı 1.
- **Ağırlıklar** (vize %40 / final %60), **harf sınırları** ve **otomatik FF eşiği** (`final < 35`) kod başında sabitlerdir; kurumunuza göre değiştirirseniz slayt ve rehberdeki beklenen sayıları (`value_counts` tablosu) da güncelleyin.
- Harf notları, FF kuralı uygulanmadan önce tüm sınıf üzerinden hesaplanan T-skoruna göre verilir.

## Süre (~110 dk)

Kurulum 10 · numpy 15 · istatistik 10 · pandas 25 · ağırlıklı ortalama 10 · çan eğrisi 10 · z/T 10 · harf notları 15 · challenge 5+. Kısalırsa neyin kesileceği `atolye/atolye-rehberi.md` sonunda yazıyor.
