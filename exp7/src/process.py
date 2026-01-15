import pandas as pd

df = pd.read_csv("data/raw_data.csv")
df["y"] = df["y"] + 1  # simple cleaning/transformation
df.to_csv("data/processed_data.csv", index=False)
print("Processed dataset saved.")


