import csv
data_planet=[]
with open("archive_dataset.csv", "r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data_planet.append(row)
headers=data_planet[0]
planet_data=data_planet[1:]
for planets in planet_data:
    planets[2]=planets[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("new_archive.csv", 'a+') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
with open("new_archive.csv") as input, open("new_new_archive.csv", 'w', newline='') as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.rightrow(row)

    
