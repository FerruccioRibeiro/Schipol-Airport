from extract import get_airlines, get_aircraft_types, get_destinations, get_flights
from salvar import salvar
from transformar import transformar_airlines, transformar_aircrafttypes, transformar_destinations, transformar_flights
from constances import OUTPUT_DIR

def main_etl():
    #Extract
    # airlines_pages = get_airlines()
    # aircarfttypes_pages = get_aircraft_types()
    # destinations_pages = get_destinations()
    flights_pages = get_flights()

    #Transform
    # airlines = transformar_airlines(airlines_pages)
    # aircrafttypes = transformar_aircrafttypes(aircarfttypes_pages)
    # destinations = transformar_destinations(destinations_pages)
    flights = transformar_flights(flights_pages)

    #Load
    salvar(
        OUTPUT_DIR,
        [
            # airlines
            # , aircrafttypes
            # , destinations
            # , 
            flights
        ],
        [
            # 'airlines'
            # , 'aircrafttypes'
            # , 'destinations'
            # , 
            'flights'
        ]
    )


if __name__=='__main__':
    main_etl()

    #import ipdb; ipdb.set_trace()