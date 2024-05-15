---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
    split_at_heading: true
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Nettverksanalyse i Python

Å finne en korteste vei ved hjelp av et bestemt gate-nettverk er et vanlig GIS-problem
som har mange praktiske applikasjoner. For eksempel, navigasjon, en av de
‘hverdagslige’ applikasjonene der **rute**-algoritmer brukes til å finne den
optimale ruten mellom to eller flere punkter.

Selvfølgelig har Python-økosystemet produsert pakker som kan brukes til
å gjennomføre nettverksanalyser, som for eksempel ruting. 
[NetworkX](https://networkx.github.io/documentation/) pakken gir forskjellige
verktøy for å analysere nettverk, og implementerer flere forskjellige rutealgoritmer,
som for eksempel
[Dijkstra’s](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path.html)
eller
[A\*](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html#module-networkx.algorithms.shortest_paths.astar)
algoritmene. Begge er vanligvis brukt til å finne korteste veier langs transportnettverk.

For å kunne utføre nettverksanalyse, er det selvfølgelig nødvendig å ha et
nettverk som brukes til analysene. 
[OSMnx](https://osmnx.readthedocs.io/) pakken lar oss hente rutbare
nettverk fra OpenStreetMap for forskjellige transportformer (gåing, sykling og
kjøring). OSMnx pakken pakker også noen av NetworkX's funksjoner på en praktisk måte
for bruk på OpenStreetMap-data.

I følgende avsnitt vil vi bruke OSMnx til å finne den korteste veien mellom
to punkter basert på sykkelbare veier. Med bare de minste modifikasjonene, kan vi
deretter gjenta analysen for det gangbare gatenettverket.



## Få et rutbart nettverk

For å laste ned OpenStreetMap-data som representerer gatenettverket, kan vi bruke
dens
[`graph_from_place()`](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.graph.graph_from_place)
funksjon. Som parametere forventer den et stedsnavn og, valgfritt, en nettverkstype.

```{code-cell} python
import osmnx

PLACE_NAME = "Kamppi, Helsinki, Finland"
graph = osmnx.graph_from_place(
    PLACE_NAME,
    network_type="bike"
)
figure, ax = osmnx.plot_graph(graph)
```

:::{admonition} Proft tips!
:class: hint

Noen ganger kan den korteste veien gå litt utenfor det definerte området av
interesse. For å ta hensyn til dette, kan vi hente nettverket for et litt større område
enn distriktet Kamppi, i tilfelle den korteste veien ikke er helt innenfor
dens grenser. 
:::

```{code-cell} python
# Få området av interesse polygon
place_polygon = osmnx.geocode_to_gdf(PLACE_NAME)

# Re-projiser polygonet til en lokal projisert CRS (slik at CRS-enheten er meter)
place_polygon = place_polygon.to_crs("EPSG:3067")

# Buffer med 200 meter
place_polygon["geometry"] = place_polygon.buffer(200)

# Re-projiser polygonet tilbake til WGS84 (kreves av OSMnx)
place_polygon = place_polygon.to_crs("EPSG:4326")

# Hent nettverksgraf
graph = osmnx.graph_from_polygon(
    place_polygon.at[0, "geometry"],
    network_type="bike"
)

fig, ax = osmnx.plot_graph(graph)
```

### Dataoversikt

Nå som vi har fått et komplett nettverksdiagram for den reisemåten vi spesifiserte
(sykling), kan vi ta en nærmere titt på hvilke attributter som er tildelt
noder og kanter i nettverket. Det er sannsynligvis lettest å først konvertere
nettverket til en geodata-frame der vi deretter kan bruke verktøyene vi lærte i
tidligere leksjoner.

For å konvertere et diagram til en geodata-frame, kan vi bruke `osmnx.graph_to_gdfs()`
(se [forrige avsnitt](retrieve-data-from-openstreetmap)). Her kan vi gjøre
bruk av funksjonens parametere `nodes` og `edges` for å velge om vi vil ha
bare noder, bare kanter, eller begge (standard):

```{code-cell} python
# Hent bare kanter fra grafen
edges = osmnx.graph_to_gdfs(graph, nodes=False, edges=True)
edges.head()
```

Den resulterende geodata-framen består av en lang liste over kolonner. De fleste av dem
relaterer til [OpenStreetMap-tags](https://wiki.openstreetmap.org/wiki/Tags), og
navnene deres er ganske selvforklarende. Kolonnene `u` og `v` beskriver
topologisk forhold innen nettverket: de betegner start- og slutt-noden
for hver kant.

:::{list-table} Kolonner i `edges`
:header-rows: 1
:name: columns-in-edges

* - Kolonne
  - Beskrivelse
  - Datatype
* - [bridge](http://wiki.openstreetmap.org/wiki/Key:bridge)    
  - Broelement              
  - boolean           
* - geometry                                                   
  - Geometri av elementet     
  - Shapely.geometry  
* - [highway](http://wiki.openstreetmap.org/wiki/Key:highway)  
  - Tag for veier (veitype)   
  - str / list        
* - [lanes](http://wiki.openstreetmap.org/wiki/Key:lanes)      
  - Antall kjørefelt             
  - int (or nan)      
* - [length](http://wiki.openstreetmap.org/wiki/Key:length)    
  - Lengden på elementet (meter)  
  - float             
* - [maxspeed](http://wiki.openstreetmap.org/wiki/Key:maxspeed)
  - Maksimal lovlige hastighetsbegrensning   
  - int /list         
* - [name](http://wiki.openstreetmap.org/wiki/Key:name)        
  - Navn på (gata) elementet
  - str (or nan)      
* - [oneway](http://wiki.openstreetmap.org/wiki/Key:oneway)    
  - Enveisvei                
  - boolean           
* - [osmid](http://wiki.openstreetmap.org/wiki/Node)           
  - Unike id-er for elementet  
  - list              
* - [u](http://ow.ly/bV8n30h7Ufm)                              
  - Startnoden for kanten      
  - int               
* - [v](http://ow.ly/bV8n30h7Ufm)                              
  - Sluttnoden for kanten       
  - int               
:::


Hvilke typer gater består nettverket vårt av?

```{code-cell} python
edges["highway"].value_counts()
```

### Transformere til projisert referansesystem

Nettverksdataens kartografiske referansesystem (CRS) er WGS84 (EPSG:4326), et
geografisk referansesystem. Det betyr at avstander er registrert og uttrykt
i grader, områder i kvadratgrader. Dette er ikke praktisk for nettverks-
analyser, som for eksempel å finne en korteste vei.

Igjen, OSMnx's *graf*-objekter tilbyr ikke en metode for å transformere deres
geodata, men OSMnx kommer med en separat funksjon:
[`osmnx.project_graph()`](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.projection.project_graph)
tar en inngangsgraf og en CRS som parametere, og returnerer en ny, transformert,
graf. Hvis `crs` utelates, er transformasjonen standard til den mest
egnede UTM-sonen lokalt.

```{code-cell} python
# Transformere grafen til UTM
graph = osmnx.project_graph(graph) 

# Hent re-projiserte noder og kanter
nodes, edges = osmnx.graph_to_gdfs(graph)

nodes.crs
```

---


## Analysering av nettverksegenskaper

Nå som vi har forberedt et rutbart nettverksdiagram, kan vi gå over til de mer
analytiske funksjonene til OSMnx, og hente informasjon om nettverket.
For å beregne grunnleggende nettverksegenskaper, bruk
[`osmnx.basic_stats()`](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.stats.basic_stats):

```{code-cell} python
# Beregn nettverksstatistikk
osmnx.basic_stats(graph)
```

Dette gir oss ennå ikke alle interessante egenskaper ved nettverket vårt, som
OSMnx ikke automatisk tar hensyn til området som er dekket av nettverket.
Vi kan gjøre det manuelt, ved, først, å avgrense [komplekse
skallet](https://en.wikipedia.org/wiki/Convex_hull) til nettverket (av en 'unary'
union av alle funksjonene), og deretter, andre, beregne området av dette skallet.

```{code-cell} python
convex_hull = edges.unary_union.convex_hull
convex_hull
```

```{code-cell} python
stats = osmnx.basic_stats(graph, area=convex_hull.area)
stats
```

```{code-cell} python
:tags: [remove-input, remove-output]

import math
import myst_nb

myst_nb.glue("node_density_km", round(stats["node_density_km"], 1))
myst_nb.glue("edge_length_total", math.floor(stats["edge_length_total"] / 1000))
```

Som vi kan se, har vi nå mye informasjon om gatenettverket vårt som
kan brukes til å forstå strukturen. Vi kan for eksempel se at gjennomsnittlig
nodetetthet i nettverket vårt er {glue:}`node_density_km`&nbsp;noder/km og at
den totale kantlengden på nettverket vårt er mer enn
{glue:}`edge_length_total`&nbsp;kilometer.


:::{admonition} Sentralitetsmål
:class: note

I tidligere år diskuterte dette kurset også [grad-
sentralitet](https://en.wikipedia.org/wiki/Centrality). Beregning av nettverk
sentralitet har endret seg i OSMnx: å gå i dybden ville være utenfor omfanget av
dette kurset. Se [den tilsvarende OSMnx
notebook](https://github.com/gboeing/osmnx-examples/blob/main/notebooks/06-stats-indicators-centrality.ipynb)
for et eksempel.
:::


---


## Korteste bananalyse

La oss nå beregne den korteste veien mellom to punkter ved hjelp av
[`osmnx.shortest_path()`](https://osmnx.readthedocs.io/en/stable/osmnx.html?highlight=get_nearest_node#osmnx.distance.shortest_path).



### Opprinnelses- og destinasjonspunkter 

Først må vi spesifisere kilden og målplasseringene for ruten vår. Hvis du
er kjent med Kamppi-området, kan du spesifisere en egendefinert stedsnavn som en
kildeposisjon. Eller, du kan følge med og velge disse punktene som opprinnelse
og destinasjon i analysen:
- [`"Maria 01, Helsinki"`](https://nominatim.openstreetmap.org/ui/search.html?q=Maria+01):
  en oppstartshub i et tidligere sykehusområde.
- [`"ruttopuisto"`](https://nominatim.openstreetmap.org/ui/search.html?q=ruttopuisto),
  en park. Parkens offisielle navn er ’Vanha kirkkopuisto’, men Nominatim
  er også i stand til å geokode kallenavnet.

Vi kunne finne ut koordinatene for disse stedene manuelt, og lage
`shapely.geometry.Point`s basert på koordinatene. Men hvis vi ville ha
mer enn bare to punkter, ville det raskt bli et ork. I stedet kan vi
bruke OSMnx til å geokode lokasjonene.

Husk å transformere opprinnelses- og destinasjonspunktene til samme referanse
system som nettverksdataene.

```{code-cell} python
origin = (
    osmnx.geocode_to_gdf("Maria 01, Helsinki")  # hent geolokasjon
    .to_crs(edges.crs)  # transformer til UTM
    .at[0, "geometry"]  # velg geometri av første rad
    .centroid  # bruk midtpunktet
)

destination = (
    osmnx.geocode_to_gdf("ruttopuisto")
    .to_crs(edges.crs)
    .at[0, "geometry"]
    .centroid
)
```

Vi har nå `shapely.geometry.Point`s som representerer opprinnelses- og destinasjon
plasseringene for nettverksanalysen vår. I en neste trinn, må vi finne disse punktene på
det rutbare nettverket før den endelige rutingen.

### Nærmeste node

For å rute på nettverket, må vi først finne et startpunkt og sluttpunkt
som er en del av nettverket. Bruk
`[osmnx.distance.nearest_nodes()`](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.distance.nearest_nodes)
for å returnere den nærmeste nodens ID:

```{code-cell} python
origin_node_id = osmnx.nearest_nodes(graph, origin.x, origin.y)
origin_node_id
```

```{code-cell} python
destination_node_id = osmnx.nearest_nodes(graph, destination.x, destination.y)
destination_node_id
```

### Ruting

Nå er vi klare for ruting og for å finne den korteste veien mellom
opprinnelses- og målplasseringene. Vi vil bruke
[`osmnx.shortest_path()`](https://osmnx.readthedocs.io/en/stable/osmnx.html?highlight=get_nearest_node#osmnx.distance.shortest_path).

Funksjonen tar tre obligatoriske parametere: en graf, en opprinnelsesnod-id, og
en destinasjonsnod-id, og to valgfrie parametere: `weight` kan settes til
å vurdere en annen *kostnadsimpedans* enn lengden på ruten, og `cpus`
kontrollerer parallell beregning av mange ruter.

```{code-cell} python
# Finn den korteste veien mellom opprinnelse og destinasjon
route = osmnx.shortest_path(graph, origin_node_id, destination_node_id)
route
```

Som et resultat får vi en liste over alle nodene som er langs den korteste veien.

Vi kunne hente plasseringene til disse nodene fra `nodes`
GeoDataFrame og lage en LineString-presentasjon av punktene, men heldigvis,
OSMnx kan gjøre det for oss og vi kan plotte korteste vei ved hjelp av
`plot_graph_route()`-funksjonen:

```{code-cell} python
# Plot den korteste veien
fig, ax = osmnx.plot_graph_route(graph, route)
```

Flott! Nå har vi den korteste veien mellom opprinnelses- og målplasseringene våre.
Å kunne analysere korteste veier mellom steder kan være verdifull
informasjon for mange applikasjoner. Her analyserte vi bare de korteste veiene
basert på avstand, men ganske ofte er det mer nyttig å finne de optimale rutene
mellom steder basert på reisetiden. Her, for eksempel kunne vi
beregne tiden det tar å krysse hvert veisegment ved å dele
lengden på veisegmentet med fartsgrensen og beregne de optimale
rutene ved å ta hensyn til fartsgrensene også som kan endre
resultatet spesielt på lengre turer enn her.

## Lagre korteste veier til disk

Ganske ofte må du lagre ruten til en fil for videre analyse og
visualiseringsformål, eller i det minste ha den som et GeoDataFrame-objekt i Python.
La oss derfor fortsette litt til og se hvordan vi kan lage ruten til en
linjestreng og lagre den korteste veigeometrien og relaterte attributter i en
geopackage-fil.

Først må vi få nodene som tilhører den korteste veien:

```{code-cell} python
# Få nodene langs den korteste veien
route_nodes = nodes.loc[route]
route_nodes
```

Som vi kan se, har vi nå alle nodene som var en del av den korteste veien som en GeoDataFrame.

Nå kan vi lage en LineString ut av punktgeometriene til nodene:

```{code-cell} python
import shapely.geometry

# Lag en geometri for den korteste veien
route_line = shapely.geometry.LineString(
    list(route_nodes.geometry.values)
)
route_line
```

Nå har vi ruten som en LineString-geometri.

La oss lage en GeoDataFrame ut av den med litt nyttig informasjon om ruten vår,
for eksempel en liste over osm-idene som er en del av ruten og lengden
på ruten.

```{code-cell} python
import geopandas

route_geom = geopandas.GeoDataFrame(
    {
        "geometry": [route_line],
        "osm_nodes": [route],
    },
    crs=edges.crs
)

# Beregn rute-lengden
route_geom["length_m"] = route_geom.length

route_geom.head()
```

Nå har vi en GeoDataFrame som vi kan lagre til disk. La oss fortsatt bekrefte at
alt er ok ved å plotte ruten vår på toppen av gatenettverket og noen
bygninger, og plot også opprinnelses- og målpunktene på toppen av kartet vårt.

Last ned bygninger:

```{code-cell} python
bygninger = osmnx.geometries_from_place(
    PLACE_NAME,
    {
        "building" : True
    }
).to_crs(edges.crs)
```

La oss nå plotte ruten og gatenettverkselementene for å bekrefte at
alt er som det skal:

```{code-cell} python
import contextily
import matplotlib.pyplot

fig, ax = matplotlib.pyplot.subplots(figsize=(12,8))

# Plot kanter og noder
edges.plot(ax=ax, linewidth=0.75, color='gray')
nodes.plot(ax=ax, markersize=2, color='gray')

# Legg til bygninger
ax = buildings.plot(ax=ax, facecolor='lightgray', alpha=0.7)

# Legg til ruten
ax = route_geom.plot(ax=ax, linewidth=2, linestyle='--', color='red')

# Legg til bakgrunnskart
contextily.add_basemap(ax, crs=buildings.crs, source=contextily.providers.CartoDB.Positron)
```

Flott, alt ser ut til å være i orden! Som du kan se, har vi nå full
kontroll over alle elementene i kartet vårt, og vi kan bruke alle estetiske
egenskaper som matplotlib gir for å endre hvordan kartet vårt vil se ut. Nå
er vi nesten klare til å lagre dataene våre på disk.



## Forbered data for lagring til fil

Dataene inneholder visse datatyper (som `list`) som bør konverteres
til tegnstrenger før du lagrer dataene til fil (et alternativ ville være
å kaste ugyldige kolonner).

```{code-cell} python
edges.head()
```

```{code-cell} python
# Kolonner med ugyldige verdier
problematiske_kolonner = [
    "osmid",
    "lanes",
    "name",
    "highway",
    "width",
    "maxspeed",
    "reversed",
    "junction",
    "bridge",
    "tunnel",
    "access",
    "service",
    
]

#  konverter valgte kolonner til strengformat
edges[problematic_columns] = edges[problematic_columns].astype(str)
```

```{code-cell} python
route_geom["osm_nodes"] = route_geom["osm_nodes"].astype(str)
```

Nå kan vi se at de fleste attributtene er av typen `object` som ganske ofte (som vår her) refererer til en datatypetype.

## Lagre dataene:

```{code-cell} python
import pathlib
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```

```{code-cell} python
# Lagre ett lag etter et annet
output_gpkg = DATA_DIRECTORY / "OSM_Kamppi.gpkg"

edges.to_file(output_gpkg, layer="streets")
route_geom.to_file(output_gpkg, layer="route")
nodes.to_file(output_gpkg, layer="nodes")
#bygninger[['geometry', 'name', 'addr:street']].to_file(output_gpkg, layer="buildings")
display(buildings.describe())
display(buildings)
```

Flott, nå har vi lagret alle dataene som ble brukt til å produsere kartene i en geopakke.



## Videre lesing

Her lærte vi hvordan man løser en enkel ruteoppgave mellom opprinnelses- og målpunkt. Hva om vi har hundrevis eller tusenvis av opprinnelser? Dette er tilfelle hvis du vil utforske reiseavstandene til en spesifikk plassering over hele byen, for eksempel når du analyserer tilgjengeligheten av jobber og tjenester (som i reisetidsmatrisedataene som ble brukt i tidligere seksjoner). 

Sjekk ut pyrosm-dokumentasjonen om [arbeid med grafer](https://pyrosm.readthedocs.io/en/latest/graphs.html#working-with-graphs) for mer avanserte eksempler på nettverksanalyse i python. For eksempel er [pandana](https://udst.github.io/pandana/) et raskt og effektivt python-bibliotek for å lage aggregerte nettverksanalyser på kort tid over store nettverk, og pyrosm kan brukes til å forberede inngangsdataene for en slik analyse.
