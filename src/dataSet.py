import json

with open(file="../storage/data/products.json", mode="r", encoding="utf-8") as item:
    product = json.load(fp=item)

with open(file="../storage/data/user.json", mode="r", encoding="utf-8") as user:
    user = json.load(fp=user)