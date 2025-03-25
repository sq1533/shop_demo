import json

with open(file="../storage/data/products.json", mode="r", encoding="utf-8") as f:
    product = json.load(fp=f)