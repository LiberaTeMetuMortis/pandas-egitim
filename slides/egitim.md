---
marp: true
theme: default
paginate: true
lang: tr
style: |
  section { font-size: 24px; padding: 36px 56px; line-height: 1.4; }
  h1 { font-size: 1.5em; color: #1f4e79; margin: 0 0 0.4em; }
  h2 { font-size: 1.2em; margin: 0.5em 0 0.3em; }
  p, ul, ol, blockquote { margin: 0.4em 0; }
  pre { font-size: 0.8em; padding: 0.5em 0.8em; margin: 0.4em 0; line-height: 1.25; }
  code { font-size: 0.9em; }
  table { font-size: 0.75em; margin: 0.4em 0; }
  th, td { padding: 2px 10px; }
---

# Python ile Veri Analizi
## numpy ve pandas ile Bağıl Değerlendirme

Bir sınıfın notlarından **çan eğrisi** çizip **harf notlarını** hesaplayacağız.

<!-- Not: Eğitmen için toplam süre ~110 dk. Her bölüm sonunda öğrenciler kodu KENDİLERİ yazar. -->

---

# Bugün ne yapacağız?

Hazır verilmiş 100 öğrencinin **vize** ve **final** notları var.

Sonunda herkes şunu üretmiş olacak:

| Öğrenci | Ortalama | T-skoru | Harf |
|---|---|---|---|
| Zeynep Demir | 68.2 | 57.1 | **BA** |

---

# Yol haritası

1. Kurulum (10 dk)
2. numpy (15 dk)
3. İstatistik: ortalama, standart sapma, çan eğrisi (10 dk)
4. pandas (25 dk)
5. Ağırlıklı ortalama (10 dk)
6. Çan eğrisini çizmek (10 dk)
7. z-skoru ve T-skoru (10 dk)
8. Harf notları (15 dk)

---

# 1. Kurulum

Git Bash veya VS Code terminalinde:

```bash
python -m pip install numpy pandas matplotlib
```

Yeni bir dosya açın: `analiz.py`

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(np.__version__, pd.__version__)
```

Çalıştırın: `python analiz.py`

> Hata yoksa hazırız. **Kuralımız: kodu kopyalamayın, yazın.**

---

# 2. numpy: Diziler (array)

Liste yavaştır ve matematik yapamaz. **numpy dizisi** hızlıdır ve tüm elemanlara aynı anda işlem uygular.

```python
notlar = np.array([70, 55, 80, 45, 90])

print(notlar * 2)        # her elemanı 2 ile çarp
print(notlar + 5)
print(notlar.mean())     # ortalama
print(notlar.max(), notlar.min())
print(notlar > 60)       # True/False dizisi
print(notlar[notlar > 60])  # filtreleme
```

**Soru:** Son satır ne yazdıracak? Önce tahmin edin, sonra çalıştırın.

---

# numpy: Rastgele sayı üretimi

Herkesin **aynı sayıları** görmesi için bir "tohum" (seed) kullanıyoruz.

```python
rng = np.random.default_rng(42)

print(rng.integers(0, 100, size=5))
print(rng.normal(loc=60, scale=15, size=5))
```

- `integers`: her sayı eşit olasılıklı (düz dağılım)
- `normal`: çoğu sayı ortalamaya (`loc`) yakın, azı uzak: **çan eğrisi**

> Aynı seed ile aynı sırada çağırırsanız sonuç herkeste aynıdır. (Öğrenci verisi ise hazır dosyadan gelecek.)

---

# 3. İstatistik: Ortalama

Sınıfın "merkezi" nerede?

**Ortalama (mean)** = tüm notların toplamı / öğrenci sayısı

$$\mu = \frac{x_1 + x_2 + \dots + x_n}{n}$$

```python
notlar = np.array([70, 55, 80, 45, 90])
print(notlar.mean())   # 68.0
```

Ama ortalama tek başına yetmez. Şu iki sınıfın ortalaması da 60:

- Sınıf A: 58, 59, 60, 61, 62 (herkes birbirine yakın)
- Sınıf B: 20, 40, 60, 80, 100 (çok dağınık)

Dağılımı da ölçmemiz lazım.

---

# İstatistik: Standart sapma

**Standart sapma (std)**: notlar ortalamadan ortalama ne kadar uzakta?

1. Her notun ortalamadan farkını al: $x_i - \mu$
2. Karesini al (negatifler kalksın)
3. Bunların ortalamasını al (buna **varyans** denir)
4. Karekökünü al

$$\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{n}}$$

```python
a = np.array([58, 59, 60, 61, 62])
b = np.array([20, 40, 60, 80, 100])
print(a.std(), b.std())   # 1.41 ve 28.28
```

Küçük std = notlar kümelenmiş. Büyük std = notlar dağınık.

---

# İstatistik: Çan eğrisi (normal dağılım)

Çok sayıda öğrencinin notları genelde şöyle dağılır:

- Çoğu öğrenci ortalamanın **yakınında**
- Çok yüksek ve çok düşük notlar **nadir**
- Eğri ortalamaya göre **simetrik**

**%68-%95 kuralı**
- Öğrencilerin yaklaşık **%68'i** ortalamanın ±1 std içinde
- Yaklaşık **%95'i** ±2 std içinde

Bağıl değerlendirme bu fikre dayanır: *"Kaç aldın?"* değil, *"sınıfın neresindesin?"*

---

# std: numpy ve pandas arasındaki fark

| | varsayılan | anlamı |
|---|---|---|
| `np.std(x)` | `ddof=0` | popülasyon (bölen: n) |
| `Series.std()` | `ddof=1` | örneklem (bölen: n-1) |

İkisi **farklı sonuç** verir! Bizim sınıf tüm popülasyon olduğu için:

```python
std = seri.std(ddof=0)
```

Bu eğitimde hep `ddof=0` yazacağız ki herkesin harf notu aynı çıksın.

---

# 4. pandas: DataFrame

**DataFrame** = satırları ve sütunları olan tablo (Excel gibi). Her sütun bir **Series**.

Öğrenci verisi hazır: `ogrenciler.csv` (100 öğrenci). Dosyayı `analiz.py` ile **aynı klasöre** koyun.

| Sütun | Anlamı |
|---|---|
| `ogrenci_no` | öğrenci numarası |
| `ad`, `soyad` | isim |
| `vize`, `final` | 0-100 arası notlar |

---

## Veriyi yükleyelim

```python
df = pd.read_csv("ogrenciler.csv")
print(df.head())
```

**Kontrol:** İlk satır şu olmalı:

```
   ogrenci_no    ad   soyad  vize  final
0     2024482  Onur  Yılmaz  70.0   64.0
```

`read_csv`: CSV dosyasını tabloya çevirir. Gerçek hayatta veri genelde böyle gelir.

---

# pandas: Veriye ilk bakış

```python
print(df.shape)       # (100, 5): 100 satır, 5 sütun
df.info()             # sütun tipleri
print(df.describe())  # count, mean, std, min, %25, %50, %75, max
```

`describe()` tek komutla az önce öğrendiğimiz istatistiklerin hepsini verir.

**Soru:** `vize` sütununun ortalaması kaç? En yüksek `final` notu kaç?

---

# pandas: Sütun seçme

```python
print(df["ad"])               # tek sütun (Series)
print(df[["ad", "vize"]])     # birden çok sütun (DataFrame)
print(df["vize"].mean())      # sütun üzerinde işlem
print(df.head(10))            # ilk 10 satır
```

Tek köşeli parantez `[ ]` = bir sütun.
Çift köşeli parantez `[[ ]]` = sütun listesi.

---

# pandas: Filtreleme

Koşul yazın, True olan satırlar kalır.

```python
# Finalden 35 altı alanlar
print(df[df["final"] < 35])

# Hem vize hem final 80 üstü
print(df[(df["vize"] > 80) & (df["final"] > 80)])
```

- `&` = ve, `|` = veya
- Her koşul **parantez içinde** olmalı

**Alıştırma:** Adı "Zeynep" olan öğrencileri listeleyin. (İpucu: `==`)

---

# pandas'ta başka neler yapabiliriz? (1/3)

*Tanıtım slaytı: ezberlemeyin, bunların var olduğunu bilin. İsteyen deneyebilir.*

## Sıralama

```python
df.sort_values("final", ascending=False).head(3)   # finale göre, büyükten küçüğe
df.sort_values(["soyad", "ad"])                    # önce soyad, sonra ad (A-Z)
```

## Benzersiz değerler ve sayma

```python
df["ad"].unique()                             # hangi isimler var?
df["ad"].nunique()                            # kaç farklı isim? -> 20
df["ad"].value_counts().head(3)               # en sık isimler: Deniz 11, Zeynep 9, Yusuf 8
df[df["ad"].isin(["Ayşe", "Zeynep"])]         # listedeki değerlerden biri olanlar
```

---

# pandas'ta başka neler yapabiliriz? (2/3)

## `.loc`: **etiketle** satır ve sütun seçme

```python
df.loc[0, "ad"]                      # 0 numaralı satır, "ad" sütunu -> "Onur"
df.loc[0:2, ["ad", "final"]]         # satır 0, 1 VE 2 (bitiş DAHİL!)
df.loc[df["final"] > 90, ["ad", "soyad", "final"]]   # koşul + sütun seçimi
```

## `.iloc`: **konumla** seçme

```python
df.iloc[0:3, 1:3]                    # ilk 3 satır, 1. ve 2. sütun (bitiş HARİÇ)
```

> `.loc` = etiket (bitiş dahil), `.iloc` = sıra numarası (bitiş hariç, Python dilimi gibi)

---

# pandas'ta başka neler yapabiliriz? (3/3)

## Değer değiştirme (önce `df.copy()` ile kopya alın!)

```python
kopya = df.copy()
kopya.loc[0, "final"] = 65                    # tek hücreyi değiştir
kopya.loc[kopya["final"] < 30, "final"] = 30  # koşula uyanları değiştir
```

## Sütunları düzenleme ve gruplama

```python
df.rename(columns={"vize": "midterm"})        # yeniden adlandır
df.drop(columns=["ogrenci_no"])               # sütun sil
df[["vize", "final"]].mean()                  # birden çok sütunun ortalaması
df.groupby("ad")["final"].mean()              # isme göre final ortalaması
```

> Not: Çoğu pandas metodu **yeni bir tablo döndürür**, `df`'i değiştirmez. Sonucu bir değişkene atamazsanız kaybolur.

---

# 5. Yeni sütun: Ağırlıklı ortalama

Vize %40, final %60:

```python
VIZE_AGIRLIK = 0.4
FINAL_AGIRLIK = 0.6

df["ortalama"] = df["vize"] * VIZE_AGIRLIK + df["final"] * FINAL_AGIRLIK
print(df.head())
```

Tek satırda 100 öğrencinin hepsi hesaplandı. Döngü yok! (numpy/pandas'ın gücü)

---

# Sıralama: en iyi 5 öğrenci

```python
print(df.sort_values("ortalama", ascending=False).head(5))
```

En yüksek 5 öğrenci kim?

---

# 6. Çan eğrisini çizelim

```python
mu = df["ortalama"].mean()
sigma = df["ortalama"].std(ddof=0)
print(f"Ortalama: {mu:.2f}, std: {sigma:.2f}")
```

Beklenen: `Ortalama: 60.45, std: 10.86`

```python
plt.hist(df["ortalama"], bins=12, edgecolor="black")
plt.title("Sınıf ortalamalarının dağılımı")
plt.xlabel("Ağırlıklı ortalama")
plt.ylabel("Öğrenci sayısı")
plt.show()
```

Çan şekline benziyor mu?

---

# Gerçek çan eğrisini üstüne çizelim

Normal dağılımın formülü (`mu` ve `sigma` ile):

```python
x = np.linspace(0, 100, 200)
pdf = np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

plt.hist(df["ortalama"], bins=12, density=True,
         alpha=0.6, edgecolor="black")
plt.plot(x, pdf, linewidth=2)
plt.axvline(mu, linestyle="--")
plt.show()
```

`density=True`: histogram alanı 1 olsun, eğriyle aynı ölçekte görünsün.

Formülün her parçasını anlamak zorunda değilsiniz. Önemli olan: **eğri sadece `mu` ve `sigma`'ya bağlı.**

---

# 7. z-skoru

*"Bu öğrenci sınıf ortalamasının kaç standart sapma üstünde/altında?"*

$$z = \frac{x - \mu}{\sigma}$$

**Örnek: Zeynep Demir** (vize 61, final 73)
- Ortalaması: 61 × 0.4 + 73 × 0.6 = **68.2**
- Sınıf ortalaması 60.45, std 10.86
- z = (68.2 − 60.45) / 10.86 = **0.71**

Yani Zeynep sınıf ortalamasının 0.71 std üstünde.

- z = 0: tam ortalama
- z = +1: 1 std üstü
- z = −2: 2 std altı

---

# T-skoru

z negatif olabiliyor ve küçük sayılarla çalışmak zor. Bunu daha okunur bir ölçeğe çeviririz:

$$T = 50 + 10 \cdot z$$

- Ortalama öğrenci → **T = 50**
- 1 std üstü → **T = 60**
- 1 std altı → **T = 40**

**Zeynep:** T = 50 + 10 × 0.71 = **57.1**

```python
df["z"] = (df["ortalama"] - mu) / sigma
df["t"] = 50 + 10 * df["z"]
print(df.head())
```

---

# 8. Harf notu tablosu

| T-skoru | Harf |
|---|---|
| ≥ 60 | AA |
| 55 - 59.99 | BA |
| 50 - 54.99 | BB |
| 45 - 49.99 | CB |
| 40 - 44.99 | CC |
| 35 - 39.99 | DC |
| 30 - 34.99 | DD |
| 25 - 29.99 | FD |
| < 25 | FF |

Ek kural: **Finali 35'in altında olan otomatik FF** alır.

---

# Harf notlarını hesaplayalım

```python
sinirlar = [-np.inf, 25, 30, 35, 40, 45, 50, 55, 60, np.inf]
harfler = ["FF", "FD", "DD", "DC", "CC", "CB", "BB", "BA", "AA"]

df["harf"] = pd.cut(df["t"], bins=sinirlar, labels=harfler, right=False)
```

`pd.cut`: sayıları aralıklara böler. `right=False` → alt sınır **dahil**
(T = 60 tam olarak AA olur).

## Otomatik FF kuralı

```python
ALT_FINAL = 35
df.loc[df["final"] < ALT_FINAL, "harf"] = "FF"
```

---

# Sonuçlara bakalım

```python
sira = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FD", "FF"]
print(df["harf"].value_counts().reindex(sira))
```

Beklenen:

```
AA 14   BA 13   BB 32   CB 11   CC 15
DC  7   DD  3   FD  0   FF  5
```

Çan eğrisi gibi: ortada çok, uçlarda az.

```python
zeynep = (df["ad"] == "Zeynep") & (df["soyad"] == "Demir")
print(df[zeynep][["ad", "soyad", "ortalama", "t", "harf"]])
```

Zeynep Demir: **BA** (sınıfta 9 Zeynep var, o yüzden soyadı da filtreledik)

---

# Challenge'lar (süreniz varsa)

1. Kaç öğrenci **kaldı** (FF)? Kimler?
2. T-skoruna göre en yüksek **5 öğrenciyi** ad, soyad, harf ile listeleyin.
3. Vizesi finalinden **20 puan yüksek** olan öğrenciler kimler?
4. Sonuçları dosyaya kaydedin: `df.to_csv("sonuclar.csv", index=False)`
5. **Bonus:** Ağırlıkları %50-%50 yapın. Kimin harfi değişti?

---

# Özet

| Konu | Araç |
|---|---|
| Rastgele sayı | `default_rng`, `rng.normal` |
| Veri yükleme | `pd.read_csv` |
| Tablo | `pd.DataFrame`, `head`, `describe` |
| Seçme / filtreleme | `df["x"]`, `df[df["x"] > 5]` |
| Yeni sütun | `df["yeni"] = ...` |
| İstatistik | `mean`, `std(ddof=0)` |
| Çan eğrisi | `plt.hist`, normal dağılım |
| Bağıl değerlendirme | z-skoru, T = 50 + 10z, `pd.cut` |

**Teşekkürler! Sorular?**
