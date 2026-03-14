
rule all:
    input:
        "results/metrics.csv",
        "results/read_length_distribution.png",
        "results/quality_distribution.png",
        "results/gc_content_distribution.png",
        "results/nanostat_report.txt"

rule run_nanostat:
    input:
        "data/barcode77.fastq.gz"
    output:
        "results/nanostat_report.txt"
    shell:
        "NanoStat --fastq {input} -n {output}"

rule analyze_fastq:
    input:
        "data/barcode77.fastq.gz"
    output:
        "results/metrics.csv"
    shell:
        "python scripts/analyze_fastq.py"

rule plot_metrics:
    input:
        "results/metrics.csv"
    output:
        "results/read_length_distribution.png",
        "results/quality_distribution.png",
        "results/gc_content_distribution.png"
    shell:
        "python scripts/plot_metrics.py"