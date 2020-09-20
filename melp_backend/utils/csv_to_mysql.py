import csv
from melp_backend.restaurants.models import Restaurant
from melp_backend import db

with open('../static/files/restaurantes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue

        id = row[0]
        rating = int(row[1])
        name = row[2]
        site = row[3]
        email = row[4]
        phone = row[5]
        street = row[6]
        city = row[7]
        state = row[8]
        lat = float(row[9])
        lng = float(row[10])

        new_restaurant = Restaurant(rating, name, site, email, phone, street,
                                    city, state, lat, lng, id)
        db.session.add(new_restaurant)
        db.session.commit()
        line_count += 1
    print(f'Processed {line_count} lines.')
