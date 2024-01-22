from GpuScraper import benchmarks
import csv

columns = ["GPU", "1080p Ultra", "1440p Ultra", "4k Ultra"]
filename = "GPU_specs.csv"

def generate_database():
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(columns)
        csvwriter.writerows(item for item in benchmarks)
