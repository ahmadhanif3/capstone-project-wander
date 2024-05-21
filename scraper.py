import time
import pandas as pd
import googlemaps

    
API_KEY = '<Your API KEY>' # Provide API Key, hardcode it to simplify. Not included, for private use
while True:
    try:
        map_client = googlemaps.Client(API_KEY)
        map_client.geocode('New York')
        print("API Key is valid\n")
        break
    except ValueError:
        print("Invalid API key provided")
    API_KEY = input("Please enter a valid Google Maps API key: ")

running = True

while(running):
    option = '0'
    while option not in ['1', '2']:
        option = input('Choose starting location option (1 or 2)' +
                      '\n1. Location (city, places)' +
                      '\n2. Coordinate (latitude & longtitude)' +
                      '\nChoice: ')
        print()
      
    if (option == '1'):
        address = input('Input address of place or city: ')
        geocode = map_client.geocode(address=address)
        if geocode:
            location = (geocode[0]['geometry']['location']['lat'],
                        geocode[0]['geometry']['location']['lng'])
    else:
        location = tuple(float(coord) for coord in input('Input as follows -> lat, long. ex: -32.121, -32.121\nCoordinates: ').split(','))
    print()

    search_string = input('Search string: ')
    print()
    distance = int(input('Radius in meters: '))
    print()
    business_list = []

    response = map_client.places_nearby(
        location=location,
        keyword=search_string,
        radius=distance
    )   

    business_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

    while next_page_token:
        time.sleep(2)
        response = map_client.places_nearby(
            location=location,
            keyword=search_string,
            radius=distance,
            page_token=next_page_token
        )   
        business_list.extend(response.get('results'))
        next_page_token = response.get('next_page_token')
    
    df = pd.DataFrame(business_list)
    df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
    file_name = input('Input file-name for <file-name>.xlsx (no whitespace, only - & _): ')
    df.to_excel(f'{file_name}.xlsx', index=False)
    print(f'Exported as {file_name}.xlsx')

    running = input('Continue? (y/n): ').lower() == 'y'