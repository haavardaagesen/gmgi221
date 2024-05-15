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

# Geokoding i geopandas

Geopandas støtter geokoding via et bibliotek kalt
[geopy](http://geopy.readthedocs.io/), som må være installert for å bruke
[geopandas ' `geopandas.tools.geocode()`
funksjon](https://geopandas.org/en/stable/docs/reference/api/geopandas.tools.geocode.html).
`geocode()` forventer en `liste` eller `pandas.Series` av adresser (strenger) og
returnerer en `GeoDataFrame` med løste adresser og punktgeometrier.

La oss prøve dette ut.

Vi vil geokode adresser lagret i en semikolon-separert tekstfil kalt
`addresses.txt`. Disse adressene ligger i Helsingforsregionen i Sør-Finland.

```{code-cell} python
import pathlib
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```

```{code-cell} python
import pandas
addresses = pandas.read_csv(
    DATA_DIRECTORY / "helsinki_addresses" / "addresses.txt",
    sep=";"
)

addresses.head()
```

Vi har en `id` for hver rad og en adresse i `addr` kolonnen.


## Geokode adresser ved hjelp av *Nominatim*

I vårt eksempel vil vi bruke *Nominatim* som en *geokodingstilbyder*. [*Nominatim*](https://nominatim.org/) er et bibliotek og tjeneste som bruker OpenStreetMap-data, og drives av OpenStreetMap Foundation. Geopandas '
[`geocode()`
funksjon](https://geopandas.org/en/stable/docs/reference/api/geopandas.tools.geocode.html) støtter den naturlig.

:::{admonition} Rettferdig bruk
:class: note

[Nominatims brukervilkår](https://operations.osmfoundation.org/policies/nominatim/)
krever at brukere av tjenesten sørger for at de ikke sender mer hyppige
forespørsler enn en per sekund, og at en tilpasset **bruker-agent** streng er
festet til hver forespørsel.

Geopandas' implementering lar oss spesifisere en `user_agent`; biblioteket tar også
hånd om å respektere hastighetsbegrensningen til Nominatim.

Å slå opp en adresse er en ganske kostbar databaseoperasjon. Derfor er det,
noen ganger, den offentlige og gratis å bruke Nominatim-serveren tar litt lenger tid å
svare. I dette eksempelet legger vi til en parameter `timeout=10` for å vente opptil 10
sekunder for et svar.
:::


```{code-cell} python
import geopandas

geocoded_addresses = geopandas.tools.geocode(
    addresses["addr"],
    provider="nominatim",
    user_agent="autogis2023",
    timeout=10
)
geocoded_addresses.head()
```

Et voilà! Som et resultat mottok vi en `GeoDataFrame` som inneholder en analysert
versjon av våre originale adresser og en `geometry` kolonne av
`shapely.geometry.Point`s som vi kan bruke, for eksempel, for å eksportere dataene til
et geospatialt dataformat.

Imidlertid ble `id`-kolonnen forkastet i prosessen. For å kombinere input
datasettet med resultatsettet vårt, kan vi bruke pandas' [*join*
operasjoner](https://pandas.pydata.org/docs/user_guide/merging.html).


## Bli med i data frames

:::{admonition} Bli med i datasett ved hjelp av pandas
:class: note

For en omfattende oversikt over forskjellige måter å kombinere data rammer og
Serier basert på sett teori, ta en titt på pandas dokumentasjon om [merge,
join og
concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html).
:::


Å bli med data fra to eller flere data frames eller tabeller er en vanlig oppgave i mange
(romlige) dataanalysearbeidsflyter. Som du kanskje husker fra våre tidligere
leksjoner, kan kombinering av data fra forskjellige tabeller basert på felles **nøkkel** attributt
gjøres enkelt i pandas/geopandas ved hjelp av [`merge()`
funksjonen](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html).
Vi brukte denne tilnærmingen i [øvelse 6 i Geo-Python
kurset](https://geo-python-site.readthedocs.io/en/latest/lessons/L6/exercise-6.html#joining-data-from-one-dataframe-to-another).

Men, noen ganger er det nyttig å bli med to data frames sammen basert på deres
**indeks**. Data frames må ha **samme antall poster** og
**dele den samme indeksen** (enkelt sagt, de skal ha samme rekkefølge av rader).

Vi kan bruke denne tilnærmingen, her, for å bli med informasjon fra den originale data
rammen `addresses` til de geokodede adressene `geocoded_addresses`, rad for rad.
`join()`-funksjonen, som standard, blir med to data frames basert på indeksen deres.
Dette fungerer korrekt for eksemplet vårt, da rekkefølgen på de to data frames er
identisk.

```{code-cell} python
geocoded_addresses_with_id = geocoded_addresses.join(addresses)
geocoded_addresses_with_id
```

Utdataen fra `join()` er en ny `geopandas.GeoDataFrame`:

```{code-cell} python
type(geocoded_addresses_with_id)
```

Den nye data rammen har alle originale kolonner pluss nye kolonner for `geometry`
og for en analysert `adresse` som kan brukes til å spot-sjekke resultatene.

:::{note}
Hvis du skulle gjøre join den andre veien, dvs. `addresses.join(geocoded_addresses)`, ville utdata være en `pandas.DataFrame`, ikke en `geopandas.GeoDataFrame`.
:::


---


Det er nå enkelt å lagre det nye datasettet som en geospatial fil, for eksempel, i
*GeoPackage* format:

```{code-cell} python
:tags: ["remove-input", "remove-output"]

# slett en muligens eksisterende fil, da den skaper
# problemer i tilfelle sphinx kjøres gjentatte ganger
try:
    (DATA_DIRECTORY / "addresses.gpkg").unlink()
except FileNotFoundError:
    pass
```

```{code-cell} python
geocoded_addresses.to_file(DATA_DIRECTORY / "addresses.gpkg")
```