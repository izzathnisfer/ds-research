import json
import csv
import os

keywords = ['vehicle', 'transport', 'motor', 'energy', 'fuel', 'petroleum', 'electricity', 'power', 'emission']

with open('found-data-sets/all.json', 'r') as f:
    data = json.load(f)

# Determine the items to iterate over
if isinstance(data, dict):
    # If the root is a dict, maybe keys are dataset IDs
    items = []
    for k, v in data.items():
        v['_file_key'] = k
        items.append(v)
elif isinstance(data, list):
    items = data
else:
    print("Unknown JSON structure")
    items = []

count = 0
for info in items:
    cat = str(info.get('category', ''))
    sub_cat = str(info.get('sub_category', ''))
    source = str(info.get('source_id', ''))
    file_key = str(info.get('_file_key', ''))
    
    text_to_search = (cat + " " + sub_cat + " " + file_key).lower()
    
    if any(k in text_to_search for k in keywords):
        if not info.get('cleaned_data'):
            continue
            
        dataset_name = file_key if file_key else f"{source} {cat} {sub_cat}"
        safe_name = "".join([c if c.isalnum() else "_" for c in dataset_name])
        safe_name = safe_name.strip('_').replace('__', '_').replace('___', '_')
        csv_file = f"found-data-sets/{safe_name}.csv"
        
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'Value', 'Category', 'SubCategory', 'Source'])
            for date, val in info['cleaned_data'].items():
                writer.writerow([date, val, cat, sub_cat, source])
                
        print(f"Saved: {csv_file} ({dataset_name}) - Category: {cat}, Sub: {sub_cat}")
        count += 1

print(f"Total datasets saved: {count}")
