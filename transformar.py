from datetime import datetime, timezone


fuso_utc = timezone.utc

def converte_datas(data):
    try:
        resultado = datetime.strptime(data,'%Y-%m-%dT%H:%M:%S.%f%z').astimezone(fuso_utc)
    except:
        resultado = None

def transformar_airlines(airlines_paginas):

    resultados = []
    airlines = []

    for pagina in airlines_paginas:
        airlines.extend(pagina.get("airlines"))

    for airline in airlines:
        resultados.append(
            {
                "iata": airline.get("iata"),
                "icao": airline.get("icao"),
                "nvls": airline.get("nvls"),
                "name": airline.get("publicName")

            }
        )
    
    return resultados

def transformar_aircrafttypes(aircrafttypes_paginas):

    resultado = []
    aircrafttypes = []

    for pagina in aircrafttypes_paginas:
        aircrafttypes.extend(pagina.get("aircraftTypes"))

    for aircrafttype in aircrafttypes:
        resultado.append(
            {
                "iataMain": aircrafttype.get("iataMain"),
                "iataSub": aircrafttype.get("iataSub"),
                "descricao_longa": aircrafttype.get("longDescription"),
                "descricao_curta": aircrafttype.get("shortDescription")
            }
        )
    
    return resultado

def transformar_destinations(destinations_pages):

    resultados = []
    destinations = []

    for pagina in destinations_pages:
        destinations.extend(pagina.get('destinations'))

    for destination in destinations:
        resultados.append(
            {
                "country": destination.get('country'),
                "city": destination.get('city'),
                "iata": destination.get('country'),
                "name": destination.get('publicName').get('english')
            }
        )
    
    return resultados

def transformar_flights(flights_pages):

    resultados = []
    flights = []

    for pagina in flights_pages:
        flights.extend(pagina.get("flights"))

    for flight in flights:
        aircraftType = flight.get('aircraftType')
        aircraftType_main = None
        aircraftType_sub = None
        if aircraftType:
            aircraftType_main = aircraftType.get('iataMain')
            aircraftType_sub = aircraftType.get('iataSub')

        baggageClaim = flight.get('baggageClaim')
        if baggageClaim:
            baggageClaim = baggageClaim.get('belts')

        codeshares = flight.get('codeshares')
        if codeshares:
            codeshares = codeshares.get('codeshares')
            if codeshares:
                codeshares = ','.join(codeshares)

        flightstates = flight.get('publicFlightState')
        if flightstates:
            flightstates = flightstates.get('flightStates')
            if flightstates:
                flightstates = '-'.join(flightstates)

        europe = None
        needvisa = None
        destinations = None
        route = flight.get('route')
        if route:
            destinations = route.get('destinations')
            europe = route.get('eu')
            needvisa = route.get('visa')
            if route:
                destinations = '->'.join(destinations)
        
        resultados.append(
            {
                "lastUpdatedAt": converte_datas(flight.get("lastUpdatedAt")),
                "actualLandingTime": converte_datas(flight.get("actualLandingTime")),
                "aircraftRegistration": flight.get('aircraftRegistration'),
                "main_type": aircraftType_main,
                "sub_type": aircraftType_sub,
                "baggage": baggageClaim,
                "codeshares": codeshares,
                "estimatedLandingTime": converte_datas(flight.get("estimatedLandingTime")),
                "expectedTimeOnBelt": converte_datas(flight.get("expectedTimeOnBelt")),
                "flightDirection": flight.get('flightDirection'),
                "flightName": flight.get('flightName'),
                "flightNumber": flight.get('flightNumber'),
                "gate": flight.get('gate'),
                "pier": flight.get('pier'),
                "id": flight.get('id'),
                "isOperationalFlight": flight.get('isOperationalFlight'),
                "airlineCode": flight.get('airlineCode'),
                "flight_states": flightstates,
                "destination": destinations,
                "europe": europe,
                "needvisa": needvisa,
                "isEurope": flight['route'].get('eu'),
                "visaNecessity": flight['route'].get('visa'),
                "scheduleDateTime": converte_datas(flight.get("scheduleDateTime")),
                "serviceType": flight.get('serviceType'),
                "terminal": flight.get('terminal')
            }
        )