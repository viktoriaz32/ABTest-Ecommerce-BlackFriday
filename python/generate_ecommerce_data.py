import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Define Desktop path (change this if your username or OS is different)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# ==============================
# 1. Generate Orders Table
# ==============================

num_orders = 2745
start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 12, 31)
num_customers = 500
num_products = 40

dates = []
for _ in range(num_orders):
    if random.random() < 0.11:
        bf_date = start_date + timedelta(days=54 + random.randint(0, 4)) # Nov 24-28
        dates.append(bf_date)
    else:
        delta_days = (end_date - start_date).days
        random_day = start_date + timedelta(days=random.randint(0, delta_days))
        dates.append(random_day)
dates.sort()

order_ids = [22001 + i for i in range(num_orders)]
customer_ids = [f'C{str(random.randint(1, num_customers)).zfill(4)}' for _ in range(num_orders)]
product_ids = [f'P{str(random.randint(1, num_products)).zfill(4)}' for _ in range(num_orders)]
quantities = [random.choices([1,2,3,4], [0.6,0.25,0.1,0.05])[0] for _ in range(num_orders)]
unit_prices = [round(random.uniform(10, 80), 2) for _ in range(num_orders)]
is_black_friday = [d >= datetime(2024, 11, 24) and d <= datetime(2024, 11, 28) for d in dates]
discounts = [0.10 if bf else 0.0 for bf in is_black_friday]
order_status = ['Completed'] * num_orders
order_values = [round(q * up * (1-d), 2) for q, up, d in zip(quantities, unit_prices, discounts)]

df_orders = pd.DataFrame({
    'OrderID': order_ids,
    'OrderDate': [d.strftime('%Y-%m-%d') for d in dates],
    'CustomerID': customer_ids,
    'ProductID': product_ids,
    'Quantity': quantities,
    'UnitPrice': unit_prices,
    'Discount': discounts,
    'OrderValue': order_values,
    'OrderStatus': order_status,
    'IsBlackFriday': ['Yes' if bf else 'No' for bf in is_black_friday]
})

df_orders.to_csv(os.path.join(desktop_path, 'supplement_ecommerce_orders.csv'), index=False)

# ==============================
# 2. Generate Customer Table
# ==============================

unique_customer_ids = sorted(df_orders['CustomerID'].unique())
num_dim_customers = len(unique_customer_ids)
first_names = ['Anna', 'Jan', 'Lucia', 'Pierre', 'Maria', 'Tomas', 'Laura', 'Jakub', 'Elena', 'Sven', 'Pavel', 'Nina', 'Sara', 'Markus', 'Jana']
last_names = ['Svensson', 'Novak', 'Bianchi', 'Dupont', 'Kowalska', 'Hansen', 'Ivanov', 'Horvat', 'Petrov', 'Müller', 'Rossi', 'Dimitrov', 'Silva', 'Nowak', 'Smith']
regions = ['Sweden', 'Czechia', 'Italy', 'France', 'Poland', 'Denmark', 'Bulgaria', 'Croatia', 'Germany', 'Portugal', 'Slovakia', 'Hungary', 'Spain', 'Norway', 'Finland']

registration_dates = []
for cid in unique_customer_ids:
    customer_orders = df_orders[df_orders['CustomerID'] == cid]
    first_order_date = pd.to_datetime(customer_orders['OrderDate'].min())
    reg_date = first_order_date - timedelta(days=random.randint(10, 700))
    registration_dates.append(reg_date.strftime('%Y-%m-%d'))

segment = []
is_repeat_buyer = []
for cid in unique_customer_ids:
    customer_orders = df_orders[df_orders['CustomerID'] == cid]
    if len(customer_orders) > 1:
        segment.append('Repeat Buyer')
        is_repeat_buyer.append('Yes')
    else:
        segment.append('New Buyer')
        is_repeat_buyer.append('No')

np.random.seed(2)
names = [random.choice(first_names) + ' ' + random.choice(last_names) for _ in range(num_dim_customers)]
customer_regions = [random.choice(regions) for _ in range(num_dim_customers)]

df_customers = pd.DataFrame({
    'CustomerID': unique_customer_ids,
    'Name': names,
    'Region': customer_regions,
    'RegistrationDate': registration_dates,
    'Segment': segment,
    'IsRepeatBuyer': is_repeat_buyer
})

df_customers.to_csv(os.path.join(desktop_path, 'supplement_ecommerce_customers.csv'), index=False)

# ==============================
# 3. Generate Product Table
# ==============================

categories = ['Protein', 'Vitamins', 'Pre-workout', 'Amino Acids', 'Creatine', 'Weight Management', 'Performance']
supplier_ids = [f'S{str(i).zfill(3)}' for i in range(1, 11)]

product_rows = []
np.random.seed(3)
for i in range(1, 41):
    pid = f'P{str(i).zfill(4)}'
    name = f"{random.choice(['Ultra', 'Pure', 'Max', 'Active', 'Fit', 'Power', 'Daily', 'Pro'])} " \
           f"{random.choice(['Whey', 'Protein', 'Omega', 'Vita', 'Amino', 'Creatine', 'Burn', 'Boost'])} {random.choice(['1kg', 'Capsules', '500g', 'Drink', 'Mix', 'Pack'])}"
    category = random.choice(categories)
    supplier_id = random.choice(supplier_ids)
    cost_price = round(np.random.uniform(6, 25), 2)
    retail_price = round(cost_price * np.random.uniform(1.5, 2.5), 2)
    is_promo = 'Yes' if random.random() < 0.8 else 'No'
    product_rows.append([pid, name, category, supplier_id, cost_price, retail_price, is_promo])

