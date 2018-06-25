import json
from geopy.distance import great_circle


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_object:
        return json.load(file_object)


def get_dict_bar(data):
    bar_dict = {}
    for bar in data['features']:
        bar_dict[bar['properties']['Attributes']['Name']] = bar['properties']['Attributes']['SeatsCount']
    return bar_dict


def get_biggest_bar(data):
    bar_dict = get_dict_bar(data)
    biggest_bar = max(bar_dict, key=bar_dict.get)
    return biggest_bar


def get_smallest_bar(data):
    bar_dict = get_dict_bar(data)
    smallest_bar = min(bar_dict, key=bar_dict.get)
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    longitude_init = data['features'][0]['geometry']['coordinates'][0]
    latitude_init = data['features'][0]['geometry']['coordinates'][1]
    closest_bar_name = ''
    distance_min = great_circle((latitude, longitude), (latitude_init, longitude_init)).meters

    for bar in data['features']:
        bar_name = bar['properties']['Attributes']['Name']
        bar_longitude = bar['geometry']['coordinates'][0]
        bar_latitude = bar['geometry']['coordinates'][1]
        distance = great_circle((bar_latitude, bar_longitude), (latitude, longitude)).meters
        if distance < distance_min:
            distance_min = distance
            closest_bar_name = bar_name
        else:
            continue
    return closest_bar_name, round(distance_min / 1000, 2)


if __name__ == '__main__':
    bar_data = load_data('bars.json')
    print('The biggest bar:', get_biggest_bar(bar_data))
    print('The smallest bar:', get_smallest_bar(bar_data))
    longitude = float(input('Enter longitude: '))
    latitude = float(input('Enter latitude: '))
    try:
        print('The closest bar:', get_closest_bar(bar_data, longitude, latitude))
    except Exception:
        print('Coordinates are not valid')
