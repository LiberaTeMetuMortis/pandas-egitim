# Atölye Rehberi: Bağıl Değerlendirme

Slaytları takip ederken bu rehber her adımın **görevini** ve **beklenen çıktıyı** verir. Kodu slayttan **kendiniz yazın**. Çıktınız beklenenle uyuşmuyorsa ilerlemeden önce eğitmene sorun.

> Veri hazır: eğitmenin verdiği `ogrenciler.csv` dosyasını `analiz.py` ile aynı klasöre koyun.

Dosya: `analiz.py`. Çalıştırma: `python analiz.py`

---

## Adım 1: Kurulum (10 dk)

**Görev:** `numpy`, `pandas`, `matplotlib` kurun ve import edin; sürümleri yazdırın.

**Kontrol:** Hata yok, sürüm numaraları yazdı.

## Adım 2: numpy (15 dk)

**Görev:** `[70, 55, 80, 45, 90]` dizisini oluşturun. Ortalamasını, en büyüğünü, 60'tan büyük olanları yazdırın. Sonra `default_rng(42)` ile 5 rastgele tam sayı ve 5 normal dağılımlı sayı üretin.

**Kontrol:** Ortalama `68.0`. `rng.integers(0, 100, size=5)` ilk çağrıda `[ 8 77 65 43 43]`.

## Adım 3: İstatistik (10 dk, yazı yok, sadece anlatım)

Kavramlar: ortalama, varyans, standart sapma, çan eğrisi, %68 kuralı.

**Kontrol (kağıt/numpy):** `np.array([58,59,60,61,62]).std()` → `1.414...`, `np.array([20,40,60,80,100]).std()` → `28.28...`

## Adım 4: Veri ve pandas (25 dk)

**Görev:** `pd.read_csv("ogrenciler.csv")` ile veriyi yükleyin. Sonra `head`, `shape`, `info`, `describe` çalıştırın. Sütun seçin; final'i 35 altı olanları ve vize+final 80 üstü olanları filtreleyin.

**Kontrol:**
```
   ogrenci_no    ad   soyad  vize  final
0     2024482  Onur  Yılmaz  70.0   64.0
1     2024453  Emre Özdemir  54.0   54.0
2     2024322 Ceren Şimşek  60.0   34.0
3     2024212 Deniz  Yılmaz  58.0   65.0
4     2024195 Kerem   Polat  65.0   86.0
(100, 5)
```
`vize` ortalaması `59.29`, en yüksek final `95.0`. Final'i 35 altı: 5 öğrenci. Vize ve final ikisi de 80 üstü: tek öğrenci (Burak Erdoğan).

> `FileNotFoundError` alırsanız `ogrenciler.csv` dosyası `analiz.py` ile aynı klasörde değildir (`python analiz.py` komutunu o klasörden çalıştırın).

**İsteğe bağlı (keşif):** "pandas'ta başka neler yapabiliriz" slaytlarındaki `sort_values`, `.loc`, `.iloc`, `value_counts`, `groupby` örneklerinden 2-3 tanesini deneyin. Çıktıyı beklenen değerlerle karşılaştırın (ör. `df["ad"].nunique()` → `20`).

## Adım 5: Ağırlıklı ortalama (10 dk)

**Görev:** `ortalama = vize × 0.4 + final × 0.6` sütununu ekleyin. En yüksek 5 öğrenciyi yazdırın.

**Kontrol:** 1. sırada Burak Erdoğan, `87.2`.

## Adım 6: Çan eğrisi (10 dk)

**Görev:** `mu`, `sigma` (`ddof=0`) hesaplayın. Histogram çizin, sonra normal dağılım eğrisini üstüne ekleyin.

**Kontrol:** `Ortalama: 60.45, std: 10.86`. Histogram yaklaşık çan şeklinde, eğri çubukları kabaca takip ediyor.

## Adım 7: z ve T skoru (10 dk)

**Görev:** `z` ve `t` sütunlarını ekleyin.

**Kontrol:** Zeynep Demir (vize 61, final 73): ortalama `68.2`, z ≈ `0.71`, T ≈ `57.1`.

## Adım 8: Harf notları (15 dk)

**Görev:** `pd.cut` ile harf sütununu oluşturun, final < 35 için FF kuralını uygulayın, `value_counts` ile dağılımı yazdırın.

**Kontrol:**

| AA | BA | BB | CB | CC | DC | DD | FD | FF |
|---|---|---|---|---|---|---|---|---|
| 14 | 13 | 32 | 11 | 15 | 7 | 3 | 0 | 5 |

Zeynep Demir → **BA**.

---

## Challenge'lar

1. Kaç öğrenci FF aldı? Kimler?
2. T-skoruna göre ilk 5 öğrenciyi ad, soyad, ortalama, harf ile yazdırın. *(Cevap: Burak Erdoğan, Mehmet Özdemir, Deniz Erdoğan, Deniz Kurt, Ece Yılmaz; hepsi AA)*
3. Vizesi finalinden en az 20 puan yüksek olanlar kimler?
4. Sonuçları `sonuclar.csv` olarak kaydedin.
5. **Bonus:** Ağırlıkları %50/%50 yapın. Hangi öğrencilerin harfi değişti?

## Eğitmen için: süre kısalırsa kesilebilecekler

Sırayla kesin: "başka neler yapabiliriz" slaytları (sadece anlatın, kodlatmayın) → Challenge 3-5 → `info()` ve sıralama → normal eğri üst üste çizimi (sadece histogram). **Adım 5-8 (ortalama → z/T → harf) her koşulda tamamlanmalı.**
