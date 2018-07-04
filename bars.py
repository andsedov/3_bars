import json
import sys
from geopy.distance import great_circle


def load_bars_json(filepath):
    with open(filepath, encoding='utf-8') as file_object:
        return json.load(file_object)


def get_biggest_bar(bars_json):
    return max(bars_json["features"],
               key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(bars_json):
    return min(bars_json["features"],
               key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])


def get_closest_bar(bars_json, longitude, latitude):
    longitude_init = bars_json['features'][0]['geometry']['coordinates'][0]
    latitude_init = bars_json['features'][0]['geometry']['coordinates'][1]
    closest_bar_name = ''
    init_point = (latitude_init, longitude_init)
    user_point = (latitude, longitude)
    distance_min = great_circle(init_point, user_point).meters

    for bar in bars_json['features']:
        bar_name = bar['properties']['Attributes']['Name']
        bar_longitude = bar['geometry']['coordinates'][0]
        bar_latitude = bar['geometry']['coordinates'][1]
        bar_point = (bar_latitude, bar_longitude)
        distance = great_circle(bar_point, user_point).meters
        if distance < distance_min:
            distance_min = distance
            closest_bar_name = bar_name
        else:
            continue
    return closest_bar_name, round(distance_min / 1000, 2)

def format_bars_data(bars_json):
    return "{} with {} seats".format(
        bars_json['properties']['Attributes']['Name'],
        bars_json['properties']['Attributes']['SeatsCount'])


if __name__ == '__main__':
    filepath = 'bars.json'
    bars_json = load_bars_json(sys.argv[1])
    print('The biggest bar:', format_bars_data(get_biggest_bar(bars_json)))
    print('The smallest bar:', format_bars_data(get_smallest_bar(bars_json)))
    longitude = float(input('Enter longitude: '))
    latitude = float(input('Enter latitude: '))
    closest_bar = get_closest_bar(bars_json, longitude, latitude)
    print('The closest bar:', closest_bar, 'meters')

