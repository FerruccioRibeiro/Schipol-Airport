from pathlib import Path

BASE_URL = "https://api.schiphol.nl/public-flights/"
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "processed"