import GpuScraper
import db

if __name__ == "__main__":
    GpuScraper.get_data()
    db.generate_database()