df_products = pd.DataFrame(product_rows, columns=[
    'ProductID', 'ProductName', 'Category', 'SupplierID', 'CostPrice', 'RetailPrice', 'IsPromoProduct'
])

df_products.to_csv(os.path.join(desktop_path, 'supplement_ecommerce_products.csv'), index=False)

# ==============================
# 4. Generate Suppliers Table
# ==============================

countries = ['Denmark', 'Germany', 'Sweden', 'Italy', 'France', 'Czechia', 'Netherlands', 'Austria', 'Poland', 'Finland']
category_supplied = [random.choice(categories) for _ in range(10)]
supplier_names = [f"{random.choice(['Nordic', 'Vita', 'Active', 'Health', 'Pure', 'Global', 'Elite', 'Euro'])}"
                  f"{random.choice(['Supps', 'World', 'Lab', 'Group', 'Foods', 'Fit', 'Care', 'Nutri'])}"
                  for _ in range(10)]
supplier_rows = [
    [supplier_ids[i], supplier_names[i], countries[i], category_supplied[i]]
    for i in range(10)
]
df_suppliers = pd.DataFrame(supplier_rows, columns=[
    'SupplierID', 'SupplierName', 'Country', 'CategorySupplied'
])

df_suppliers.to_csv(os.path.join(desktop_path, 'supplement_ecommerce_suppliers.csv'), index=False)

# ==============================
# 5. Generate Campaigns Table
# ==============================

campaign_data = [
    ['BF2024', 'Black Friday', '2024-11-24', '2024-11-28', 'BF2024', 10, 'Yes'],
    ['XMAS2024', 'Xmas Promo', '2024-12-20', '2024-12-24', 'XMAS24', 15, 'No'],
    ['SPRING24', 'Spring Launch', '2024-10-15', '2024-10-22', 'SPR24', 12, 'No'],
    ['HALLOWEEN24', 'Halloween Flash', '2024-10-29', '2024-10-31', 'HW24', 7, 'No'],
]
df_campaigns = pd.DataFrame(campaign_data, columns=[
    'CampaignID', 'Name', 'StartDate', 'EndDate', 'PromoCode', 'DiscountPercent', 'IsBlackFriday'
])

df_campaigns.to_csv(os.path.join(desktop_path, 'supplement_ecommerce_campaigns.csv'), index=False)

# ==============================
# 6. Generate Date Table
# ==============================

date_range = pd.date_range(start='2024-10-01', end='2024-12-31', freq='D')
date_table = []
for date in date_range:
    is_holiday = 'Yes' if date.strftime('%m-%d') in ['12-24', '12-25', '12-26', '10-31'] else 'No'
    is_black_friday = 'Yes' if date >= pd.Timestamp('2024-11-24') and date <= pd.Timestamp('2024-11-28') else 'No'
    date_table.append([
        date.strftime('%Y-%m-%d'),
        date.day,
        date.month,
        date.year,
        f"Q{((date.month-1)//3)+1}",
        date.isocalendar()[1],
        is_holiday,
        is_black_friday
    ])
df_date = pd.DataFrame(date_table, columns=[
    'Date', 'Day', 'Month', 'Year', 'Quarter', 'Week', 'IsHoliday', 'IsBlackFriday'
])

df_date.to_csv(os.path.join(desktop_path, 'supplement_ecommerce_date.csv'), index=False)

# ==============================
# 7. Generate Inventory Table
# ==============================

np.random.seed(4)
inv_rows = []
for i in range(1, 41):
    pid = f'P{str(i).zfill(4)}'
    stock_level = random.randint(10, 500)
    last_update = '2024-12-31'
    expiry_date = (datetime(2025, 1, 1) + timedelta(days=random.randint(30, 400))).strftime('%Y-%m-%d')
    inv_rows.append([pid, stock_level, last_update, expiry_date])
df_inventory = pd.DataFrame(inv_rows, columns=[
    'ProductID', 'StockLevel', 'LastUpdate', 'ExpiryDate'
])

df_inventory.to_csv(os.path.join(desktop_path, 'supplement_ecommerce_inventory.csv'), index=False)

# ==============================
# 8. Generate Product Affinity Table
# ==============================

affinity_rows = []
order_groups = df_orders.groupby('OrderID')
for oid, group in order_groups:
    products = group['ProductID'].tolist()
    if len(products) > 1:
        for i in range(len(products)):
            for j in range(i + 1, len(products)):
                affinity_rows.append([oid, products[i], products[j], 'Yes'])
df_affinity = pd.DataFrame(affinity_rows, columns=[
    'OrderID', 'ProductID_A', 'ProductID_B', 'BoughtTogether'
])
for _ in range(150):
    oid = random.choice(df_orders['OrderID'])
    prod_a, prod_b = random.sample(list(df_products['ProductID']), 2)
    if not ((df_affinity['OrderID'] == oid) & (df_affinity['ProductID_A'] == prod_a) & (df_affinity['ProductID_B'] == prod_b)).any():
        df_affinity = df_affinity.append({
            'OrderID': oid,
            'ProductID_A': prod_a,
            'ProductID_B': prod_b,
            'BoughtTogether': 'No'
        }, ignore_index=True)

df_affinity.to_csv(os.path.join(desktop_path, 'supplement_ecommerce_product_affinity.csv'), index=False)