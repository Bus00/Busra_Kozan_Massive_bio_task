
import gzip
import pandas as pd
import os

# Dosya yolları
fastq_file = "data/barcode77.fastq.gz"
out_csv = "results/metrics.csv"
out_summary = "results/summary_stats.txt"

read_lengths = []
gc_counts = []
qualities = []

# N50 ve Q Skorları için sayaçlar
total_bases = 0
q20_bases = 0
q30_bases = 0

print("FASTQ analizi başlıyor..")

# Klasör yoksa oluşturalım
os.makedirs("results", exist_ok=True)

with gzip.open(fastq_file, "rt") as f:
    while True:
        header = f.readline()
        if not header:
            break

        sequence = f.readline().strip()
        plus = f.readline()
        quality = f.readline().strip()

        seq_len = len(sequence)
        if seq_len == 0:
            continue
            
        read_lengths.append(seq_len)

        # 1. GC İçeriği(%)
        gc = (sequence.count("G") + sequence.count("C")) / seq_len * 100
        gc_counts.append(gc)

        # 2. Kalite Skorları 
        q_scores = [ord(c) - 33 for c in quality]
        qualities.append(sum(q_scores) / seq_len)

        # 3. Q20 ve Q30 Sayımı
        total_bases += seq_len
        q20_bases += sum(1 for q in q_scores if q >= 20)
        q30_bases += sum(1 for q in q_scores if q >= 30)

# N50 HESAPLAMASI 
read_lengths_sorted = sorted(read_lengths, reverse=True)
half_length = sum(read_lengths_sorted) / 2
cumulative_sum = 0
n50 = 0

for length in read_lengths_sorted:
    cumulative_sum += length
    if cumulative_sum >= half_length:
        n50 = length
        break

#  DOĞRULUK ORANI 
avg_q_overall = sum(qualities) / len(qualities)
# Phred to Accuracy formula
overall_accuracy = (1 - 10**(-avg_q_overall/10)) * 100

# Verileri CSV'ye kaydet
df = pd.DataFrame({
    "read_length": read_lengths,
    "gc_content": gc_counts,
    "avg_quality": qualities
})
df.to_csv(out_csv, index=False)

# İSTATİSTİKSEL ÖZET RAPORU
q20_percent = (q20_bases / total_bases) * 100 if total_bases > 0 else 0
q30_percent = (q30_bases / total_bases) * 100 if total_bases > 0 else 0

with open(out_summary, "w") as f:
    f.write("=== Biyoinformatik Kalite Kontrol (QC) Özeti ===\n")
    f.write(f"Toplam Okuma Sayısı: {len(read_lengths):,}\n")
    f.write(f"Toplam Baz Sayısı: {total_bases:,}\n")
    f.write(f"N50 Değeri: {n50} bp\n")
    f.write(f"Ortalama Kalite (Phred): {avg_q_overall:.2f}\n")
    f.write(f"Genel Baz Doğruluğu: %{overall_accuracy:.2f}\n")
    f.write(f"Q20 Yüzdesi: %{q20_percent:.2f} (Hata payı 1/100)\n")
    f.write(f"Q30 Yüzdesi: %{q30_percent:.2f} (Hata payı 1/1000)\n")
    f.write("================================================\n")

print(f"Analiz tamamlandı. Ortalama Doğruluk: %{overall_accuracy:.2f}")