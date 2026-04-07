import json

keywords = ['vehicle', 'transport', 'motor', 'energy', 'fuel', 'petroleum', 'electricity', 'power', 'emission']

with open('found-data-sets/summary.json', 'r') as f:
    data = json.load(f)

print("Matches found:")
for key, info in data.items():
    text_to_search = (str(info.get('category', '')) + " " + str(info.get('sub_category', '')) + " " + key).lower()
    if any(k in text_to_search for k in keywords):
        print(f"ID: {key}")
        print(f"  Category: {info.get('category')}")
        print(f"  Sub-category: {info.get('sub_category')}")
        print(f"  Source: {info.get('source_id')}")
        print("-" * 40)
