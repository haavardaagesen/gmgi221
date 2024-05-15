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

# Spørringer om punkt-i-polygon

Å finne ut om et bestemt punkt er plassert innenfor eller utenfor et område,
eller å finne ut om en linje skjærer med en annen linje eller polygon er
grunnleggende geospatiale operasjoner som ofte brukes f.eks. for å velge
data basert på plassering. Slike romlige spørringer er en av de typiske
første trinnene i arbeidsflyten når du gjør romlig analyse. Å utføre en
romlig join (vil bli introdusert senere) mellom to romlige datasett er
en av de mest typiske applikasjonene der Point in Polygon (PIP) spørring
brukes.

For videre lesing om PIP og andre geometriske operasjoner,
se kapittel 4.2 i Smith, Goodchild & Longley: [Geospatial Analysis - 6th edition](https://www.spatialanalysisonline.com/HTML/index.html).


## Hvordan sjekke om et punkt er inne i en polygon?

Beregningsteknisk er det mest vanlig å oppdage om et punkt er inne i en polygon ved å bruke en spesifikk formel kalt [Ray Casting-algoritmen](https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm).
Heldigvis trenger vi ikke å lage en slik funksjon selv for
utføre Point in Polygon (PIP) spørring. I stedet kan vi dra
fordel av [Shapely's binære predikater](https://shapely.readthedocs.io/en/stable/manual.html#binary-predicates)
som kan evaluere de topologiske forholdene mellom geografiske
objekter, som PIP som vi er interessert i her.

## Spørringer om punkt-i-polygon på `shapely` geometrier

Det er stort sett to måter å utføre PIP på i Shapely:

1. ved hjelp av en funksjon kalt
   [within()](https://shapely.readthedocs.io/en/stable/manual.html#object.within)
   som sjekker om et punkt er innenfor en polygon
2. ved hjelp av en funksjon kalt
   [contains()](https://shapely.readthedocs.io/en/stable/manual.html#object.contains)
   som sjekker om en polygon inneholder et punkt

:::{note}
Selv om vi snakker her om **Point** i Polygon
operasjon, er det også mulig å sjekke om en LineString eller Polygon er
inne i en annen Polygon.
:::


La oss først lage et par punktgeometrier:

```{code-cell} python
import shapely.geometry
point1 = shapely.geometry.Point(24.952242, 60.1696017)
point2 = shapely.geometry.Point(24.976567, 60.1612500)
```

... og en polygon:

```{code-cell} python
polygon = shapely.geometry.Polygon(
    [
        (24.950899, 60.169158),
        (24.953492, 60.169158),
        (24.953510, 60.170104),
        (24.950958, 60.169990)
    ]
)
```

```{code-cell} python
print(point1)
print(point2)
print(polygon)
```

La oss sjekke om punktene er `within()` polygonen:

```{code-cell} python
point1.within(polygon)
```

```{code-cell} python
point2.within(polygon)
```

Det ser ut til at det første punktet er inne i polygonen, men det andre er det ikke.

Vi kan snu logikken til oppslaget: I stedet for å sjekke om punktet er
innenfor polygonen, kan vi også spørre om polygonen `contains()` punktet:

```{code-cell} python
polygon.contains(point1)
```

```{code-cell} python
polygon.contains(point2)
```

:::{hint}
De to måtene å sjekke det romlige forholdet er komplementære og gir
ekvivalente resultater;
[`contains()`](https://shapely.readthedocs.io/en/stable/manual.html#object.contains)
er inverse til
[`within()`](https://shapely.readthedocs.io/en/stable/manual.html#object.within),
og omvendt.

Så, hvilken en skal du bruke? Vel, det avhenger av:

-  hvis du har **mange punkter og bare en polygon** og du prøver å finne ut
   hvilken av dem som er inne i polygonen: Du må kanskje iterere over punktene
   og sjekke ett om gangen om det er **`within()`** polygonen.
-  hvis du har **mange polygoner og bare ett punkt** og du vil finne ut
   hvilket polygon som inneholder punktet: Du må kanskje iterere over polygonene
   til du finner et polygon som **`contains()`** det spesifiserte punktet
:::


## Spørringer om punkt-i-polygon på `geopandas.GeoDataFrame`s

I det følgende praktiske eksempelet finner vi ut hvilke av adressene vi fikk
i [geokodingseksjonen](geocoding-in-geopandas) som ligger innenfor et bestemt
bydistrikt i Helsinki.

Datamengden vi bruker er fra [Helsinki Region Infoshare](https://hri.fi/data/en_GB/dataset/helsingin-piirijako), og lisensiert under en [Creative-Commons-Attribution-4.0](https://creativecommons.org/licenses/by/4.0/) lisens.

```{code-cell} python
import pathlib
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```

```{code-cell} python
import geopandas

bydeler = geopandas.read_file(
    DATA_DIRECTORY / "helsinki_city_districts" / "helsinki_city_districts_2021.gpkg"
)
bydeler.head()
```

```{code-cell} python
bydeler.plot()
```

Spesielt ønsker vi å finne ut hvilke punkter som er innenfor 'Eteläinen'
('sør') bydelen. La oss begynne med å få et separat datasett for
denne distriktet, laste adressene data, og plotte et flerlagskart
som viser alle distriktene, 'Eteläinen' distriktet og alle punktene i
ett kart:

```{code-cell} python
sør_distrikt = bydeler[bydeler.name == "Eteläinen"]
sør_distrikt
```

```{code-cell} python
adresser = geopandas.read_file(DATA_DIRECTORY / "adresser.gpkg")
```

:::{admonition} Plotting flere kartlag
:class: hint

For å plotte flere kartlag i én figur, bruk `ax` parameter for å spesifisere i
hvilke *akser* data skal plottes. Vi brukte dette i [leksjon 7 av
Geo-Python](https://geo-python-site.readthedocs.io/en/latest/notebooks/L7/matplotlib.html) for å legge til tekst i et plot eller modifisere akseegenskaper.

Den enkleste måten å få en *akse* er å lagre den første `plot()`’s
returverdi (se nedenfor). Et annet alternativ er å lage [`subplots()`](https://geo-python-site.readthedocs.io/en/latest/notebooks/L7/advanced-plotting.html#using-subplots), muligens med bare en rad og en kolonne.
:::

```{code-cell} python
akser = bydeler.plot(facecolor="grå")
sør_distrikt.plot(ax=akser, facecolor="rød")
adresser.plot(ax=akser, color="blå", markersize=5)
```

Noen punkter er innenfor 'Eteläinen' distriktet, men andre er det ikke. For å finne
ut hvilke som er de inne i distriktet, kan vi bruke en **punkt-i-polygon
spørring**, denne gangen på hele `geopandas.GeoDataFrame`. Dens metode
`within()` returnerer Boolsk (`True`/`False`) verdier som indikerer om eller ikke
en rad's geometri er inneholdt i den angitte *andre* geometrien:


:::{admonition} geometri vs. geometrikolonne
:class: caution

I eksempelet nedenfor bruker vi `sør.at[0, "geometry"]` for å få en enkelt
verdi, en `shapely.geometry.Polygon`, i stedet for en hel kolonne (en
`GeoSeries`). Dette er for å matche hver rad's geometri av hele
`adresser` data rammen mot *den samme polygonen*. Hvis, i motsetning, vi ville
kjøre `within()` mot en kolonne, ville operasjonen bli utført radvis,
dvs. det første adressepunktet ville bli sjekket mot den første polygonen, det
andre adressepunktet mot den andre polygonen, og så videre.

Sjekk [dokumentasjonen for
`within()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.within.html)
for å lære mer!
:::

```{code-cell} python
adresser.within(sør_distrikt.at[0, "geometry"])
```

Denne listen med Boolsk verdier, også kalt en *maske-array* kan brukes til å filtrere
input data-rammen:

```{code-cell} python
adresser_i_sør_distriktet = adresser[
    adresser.within(sør_distrikt.at[0, "geometry"])
]
adresser_i_sør_distriktet
```

Til slutt, la oss plotte denne listen med adresser en gang til for visuelt å verifisere
at alle av dem, faktisk, er plassert innenfor 'Eteläinen' bydistriktet:

```{code-cell} python
akser = bydeler.plot(facecolor="grå")
sør_distrikt.plot(ax=akser, facecolor="rød")

adresser_i_sør_distriktet.plot(
    ax=akser,
    color="gull",
    markersize=5
)
```

Perfekt! Nå sitter vi igjen med bare de (gyldne) punktene som faktisk er
inne i den røde polygonen. Det er akkurat det vi ønsket!