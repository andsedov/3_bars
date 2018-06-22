import json
from math import sin, cos, sqrt, atan2


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_object:
        return json.load(file_object)


def get_biggest_bar(data):
    seats_count_max = 0
    seats_count_max_bar_name = ''
    for item in data['features']:
        seats_count = item['properties']['Attributes']['SeatsCount']
        bar_name = item['properties']['Attributes']['Name']
        if seats_count > seats_count_max:
            seats_count_max = seats_count
            seats_count_max_bar_name = bar_name
        else:
            continue
    return seats_count_max_bar_name, seats_count_max


def get_smallest_bar(data):
    seats_count_min_bar_name, seats_count_min = get_biggest_bar(data)
    for item in data['features']:
        seats_count = item['properties']['Attributes']['SeatsCount']
        bar_name = item['properties']['Attributes']['Name']
        if seats_count < seats_count_min:
            seats_count_min = seats_count
            seats_count_min_bar_name = bar_name
        else:
            continue
    return seats_count_min_bar_name, seats_count_min


def get_distance(longitude_1, latitude_1, longitude_2, latitude_2):
    R = 6373.0
    dlon = longitude_2 - longitude_1
    dlat = latitude_2 - longitude_1
    a = (sin(dlat/2))**2+cos(latitude_1)*cos(latitude_2)*(sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def get_closest_bar(data, longitude, latitude):
    longitude_init = data['features'][0]['geometry']['coordinates'][0]
    latitude_init = data['features'][0]['geometry']['coordinates'][1]
    closest_bar_name = ''
    distance_min = get_distance(longitude, latitude, longitude_init, latitude_init)
    for item in data['features']:
        bar_name = item['properties']['Attributes']['Name']
        bar_longitude = item['geometry']['coordinates'][0]
        bar_latitude = item['geometry']['coordinates'][1]
        distance = get_distance(bar_longitude, bar_latitude, longitude_init, latitude_init)
        if distance < distance_min:
            distance_min = distance
            closest_bar_name = bar_name
        else:
            continue
    return closest_bar_name, round(distance_min, 2)


if __name__ == '__main__':
    data = load_data('bars.json')
    print('The biggest bar:', get_biggest_bar(data))
    print('The smallest bar:', get_smallest_bar(data))
    longitude = float(input('Enter longitude: '))
    latitude = float(input('Enter latitude: '))
    try:
        print('The closest bar:', get_closest_bar(data, longitude, latitude))
    except:
        print('Coordinates are not valid')
