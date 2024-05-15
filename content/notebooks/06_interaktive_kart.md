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

# Interaktive kart

[Online kart](https://link.springer.com/referenceworkentry/10.1007/978-3-319-23519-6_1485-2)
har vært interaktive i lang tid: nesten alle online kart tillater å zoome
inn og ut, å panorere kartomfanget, og å velge kartfunksjoner, eller ellers
forespørre informasjon om dem.

Interaktivt innhold i nettsider, som online kart, er typisk
implementert ved hjelp av
[*JavaScript*/*ECMAScript*](https://en.wikipedia.org/wiki/ECMAScript), et skriptspråk
opprinnelig rettet mot nettsider, primært, men brukt for mange andre
applikasjoner.

I det åpne kildekoderiket finnes det en rekke forskjellige *JavaScript*
biblioteker for interaktiv webkartografi, inkludert
[Leaflet](https://leafletjs.com/), som vi vil bruke i denne leksjonen, og
[OpenLayers](https://openlayers.org/).

Ingen bekymringer, vi vil ikke måtte skrive en eneste linje med *JavaScript*; dette er en
*Python* kurs, tross alt. Heller, vi vil dra nytte av
[*Folium*](https://python-visualization.github.io/folium/) Python-pakken: den
hjelper med å lage interaktive *Leaflet* kart fra data lagret i
`geopandas.GeoDataFrame`s.


:::{admonition} *Folium* ressurser
:class: note

Finn mer informasjon om mulighetene til *Folium* pakken på dens
offisielle nettsider:
- [Dokumentasjon](https://python-visualization.github.io/folium/)
- [Eksempelgalleri](https://nbviewer.org/github/python-visualization/folium/tree/main/examples/)
- [Hurtigstart guide](https://python-visualization.github.io/folium/quickstart.html#Getting-Started)
:::


## Opprette et enkelt interaktivt webkart

Vi vil starte med å lage et enkelt interaktivt webkart som ikke inneholder noe
annet enn et basekart. Dette er for at vi skal bli vant til hvordan *Folium*’s syntaks fungerer, og
hvilke trinn vi må ta.

Vi lager et `folium.Map` objekt, og spesifiserer sentrert rundt hvilken `location`
og på hvilket innledende zoomnivå (~0-20) et kart skal vises. Ved å sette
`control_scale` til `True`, får vi *Folium* til å vise en skalabar.

```{code-cell} python
import pathlib
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"

# Vi vil eksportere HTML-sider i løpet av denne leksjonen,
# la oss også forberede en utdatamappe for dem:
HTML_DIRECTORY = NOTEBOOK_PATH / "html"
HTML_DIRECTORY.mkdir(exist_ok=True)
```


```{code-cell} python
import folium

interactive_map = folium.Map(
    location=(60.2, 24.8),
    zoom_start=10,
    control_scale=True
)

interactive_map
```


### Lagre det resulterende kartet

For å lagre dette kartet til en HTML-fil som kan åpnes i en hvilken som helst nettleser,
bruk [`folium.Map.save()`](https://python-visualization.github.io/branca/element.html#branca.element.Element.save):

```{code-cell} python
interactive_map.save(HTML_DIRECTORY / "base-map.html")
```


### Endre basekartet

Hvis du vil bruke et annet baselag enn standard OpenStreetMap,
aksepterer `folium.Map` en parameter `tiles`, som enten kan referere til [en av de
innebygde kartleverandørene](https://python-visualization.github.io/folium/modules.html#folium.folium.Map).

Mens vi er i gang, la oss også variere senterlokasjonen og zoomnivået
på kartet:

```{code-cell} python
interactive_map = folium.Map(
    location=(60.2, 25.00),
    zoom_start=12,
    tiles="cartodbpositron"
)
interactive_map
```

Eller vi kan peke på en egendefinert *tileset URL*:

```{code-cell} python
interactive_map = folium.Map(
    location=(60.2, 25.00),
    zoom_start=12,
    tiles="https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}",
    attr="Google maps",
)
interactive_map
```

## Legg til en punktmarkør

For å legge til en enkelt markør til et *Folium* kart, opprett en
[`folium.Marker`](https://python-visualization.github.io/folium/modules.html#folium.map.Marker).
Gi en
[`folium.Icon`](https://python-visualization.github.io/folium/modules.html#folium.map.Icon)
som en parameter `icon` for å påvirke hvordan markøren er stylet, og sett `tooltip`
for å vise en tekst når musepekeren beveger seg over den.

```{code-cell} python
interactive_map = folium.Map(
    location=(60.2, 25.0),
    zoom_start=12
)

kumpula = folium.Marker(
    location=(60.204, 24.962),
    tooltip="Kumpula Campus",
    icon=folium.Icon(color="green", icon="ok-sign")
)
kumpula.add_to(interactive_map)

interactive_map
```


## Legg til et lag med punkter

*Folium* støtter også å legge til hele lag, for eksempel, som
`geopandas.GeoDataFrames`. *Folium* implementerer [*Leaflet*'s `geoJSON`
lag](https://leafletjs.com/reference.html#geojson) i sin
`folium.features.GeoJson` klasse. Vi kan initialisere en slik klasse (og lag)
med en geodata-ramme, og legge den til et kart. I eksempelet nedenfor bruker vi
`addresses.gpkg` datasettet vi lager [i leksjon
3](../lesson-3/geocoding-in-geopandas).

```{code-cell} python
import geopandas

addresses = geopandas.read_file(DATA_DIRECTORY / "addresses.gpkg")
addresses.head()
```

```{code-cell} python
interactive_map = folium.Map(
    location=(60.2, 25.0),
    zoom_start=12
)

addresses_layer = folium.features.GeoJson(
    addresses,
    name="Offentlige transportstopp"
)
addresses_layer.add_to(interactive_map)

interactive_map
```

Vi kan også legge til et popup-vindu på kartet vårt som ville vise adressene på interessepunktet ved å klikke:

```{code-cell} python
interactive_map = folium.Map(
    location=(60.2, 25.0),
    zoom_start=12
)

popup = folium.GeoJsonPopup(
    fields=["address"],
    aliases=["Adresse"],
    localize=True,
    labels=True,
    style="background-color: yellow;",
)

addresses_layer = folium.features.GeoJson(
    addresses,
    name="Offentlige transportstopp",
    popup=popup
)
addresses_layer.add_to(interactive_map)

interactive_map
```
## Legg til et polygonlag

I den følgende delen skal vi gjenbesøke et annet datasett som vi har jobbet med før: Helsingfors-regionens befolkningsrutenett som vi ble kjent med i [leksjon 2](../lesson-2/vector-data-io), og som du brukte under [øvelse 3](../lesson-3/exercise-3). Vi kan laste laget direkte fra [HSY’s åpne data WFS-endepunkt](https://hri.fi/):

```{code-cell} python
# For å ignorere SSL-sertifikatproblemet
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
population_grid = (
    geopandas.read_file(
        "https://kartta.hsy.fi/geoserver/wfs"
        "?service=wfs"
        "&version=2.0.0"
        "&request=GetFeature"
        "&typeName=asuminen_ja_maankaytto:Vaestotietoruudukko_2020"
        "&srsName=EPSG:4326"
        "&bbox=24.6,60.1,25.2,60.4,EPSG:4326"
    )
    .set_crs("EPSG:4326")
)
population_grid.head()
```

La oss først rengjøre dataframen: fjern alle kolonner vi ikke trenger, og
gi de gjenværende nye navn til engelsk.

```{code-cell} python
population_grid = population_grid[["index", "asukkaita", "geometry"]]
population_grid = population_grid.rename(columns={
    "asukkaita": "population"
})
```

:::{admonition} Indekskolonne for koroplettkart
:class: hint

Vi vil bruke `folium.Choropleth` for å vise befolkningsrutenettet. Koroplettkart
er mer enn bare polygon-geometrier, som kan vises som et
`folium.features.GeoJson` lag, akkurat som vi brukte for adressene, ovenfor. Snarere tar klassen seg av kategorisering av data, legger til en legende, og
noen flere små oppgaver for å raskt lage vakre temakart.

Klassen forventer et inngangsdatasett som har en eksplisitt, `str`-type, indeks
kolonne, da den behandler det geografiske inngangen og det tematiske inngangen som separate
datasett som må samles (se også, nedenfor, hvordan vi spesifiserer både
`geo_data` og `data`).

En god tilnærming for å lage en slik kolonne er å kopiere dataframens indeks
til en ny kolonne, for eksempel `id`.
:::


```{code-cell} python
population_grid["id"] = population_grid.index.astype(str)
```

Nå kan vi lage koroplettlaget for polygoner, og legge det til et kartobjekt.
På grunn av den litt komplekse arkitekturen til *Folium*, må vi gi en
rekke parametere:
- `geo_data` og `data`, geografiske og tematiske inngangsdatasett,
  henholdsvis. Kan være den samme `geopandas.GeoDataFrame`.
- `columns`: en tuple av navnene på relevante kolonner i `data`: en unik
  indekskolonne, og kolonnen som inneholder tematiske data
- `key_on`: hvilken kolonne i `geo_data` som skal brukes for å koble `data` (dette er
  i utgangspunktet identisk med `columns`, bortsett fra at det bare er den første verdien)

```{code-cell} python
interactive_map = folium.Map(
    location=(60.17, 24.94),
    zoom_start=12
)

population_grid_layer = folium.Choropleth(
    geo_data=population_grid,
    data=population_grid,
    columns=("id", "population"),
    key_on="feature.id"
)
population_grid_layer.add_to(interactive_map)

interactive_map
```


For å gjøre kartet litt finere, la oss fortsatt be om flere kategorier (`bins`),
endre fargeområdet (ved hjelp av `fill_color`), sett linjetykkelsen til null,
og legg et lag navn til legenden:


```{code-cell} python
interactive_map = folium.Map(
    location=(60.17, 24.94),
    zoom_start=12
)

population_grid_layer = folium.Choropleth(
    geo_data=population_grid,
    data=population_grid,
    columns=("id", "population"),
    key_on="feature.id",

    bins=9,
    fill_color="YlOrRd",
    line_weight=0,
    legend_name="Befolkning, 2020",

    highlight=True
)
population_grid_layer.add_to(interactive_map)

interactive_map
```

### Legg til en tooltip til et koroplettkart

I et slikt interaktivt kart, ville det være fint å vise verdien av hver
rutenett polygon når du holder musepekeren over den. *Folium* støtter ikke
dette out-of-the-box, men med en enkel triks kan vi utvide funksjonaliteten:
Vi legger til et gjennomsiktig polygonlag ved hjelp av en 'grunnleggende' `folium.features.GeoJson`,
og konfigurerer den til å vise tooltips.

Vi kan beholde `map` vi laget ovenfor, og bare legge til et annet lag på den.

```{code-cell} python
# folium GeoJson lag forventer en stylingfunksjon,
# som mottar hver av kartets funksjon og returnerer
# en individuell stil. Den kan imidlertid også returnere en
# statisk stil:
def style_function(feature):
    return {
        "color": "transparent",
        "fillColor": "transparent"
    }


# Mer komplekse tooltips kan lages ved hjelp av
# `folium.features.GeoJsonTooltip` klassen. Nedenfor bruker vi
# dens mest grunnleggende funksjoner: `fields` spesifiserer hvilke kolonner
# som skal vises, `aliases` hvordan de skal være merket.
tooltip = folium.features.GeoJsonTooltip(
    fields=("population",),
    aliases=("Befolkning:",)
)


tooltip_layer = folium.features.GeoJson(
    population_grid,
    style_function=style_function,
    tooltip=tooltip
)
tooltip_layer.add_to(interactive_map)

interactive_map
```


:::{admonition} Python-pakker for interaktive (web) kart
:class: note

*Folium* er bare en av mange pakker som gir en enkel måte å lage interaktive kart ved hjelp av data lagret i (geo-)pandas dataframer. Andre interessante biblioteker inkluderer:

- [GeoViews](https://geoviews.org/),
- [Mapbox GL for Jupyter](https://github.com/mapbox/mapboxgl-jupyter),
- [Bokeh](https://docs.bokeh.org/en/latest/docs/gallery.html),
- [Plotly Express](https://plotly.com/python/maps/), og mange flere.
:::