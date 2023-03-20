import csv
import random

# Define possible values for the columns
machine_models = ["a01", "a02", "b01", "b02", "c01", "c02"]
machine_types = ["smart switches", "router"]
country_names = ["india", "usa", "norway", "united kingdom", "vietnam"]
india_delivery_sites = ["vellore", "vit"]
usa_delivery_sites = ["newyork", "california"]
norway_delivery_sites = ["loften"]
uk_delivery_sites = ["london"]
vietnam_delivery_sites = ["vietnam-city"]
software_versions = ["sw101", "sw202", "sw303"]

# Open the main CSV file for writing
with open("switches.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["machine model", "machine type", "country name", "delivery date", "delivery site", "price", "software version"])

    # Open additional CSV files for writing
    india_file = open("india.csv", "w", newline="")
    india_writer = csv.writer(india_file)
    india_writer.writerow(["machine model", "machine type", "delivery date", "delivery site", "price", "software version"])

    uk_file = open("united_kingdom.csv", "w", newline="")
    uk_writer = csv.writer(uk_file)
    uk_writer.writerow(["machine model", "machine type", "delivery date", "delivery site", "price", "software version"])

    vietnam_file = open("vietnam.csv", "w", newline="")
    vietnam_writer = csv.writer(vietnam_file)
    vietnam_writer.writerow(["machine model", "machine type", "delivery date", "delivery site", "price", "software version"])

    # Generate and write 100 random records to the main CSV file
    for i in range(1000):
        # Choose random values for each column
        machine_model = random.choice(machine_models)
        machine_type = random.choice(machine_types)
        country_name = random.choice(country_names)
        delivery_site = ""
        delivery_date = f"{random.randint(1, 31)}/{'0' if random.randint(0, 1) == 0 else ''}{random.randint(1, 3)}/2023"
        #delivery_date = f"2023-{random.randint(1,3):02d}-{random.randint(1,31):02d}" # Choose a random date in January-March 2023
        price = random.randint(400, 600)
        software_version = random.choice(software_versions)

        if country_name == "india":
            delivery_site = random.choice(india_delivery_sites)
            india_writer.writerow([machine_model, machine_type, delivery_date, delivery_site, price,software_version])
        elif country_name == "usa":
            delivery_site = random.choice(usa_delivery_sites)
        elif country_name == "norway":
            delivery_site = random.choice(norway_delivery_sites)
        elif country_name == "united kingdom":
            delivery_site = random.choice(uk_delivery_sites)
            uk_writer.writerow([machine_model, machine_type, delivery_date, delivery_site, price,software_version])
        elif country_name == "vietnam":
            delivery_site = random.choice(vietnam_delivery_sites)
            vietnam_writer.writerow([machine_model, machine_type, delivery_date, delivery_site,price, software_version])

        writer.writerow([machine_model, machine_type, country_name, delivery_date, delivery_site, price, software_version])




#for machine.csv
models = ['a01', 'a02', 'b01', 'b02', 'c01', 'c02']
types = ['smartswitches', 'routers']
faults = ['maintenance', 'emergency', 'service', 'risky fault']
parts = ['rom', 'ram', 'port']

with open('machine.csv', mode='w', newline='') as csv_file:
    fieldnames = ['machine model', 'machine type', 'fault type', 'fault date', 'part name', 'part price', 'service status']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(400):
        model = random.choice(models)
        machine_type = random.choice(types)
        fault_type = random.choice(faults)
        fault_date = f"{random.randint(1, 31)}/{'0' if random.randint(0, 1) == 0 else ''}{random.randint(1, 3)}/2023"
        part_name = random.choice(parts)
        part_price = random.randint(50, 100)
        service_status = random.choice(['in-service', 'out-of-service'])

        writer.writerow({'machine model': model, 'machine type': machine_type, 'fault type': fault_type,
                         'fault date': fault_date, 'part name': part_name, 'part price': part_price,
                         'service status': service_status})
