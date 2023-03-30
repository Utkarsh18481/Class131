import plotly.express as px
import csv

rows = []

with open("new.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

header = rows[0]
planet_data_rows = rows[1:]
print(header)
print(planet_data_rows[0])

header[0] = "row_number"
solar_system_planet_count = ""
for data in planet_data_rows:
    if solar_system_planet_count.get(data[11]):
        solar_system_planet_count[data[11]]+= 1
    else:
        solar_system_planet_count[data[11]] = 1

for planet_data in planet_data_rows:
    planet_mass = planet_data[3]
    if planet_mass.lower()=="unknown":
        planet_data_rows.remove(planet_data)
        continue
    else: 
        planet_mass_value = planet_mass.split(" ")[0]
        planet_mass_ref = planet_mass.split(" ")[1]
        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8
        planet_data[3] = planet_mass_value
    planet_radius = planet_data[7]
    if planet_radius.lower()=="unknown":
        planet_data_rows.remove(planet_data)
        continue
    else: 
        planet_radius_value = planet_radius.split(" ")[0]
        planet_radius_ref = planet_radius.split(" ")[2]
        if planet_radius_ref == "Jupiters":
            planet_radius_value = float(planet_radius_value) * 11.2
        planet_data[7] = planet_radius_value

planet_masses = []
planet_radiuses = []
planet_names = []

for planet_data in planet_data_rows:
    planet_masses.append(planet_data[3])
    planet_radiuses.append(planet_data[7])
    planet_names.append(planet_data[1])
    planet_gravity = []
for index, name in enumerate(planet_names):
    gravity = (float(planet_masses[index])* 5.9) / (float(planet_radiuses[index])* float(planet_radiuses[index]) * 637100 * 637100) * 6.674e-11
    planet_gravity.append(gravity)
fig = px.scatter(x = planet_radiuses, y = planet_masses, size = planet_gravity)
fig.show()
