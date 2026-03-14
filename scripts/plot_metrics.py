
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Grafikler oluşturuluyor..")

df = pd.read_csv("results/metrics.csv")
os.makedirs("results", exist_ok=True)

# seaborn 
sns.set_theme(style="whitegrid")

# okuma Uzunluğu Dağılımı (Read Length)
plt.figure(figsize=(10, 6))
sns.histplot(df["read_length"], bins=50, color="skyblue", kde=True)
plt.title("Okuma Uzunluğu Dağılımı (Read Length Distribution)", fontsize=14)
plt.xlabel("Okuma Uzunluğu (bp)")
plt.ylabel("Frekans (Okuma Sayısı)")
plt.savefig("results/read_length_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# kalite Dağılımı (Quality Score)
plt.figure(figsize=(10, 6))
sns.histplot(df["avg_quality"], bins=50, color="salmon", kde=True)
plt.axvline(x=20, color='red', linestyle='--', label='Q20 Sınırı') # Q20 çizgisini gösterelim
plt.title("Kalite Skoru Dağılımı (Quality Score Distribution)", fontsize=14)
plt.xlabel("Ortalama Kalite Skoru (Phred)")
plt.ylabel("Frekans")
plt.legend()
plt.savefig("results/quality_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# GC içeriği dağılımı (GC Content)
plt.figure(figsize=(10, 6))
sns.histplot(df["gc_content"], bins=50, color="olive", kde=True)
plt.title("GC İçeriği Dağılımı (GC Content Distribution)", fontsize=14)
plt.xlabel("GC Yüzdesi (%)")
plt.ylabel("Frekans")
plt.savefig("results/gc_content_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

print("Tüm grafikler başarıyla oluşturuldu.")

# özet istatistikler
print("\n=== TEMEL ÖZET İSTATİSTİKLER (ORTALAMA VE MEDYAN) ===")
print(f"Okuma Uzunluğu -> Ortalama: {df['read_length'].mean():.2f} bp, Medyan: {df['read_length'].median():.2f} bp")
print(f"GC İçeriği     -> Ortalama: {df['gc_content'].mean():.2f}%, Medyan: {df['gc_content'].median():.2f}%")
print(f"Kalite Skoru   -> Ortalama: {df['avg_quality'].mean():.2f}, Medyan: {df['avg_quality'].median():.2f}")
print("=====================================================\n")