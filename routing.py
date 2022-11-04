from email.policy import default
import googlemaps
import requests
from datetime import timedelta


class routing:
    def get_tm(origin,destination):
        url = 'https://restapi.amap.com/v3/direction/driving?'
        key = 'ae4bb43cb695f854153222270cc1cb86'
        link = '{}origin={}&destination={}&key={}'.format(url,origin,destination,key)
        response = requests.get(link)
        dis,tm = 999999, 999999
        if response.status_code == 200:
            results = response.json()
            if results['status'] == '1':
                tm = int(results['route']['paths'][0]['duration'])
            else:
                print(link)
        tm = timedelta(seconds = tm)
        return tm  

    def create_path(start,end):
        gmaps = googlemaps.Client(key='AIzaSyBh6eU48AhR1wiYNWyGxXKn23N4sIAc6ek')
        start_location = '澳門'+str(start)
        end_location = '澳門' + str(end)
        start_encode = gmaps.geocode(start_location)
        end_encode = gmaps.geocode(end_location)
        start_coordinate_lat = start_encode[0]['geometry']['location']['lat']
        start_coordinate_lat = "{:.6f}".format(start_coordinate_lat)
        start_coordinate_lng = start_encode[0]['geometry']['location']['lng']
        start_coordinate_lng = "{:.6f}".format(start_coordinate_lng)
        start_coordinate = '{},{}'.format(start_coordinate_lng, start_coordinate_lat)
        end_coordinate_lat = end_encode[0]['geometry']['location']['lat']
        end_coordinate_lat = "{:.6f}".format(end_coordinate_lat)
        end_coordinate_lng = end_encode[0]['geometry']['location']['lng']
        end_coordinate_lng = "{:.6f}".format(end_coordinate_lng)
        end_coordinate = '{},{}'.format(end_coordinate_lng, end_coordinate_lat)
        duration = routing.get_tm(start_coordinate,end_coordinate)
        path = {'start':start,'end':end,'duration':duration}
        return path