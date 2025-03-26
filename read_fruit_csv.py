import csv

with open('DATA/fruit_data.csv') as fruit_in:
    rdr = csv.reader(fruit_in)
    header = next(rdr)
    for fruit, unit, price in rdr:
        price = float(price)
        print(f"{fruit:12s} {unit:8s} {price:5.2f}")

print('-' * 60)

with open('DATA/fruit_data.csv') as fruit_in:
    headers = next(fruit_in).rstrip().split(',')
    print(f"{headers = }")
    
    rdr = csv.DictReader(fruit_in, fieldnames=headers)
    for row in rdr:
        row['price'] = float(row['price'])
        print(f"{row['fruit']:12s} {row['unit']:8s} {row['price']:5.2f}")