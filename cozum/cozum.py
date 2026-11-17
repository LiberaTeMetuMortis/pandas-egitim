"""Pandas Eğitimi - Eğitmen çözümü (baştan sona çalışır).

Çalıştırma:  python cozum/cozum.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1) VERİYİ YÜKLE  (veri/uret.py ile üretilmiş hazır dosya)
# ---------------------------------------------------------------
df = pd.read_csv("veri/ogrenciler.csv")

print(df.head())
print(df.shape)

# ---------------------------------------------------------------
# 2) KEŞİF
# ---------------------------------------------------------------
df.info()
print(df.describe())
print(df["vize"].mean(), df["final"].max())

# Seçme ve filtreleme
print(df[["ad", "vize"]].head())
print(df[df["final"] < 35])
print(df[(df["vize"] > 80) & (df["final"] > 80)])

# ---------------------------------------------------------------
# 3) AĞIRLIKLI ORTALAMA (vize %40, final %60)
# ---------------------------------------------------------------
VIZE_AGIRLIK = 0.4
FINAL_AGIRLIK = 0.6
df["ortalama"] = df["vize"] * VIZE_AGIRLIK + df["final"] * FINAL_AGIRLIK
print(df.sort_values("ortalama", ascending=False).head(5))

# ---------------------------------------------------------------
# 4) İSTATİSTİK: ortalama, standart sapma (ddof=0 -> popülasyon)
# ---------------------------------------------------------------
mu = df["ortalama"].mean()
sigma = df["ortalama"].std(ddof=0)
print(f"Sınıf ortalaması: {mu:.2f}, standart sapma: {sigma:.2f}")
# Not: np.std varsayılan ddof=0, pandas .std() varsayılan ddof=1 -> ikisini açıkça yazıyoruz.
assert np.isclose(sigma, np.std(df["ortalama"].to_numpy(), ddof=0))

# ---------------------------------------------------------------
# 5) ÇAN EĞRİSİ
# ---------------------------------------------------------------
x = np.linspace(0, 100, 200)
pdf = np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

plt.hist(df["ortalama"], bins=12, density=True, alpha=0.6, edgecolor="black")
plt.plot(x, pdf, linewidth=2)
plt.axvline(mu, linestyle="--")
plt.title("Sınıf ortalamalarının dağılımı")
plt.xlabel("Ağırlıklı ortalama")
plt.ylabel("Yoğunluk")
plt.savefig("can_egrisi.png", dpi=120)
# plt.show()  # canlı oturumda açın

# ---------------------------------------------------------------
# 6) Z-SKORU ve T-SKORU
# ---------------------------------------------------------------
df["z"] = (df["ortalama"] - mu) / sigma
df["t"] = 50 + 10 * df["z"]

# ---------------------------------------------------------------
# 7) HARF NOTLARI
# ---------------------------------------------------------------
sinirlar = [-np.inf, 25, 30, 35, 40, 45, 50, 55, 60, np.inf]
harfler = ["FF", "FD", "DD", "DC", "CC", "CB", "BB", "BA", "AA"]
df["harf"] = pd.cut(df["t"], bins=sinirlar, labels=harfler, right=False)

# Final ALT_FINAL'in altındaysa otomatik FF
ALT_FINAL = 35
df.loc[df["final"] < ALT_FINAL, "harf"] = "FF"

sira = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FD", "FF"]
print(df["harf"].value_counts().reindex(sira))

# ---------------------------------------------------------------
# 8) CHALLENGE'LAR
# ---------------------------------------------------------------
print("Kalanlar:", (df["harf"] == "FF").sum())
print(df.sort_values("t", ascending=False)[["ad", "soyad", "ortalama", "harf"]].head(5))

df.to_csv("sonuclar.csv", index=False)
