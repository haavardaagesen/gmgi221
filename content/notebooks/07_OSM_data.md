---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
    split_at_heading: true
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Henting av data fra OpenStreetMap

## Hva er OpenStreetMap?

:::{figure} ../../static/images/lesson-6/osm-logo_256x256px.svg
:name: osm-logo
:alt: Logoet til OpenStreetMap (OSM)

OpenStreetMap er en gratis og åpen karttjeneste, men - først og fremst - er det
et globalt samarbeidsprosjekt for å samle inn frie og åpne geodata. *Kilde:
[wiki.openstreetmap.org](https://wiki.openstreetmap.org/wiki/Logos)*
:::

OpenStreetMap (OSM) er en global samarbeidsdatabase (crowd-sourced) og
prosjekt som har som mål å lage et fritt redigerbart kart over verden som inneholder
informasjon om miljøet vårt. Den inneholder data om gater, bygninger,
forskjellige tjenester og arealbruk, for å nevne noen få.
De innsamlede dataene er også grunnlaget for kartet på [openstreetmap.org](https://openstreetmap.org/). 


:::{admonition} Bidra!
:class: note

Du kan også registrere deg som bidragsyter hvis du vil legge til i databasen og
kartet eller korrigere og forbedre eksisterende data. Les mer i [OpenStreetMap
Wiki](https://wiki.openstreetmap.org/wiki/Main_Page).
:::


OSM har mer enn 8 millioner registrerte brukere som bidrar med rundt 4 millioner
endringer daglig. Databasen inneholder data som er beskrevet av [mer enn 7
milliarder noder](http://wiki.openstreetmap.org/wiki/Stats) (som utgjør linjer,
polygoner og andre objekter).

Mens den mest kjente siden av OpenStreetMap er kartet selv, som [vi
har brukt som et bakgrunnskart](../lesson-5/static-maps), er prosjektet mye
mer enn det. OSMs data kan brukes til mange andre formål som
**ruting**, **geokoding**, **utdanning** og **forskning**. OSM brukes også mye
for humanitær respons, for eksempel i kriseområder (for eksempel etter naturkatastrofer) og for å fremme økonomisk utvikling. Les mer om humanitære
prosjekter som bruker OSM-data fra [Humanitarian OpenStreetMap Team (HOTOSM)
nettsted](https://www.hotosm.org).

## Hovedverktøy i denne leksjonen

### OSMnx

Denne uken skal vi utforske en Python-pakke kalt
[OSMnx](https://github.com/gboeing/osmnx) som kan brukes til å hente gate-
nettverk fra OpenStreetMap, og konstruere, analysere og visualisere dem. OSMnx
kan også hente data om interessepunkter, som restauranter, skoler og
forskjellige typer tjenester. Pakken inkluderer også verktøy for å finne ruter på
et nettverk lastet ned fra OpenStreetMap, og implementerer algoritmer for å finne
korteste forbindelser for gange, sykling eller kjøring.


For å få en oversikt over mulighetene med pakken, se den innledende
videoen gitt av hovedutvikleren av pakken, Prof. Geoff Boeing: ["Meet
the developer: Introduction to OSMnx package by Geoff
Boeing"](https://www.youtube.com/watch?v=Q0uxu25ddc4&list=PLs9D4XVqc6dCAhhvhZB7aHGD8fCeCC_6N).

Det er også en vitenskapelig artikkel tilgjengelig som beskriver pakken:

> Boeing, G. 2017. ["OSMnx: New Methods for Acquiring, Constructing, Analyzing,
> and Visualizing Complex Street
> Networks."](https://www.researchgate.net/publication/309738462_OSMnx_New_Methods_for_Acquiring_Constructing_Analyzing_and_Visualizing_Complex_Street_Networks)
> Computers, Environment and Urban Systems 65, 126-139.
> doi:10.1016/j.compenvurbsys.2017.05.004

[Denne
opplæringen](https://github.com/gboeing/osmnx-examples/blob/master/notebooks/01-overview-osmnx.ipynb)
gir en praktisk oversikt over OSMnx-funksjonaliteter, og har også inspirert
denne AutoGIS-leksjonen.


### NetworkX

Vi vil også bruke [NetworkX](https://networkx.github.io/documentation//)
til å manipulere og analysere gatenettverksdataene hentet fra
OpenStreetMap. NetworkX er en Python-pakke som kan brukes til å opprette,
manipulere og studere strukturen, dynamikken og funksjonene til komplekse
nettverk.


---

## Last ned og visualiser OpenStreetMap-data med OSMnx

En nyttig funksjon med OSMnx er enkle å bruke verktøy for å laste ned
[OpenStreetMap](http://www.openstreetmap.org) data via prosjektets [OverPass
API](http://wiki.openstreetmap.org/wiki/Overpass_API).
I denne delen vil vi lære å laste ned og visualisere gatenettverket
og tilleggsdata fra OpenStreetMap som dekker et interesseområde.


### Gatenettverk

[`osmnx.graph`
modulen](https://osmnx.readthedocs.io/en/stable/osmnx.html#module-osmnx.graph)
laster ned data for å konstruere et kjørbart vei-nettverksgraf, basert på et
brukerdefinert interesseområde. Dette interesseområdet kan spesifiseres, for
eksempel ved bruk av et stedsnavn, en begrensningsboks eller et polygon. Her vil vi bruke
et stedsnavn for å hente data som dekker Kamppi-området i Helsinki, Finland.

I stedsnavnsforespørselen bruker OSMnx Nominatim Geocoding API. Dette betyr
at stedsnavn skal eksistere i OpenStreetMap-databasen (kjør et testsøk
på [openstreetmap.org](https://www.openstreetmap.org/) eller
[nominatim.openstreetmap.org](https://nominatim.openstreetmap.org/ui/search.html)).

Vi vil lese et OSM-gatenettverk ved hjelp av OSMnxs
[graph_from_place()](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.graph.graph_from_place) funksjon:

```{code-cell} python
import osmnx

PLACE_NAME = "Kamppi, Helsinki, Finland"
graph = osmnx.graph_from_place(PLACE_NAME)
```

Sjekk datatypen til grafen:

```{code-cell} python 
type(graph)
```

Det vi har her er et
[`networkx.MultiDiGraph`](https://networkx.org/documentation/stable/reference/classes/multidigraph.html) objekt.

OSMnxs grafer har ikke en innebygd metode for å plotte dem, men pakken
kommer med en funksjon for å gjøre det:

```{code-cell} python
figure, ax = osmnx.plot_graph(graph)
```

Akkurat som dens GeoPandas og Pandas-ekvivalenter, bruker `osmnx.plot_graph()`
matplotlib. Funksjonen returnerer en `(figure, axes)`-tuple, som kan brukes til 
å modifisere figuren ved hjelp av alle matplotlib-funksjoner vi allerede har blitt kjent med.

Vi kan se at grafen vår inneholder noder (punktene) og kanter (linjene)
som kobler disse nodene til hverandre.

### Konverter en graf til `GeoDataFrame`s

Gatenettverket vi nettopp lastet ned er en *graf*, mer spesifikt en
`networkx.MultiDiGraph`. Hovedformålet er å representere de topologiske
forholdene mellom noder og koblingene (kanter) mellom dem. Noen ganger er det mer praktisk å ha de underliggende geodataene i `geopandas.GeoDataFrame`s.
OSMnx kommer med en praktisk funksjon som konverterer en graf til to geo-data
rammer, en for noder, og en for kanter:
[`osmnx.graph_to_gdfs()`](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.utils_graph.graph_to_gdfs).


```{code-cell} python
nodes, edges = osmnx.graph_to_gdfs(graph)
```

```{code-cell} python
nodes.head()
```

```{code-cell} python
edges.head()
```

Fint! Nå, som vi kan se, har vi grafen vår som GeoDataFrames og vi kan plotte
dem ved hjelp av de samme funksjonene og verktøyene som vi har brukt før.



### Stedspolygon

La oss også plotte polygonet som representerer vårt interesseområde (Kamppi,
Helsinki). Vi kan hente polygon-geometrien ved hjelp av
[osmnx.geocode_to_gdf()](https://osmnx.readthedocs.io/en/stable/osmnx.html?highlight=geocode_to_gdf(#osmnx.geocoder.geocode_to_gdf)
funksjonen.

```{code-cell} python
# Hent stedsgrensen relatert til stedsnavnet som en geodataframe
area = osmnx.geocode_to_gdf(PLACE_NAME)
```

Som navnet på funksjonen allerede forteller oss, returnerer den et GeoDataFrame-objekt
basert på det spesifiserte stedsnavnsøket. La oss fortsatt verifisere datatypen: 

```{code-cell} python
# Sjekk datatypen
type(area)
```

La oss også ta en titt på dataene:

```{code-cell} python
# Sjekk dataverdier
area
```

```{code-cell} python
# Plot området:
area.plot()
```

### Bygningsavtrykk

I tillegg til nettverksdata, kan OSMnx også laste ned alle andre data som finnes i OpenStreetMap-databasen. Dette inkluderer for eksempel bygningsavtrykk og forskjellige interessepunkter (POI-er). For å laste ned vilkårlige geometrier, filtrert av [OSM-tags](https://wiki.openstreetmap.org/wiki/Map_features) og et stedsnavn, bruk [`osmnx.geometries_from_place()`](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.geometries.geometries_from_place) [geometries er snart utdatert - La oss allerede bruke features i stedet]. Taggen for å hente alle [bygninger](https://wiki.openstreetmap.org/wiki/Buildings) er `building = yes`.

```{code-cell} python 
buildings = osmnx.geometries_from_place(
    PLACE_NAME,
    {"building": True},
)
```

```{code-cell} python 
len(buildings) 
```

```{code-cell} python 
buildings.head() 
```

Som du kan se, er det flere kolonner i `buildings`. Hver kolonne inneholder
informasjon om en spesifikk tag som OpenStreetMap-bidragsytere har lagt til.
Hver tag består av en nøkkel (kolonnenavnet) og verdier (for eksempel
`building=yes` eller `building=school`). Les mer om tags og tagging
praksis i [OpenStreetMap
wiki](https://wiki.openstreetmap.org/wiki/Tags). 

```{code-cell} python 
buildings.columns 
```



### Interessepunkter

Interessepunkt (POI) er et generisk konsept som beskriver punktlokasjoner
som representerer steder av interesse. Siden `osmnx.geometries_from_place()` kan laste ned alle geometridata som finnes i OpenStreetMap-databasen, kan det også brukes til å laste ned alle typer POI-data. [geometries er snart utdatert - La oss allerede bruke features i stedet]

I OpenStreetMap beskrives mange POI-er ved hjelp av [`amenity`
taggen](https://wiki.openstreetmap.org/wiki/Key:amenity).  Vi kan for eksempel,
hente alle restaurantlokasjoner ved å spørre om `amenity=restaurant`. 

```{code-cell} python
restaurants = osmnx.geometries_from_place(
    PLACE_NAME,
    {
        "amenity": "restaurant"
    }
)
len(restaurants) 
```

Som vi kan se, er det ganske mange restauranter i området.

La oss utforske hvilke attributter vi har i vår GeoDataFrame for restauranter:

```{code-cell} python
# Tilgjengelige kolonner
restaurants.columns.values 
```

Som du kan se, er det ganske mye (potensiell) informasjon relatert til
fasilitetene. La oss velge ut kolonnene og undersøke dataene videre. Kan vi
hente ut alle restauranters navn, adresse og åpningstider?

```{code-cell} python
# Velg noen nyttige kolonner og skriv ut
interesting_columns = [
    "name",
    "opening_hours",
    "addr:city",
    "addr:country",
    "addr:housenumber",
    "addr:postcode",
    "addr:street"
]

# Skriv ut kun valgte kolonner
restaurants[interesting_columns].head(10) 
```

:::{tip}
hvis noe av informasjonen trenger en oppdatering, gå til [openstreetmap.org](https://openstreetmap.org) og rediger kildeinformasjonen!
:::



### Parker og grøntområder

La oss prøve å hente alle offentlige parker i Kamppi-området. I OpenStreetMap,
[skal parker være tagget](https://wiki.openstreetmap.org/wiki/Map_features) som
`leisure = park`. Mindre grøntområder (*puistikot*) er noen ganger også tagget
`landuse = grass`. Vi kan kombinere flere tags i en dataforespørsel.

```{code-cell} python
parks = osmnx.geometries_from_place(
    PLACE_NAME,
    {
        "leisure": "park",
        "landuse": "grass",
    },
)
```

```{code-cell} python
parks.head()
```

```{code-cell} python 
parks.plot(color="green") 
```


### Plotting av dataene

La oss lage et kart ut av gatene, bygningene, restaurantene og områdepolygonet.


```{code-cell} python 
import matplotlib
figure, ax = matplotlib.pyplot.subplots(figsize=(12,8))

# Plot avtrykket
area.plot(ax=ax, facecolor="black")

# Plot parkene
parks.plot(ax=ax, facecolor="green")

# Plot gate 'kanter'
edges.plot(ax=ax, linewidth=1, edgecolor="dimgray")

# Plot bygningene
buildings.plot(ax=ax, facecolor="silver", alpha=0.7)

# Plot restaurantene
restaurants.plot(ax=ax, color="yellow", alpha=0.7, markersize=10)
```

Kult! Nå har vi et kart der vi har plottet restaurantene, bygningene,
gatene og grensene for det valgte området 'Kamppi' i Helsinki. Og
alt dette krever bare noen få linjer med kode. Ganske flott!

:::{admonition} Sjekk din forståelse
:class: hint

Hent OpenStreetMap-data fra et annet område! Last ned disse elementene ved hjelp av
OSMnx-funksjoner fra ditt interesseområde:
    
- Utstrekning av området ved hjelp av `geocode_to_gdf()`
- Gate-nettverk ved hjelp av `graph_from_place()`, og konverter til geo-data frame ved hjelp av
  `graph_to_gdfs()`
- Bygningsavtrykk (og andre geometrier) ved hjelp av `geometries_from_place()`
  og passende tags.
    
*Merk, jo større område du velger, jo lenger tid tar det å hente data
fra API!*


```{code-cell} python python
# Spesifiser navnet som brukes for å søke etter dataene. Sjekk at steds-
# navnet er gyldig fra https://nominatim.openstreetmap.org/ui/search.html
MY_PLACE = ""
```

```{code-cell} python python
# Hent gate-nettverk
```

```{code-cell} python python
# Hent bygningsavtrykk
```

```{code-cell} python python
# Plot dataene
```
:::


## Videre lesing

For å analysere OpenStreetMap-data over store områder, er det ofte mer effektivt og
meningsfullt å laste ned dataene på en gang, i stedet for separate spørringer til
API. Slike datadumper fra OpenStreetMap er tilgjengelige i forskjellige filformater,
OSM [Protocolbuffer Binary
Format](https://wiki.openstreetmap.org/wiki/PBF_Format) (PBF) er en av
dem. Datautdrag som dekker hele land og kontinenter er tilgjengelige, for
eksempel, på [download.geofabrik.de](https://download.geofabrik.de/).

[Pyrosm](https://pyrosm.readthedocs.io/) er en Python-pakke for lesing
av OpenStreetMap-data fra PBF-filer til `geopandas.GeoDataFrames`. Pyrosm gjør
det enkelt å hente vei-nettverk, bygninger, interessepunkter (POI), arealbruk,
naturlige elementer, administrative grenser og mye mer - likt OSMnx,
men tilpasset analyser av store områder.  Mens OSMnx leser dataene fra
Overpass API, leser pyrosm dataene fra en lokal PBF-fil.

Les mer om henting og bruk av pbf-filer som kilde for å analysere
OpenStreetMap-data i Python fra [pyrosm
dokumentasjonen](https://pyrosm.readthedocs.io/en/latest/basics.html#protobuf-file-what-is-it-and-how-to-get-one).