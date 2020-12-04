'''{
"type": "FeatureCollection",
"licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
"features": [{
    "type": "Feature",
    "properties": {
        "name": "prueba",
        "display_name": "polígono",
        "address": {
            "city": "Bogotá",
            "county": "Bogotá",
            "country": "colombia",
            "country_code": "co"
        }
    },
    "bbox": [-103.2838528, 20.6960196, -103.2835124, 20.6987892],
    "geometry": {
        "type": "Point",
        "coordinates": [-103.283776174626, 20.6966302195429]
    }'''

    #Sin agujeros:

     {
         "tipo": "Polígono",
         "coordenadas": [
             [
                 [100,0, 0,0],
                 [101,0, 0,0],
                 [101,0, 1,0],
                 [100,0, 1,0],
                 [100,0, 0,0]
             ]
         ]
     }

   #Con agujeros:

     {
         "tipo": "Polígono",
         "coordenadas": [
             [
                 [100,0, 0,0],
                 [101,0, 0,0],
                 [101,0, 1,0],
                 [100,0, 1,0],
                 [100,0, 0,0]
             ],
             [
                 [100,8, 0,8],
                 [100,8, 0,2],
                 [100,2, 0,2],
                 [100,2, 0,8],
                 [100,8, 0,8]
             ]
         ]
     }
}]
}
