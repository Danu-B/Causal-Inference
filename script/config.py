from pathlib import Path

class Config:
  RANDOM_SEED = 90
  ASSETS_PATH = Path("../")
  REPO = "~/Users/Danayt/Causal-Inference"
  DATASET_FILE_PATH = "data/data.csv"
  DATASET_PATH = ASSETS_PATH / "data"
