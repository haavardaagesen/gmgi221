---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
    split_at_heading: true
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Overleggsanalyse

Overleggsanalyser er GIS-operasjoner der to eller flere vektorlag er
kombinert for å produsere nye geometrier. Typiske overleggsoperasjoner inkluderer *union*,
*intersection*, og *difference* - navngitt etter resultatet av kombinasjonen av
to lag.


:::{figure} ../../static/images/lesson-4/overlay-operations_700x200px.svg
:alt: Fire paneler som viser unionen, interseksjonen, symmetrisk differanse og differanse av to geometrier.

Romlig overlegg med to inngangsvektorlag (rektangel, sirkel). Det resulterende vektorlaget vises i grønt. *Kilde: [QGIS dokumentasjon](https://docs.qgis.org/latest/en/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html#figure-overlay-operations)*
:::


I denne opplæringen vil vi utføre en overleggsanalyse for å velge de polygon
cellene i et nett datasett som ligger innenfor bygrensene i Helsinki. For denne
øvelsen, bruker vi to inngangs datasett: et nett av statistiske polygoner med
reisetiden til Helsingfors jernbanestasjon, som dekker hele storbyområdet (`helsinki_region_travel_times_to_railway_station.gpkg`) og et polygon
datasett (med en funksjon) av området kommunen Helsingfors dekker
(`helsinki_municipality.gpkg`). Begge filene er i logisk navngitte undermapper
av `DATA_DIRECTORY`.

```{code-cell} python
import pathlib 
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```

```{code-cell} python
import geopandas

nett = geopandas.read_file(
    DATA_DIRECTORY
    / "helsinki_region_travel_times_to_railway_station"
    / "helsinki_region_travel_times_to_railway_station.gpkg"
)

helsinki = geopandas.read_file(
    DATA_DIRECTORY / "helsinki_municipality" / "helsinki_municipality.gpkg"
)
```

La oss gjøre en rask overleggsvisualisering av de to lagene:

```{code-cell} python
# Plott lagene
ax = nett.plot(facecolor="gray")
helsinki.plot(ax=ax, facecolor="None", edgecolor="blue")
```

Her er det grå området Reisetid Matrise - et datasett som inneholder 13231
rutenett kvadrater (13231 rader med data) som dekker Helsingfors-regionen, og det blå området representerer kommunen Helsingfors. Målet vårt er å utføre en overleggsanalyse og velge geometriene fra rutenett polygonlaget som krysser
med Helsingfors kommune polygon.

Når du utfører overleggsanalyse, er det viktig å først sjekke at CRS
av lagene matcher. Overleggsvisualiseringen indikerer at alt burde være
ok (lagene plottes pent oppå hverandre). Men, la oss
likevel sjekke om crs matcher ved hjelp av Python:

```{code-cell} python
# Sjekk crs av kommunen polygon
print(helsinki.crs)
```

```{code-cell} python
# Sørg for at CRS matcher, hvis ikke løft en AssertionError
assert helsinki.crs == nett.crs, "CRS skiller seg mellom lagene!"
```

Faktisk, det gjør de. Vi er nå klare til å utføre en overleggsanalyse mellom disse lagene. 

Vi vil lage et nytt lag basert på rutenett polygoner som `intersect` med vår
Helsingfors lag. Vi kan bruke en metode `overlay()` av en `GeoDataFrame` for å utføre
overleggsanalysen som tar som en input 1) andre GeoDataFrame, og 2)
parameter `how` som kan brukes til å kontrollere hvordan overleggsanalysen er
utført (mulige verdier er `'intersection'`, `'union'`,
`'symmetric_difference'`, `'difference'`, og `'identity'`):

```{code-cell} python
intersection = nett.overlay(helsinki, how="intersection")
```

La oss plotte dataene våre og se hva vi har:

```{code-cell} python
intersection.plot(color="b")
```

Som et resultat har vi nå bare de rutenett cellene som krysser med Helsingfors
grenser. Hvis du ser nøye etter, kan du også observere at **rutenett cellene er
klippet basert på grensen.**

- Hva med dataattributter? La oss se hva vi har:

```{code-cell} python
intersection.head()
```

Som vi kan se, på grunn av overleggsanalysen, inneholder datasettet attributtene
fra begge input lagene.

La oss lagre resultatrutenettet vårt som en GeoPackage.

```{code-cell} python
intersection.to_file(
    DATA_DIRECTORY / "intersection.gpkg",
    layer="travel_time_matrix_helsinki_region"
)
```

Det er mange flere eksempler på forskjellige typer overleggsanalyse i
[Geopandas dokumentasjon](http://geopandas.org/set_operations.html) hvor du
kan gå og lære mer.