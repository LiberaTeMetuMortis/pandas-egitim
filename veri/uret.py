"""Eğitmen aracı: ogrenciler.csv dosyasını üretir (öğrencilere VERİLMEZ, sadece CSV verilir).

Çalıştırma:  python veri/uret.py
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 100

isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Mustafa", "Zeynep", "Elif",
           "Emre", "Burak", "Deniz", "Selin", "Can", "Ece", "Kerem", "Defne",
           "Yusuf", "Merve", "Berk", "Ceren", "Onur"]
soyisimler = ["Yılmaz", "Kaya", "Demir", "Şahin", "Çelik", "Yıldız", "Aydın",
              "Özdemir", "Arslan", "Doğan", "Kılıç", "Aslan", "Çetin", "Koç",
              "Kurt", "Özkan", "Şimşek", "Polat", "Erdoğan", "Güneş"]

df = pd.DataFrame({
    "ogrenci_no": rng.choice(np.arange(2024001, 2024501), size=n, replace=False),
    "ad": rng.choice(isimler, size=n),
    "soyad": rng.choice(soyisimler, size=n),
    "vize": np.clip(rng.normal(loc=60, scale=15, size=n), 0, 100).round(),
    "final": np.clip(rng.normal(loc=60, scale=15, size=n), 0, 100).round(),
})

df.to_csv("veri/ogrenciler.csv", index=False)
print(df.head())
