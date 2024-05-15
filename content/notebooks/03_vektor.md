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

# Vektor Data I/O

Et av de første trinnene i mange analysearbeidsflyter er å lese data fra en fil, et av de siste trinnene skriver ofte data til en utdatafil. Til skrekk og gru for mange geoinformatikkforskere, finnes det mange filformater for GIS-data: den gamle og forhatte, men også elskede og etablerte [ESRI Shapefile](https://en.wikipedia.org/wiki/Shapefile), den universelle [Geopackage (GPKG)](https://en.wikipedia.org/wiki/GeoPackage), og den web-optimaliserte [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) er bare noen av de mer kjente eksemplene.

Frykt ikke, Python kan lese dem alle (ingen garantier, though)! 

De fleste av dagens Python GIS-pakker er avhengige av [GDAL/OGR](https://gdal.org/)-bibliotekene, som det finnes moderne grensesnitt for i form av Python-pakkene [fiona](https://fiona.readthedocs.io) og [rasterio](https://rasterio.readthedocs.io).

I dag skal vi konsentrere oss om vektordata, så la oss først ta en nærmere titt på fionas kapabiliteter, og deretter importere og eksportere data ved hjelp av [geopandas](https://geopandas.org/), som bruker fiona under hetta.


---

:::{admonition} Definere en konstant for datamappen
:class: note

For å gjøre det lettere å håndtere stiene til inngangs- og utgangsdatafiler, er det en god vane å [definere en konstant som peker på datamappen](managing-file-paths) øverst i en notatbok:

:::

```{code-cell} python
import pathlib 
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```


---

## Filformater

Fiona kan lese (nesten) alle geospatiale filformater, og skrive mange av dem. For å finne ut nøyaktig hvilke (det kan avhenge av den lokale installasjonen og versjonen), kan vi skrive ut listen over dens filformatdrivere:

```{code-cell} python
import fiona
fiona.supported_drivers
```

:::{hint}
I denne listen markerer `r` filformater som Fiona kan *l*ese, og `w` formater det kan *s*krive. En `a` markerer formater som Fiona kan *a*ppendere nye data til eksisterende filer.

Merk at hver av de listede 'formatene' faktisk er navnet på driverimplementasjonen, og mange av driverne kan åpne flere relaterte filformater.

Mange flere 'eksotiske' filformater kan kanskje ikke vises i denne listen over din lokale installasjon, fordi du må installere ekstra biblioteker. Du kan finne en fullstendig liste over filformater som støttes av GDAL/OGR (og Fiona) på nettsiden: [gdal.org/drivers/vector/](https://gdal.org/drivers/vector/).
:::


### Lesing og skriving av geospatiale data

Fiona gir veldig lavt nivå tilgang til geodatafiler. Dette er noen ganger nødvendig, men i typiske analysearbeidsflyter er det mer praktisk å bruke et høyere nivå bibliotek. Den mest brukte for geospatiale vektordata er [geopandas](https://geopandas.org). Som nevnt ovenfor, bruker den Fiona for lesing og skriving av filer, og støtter dermed de samme filformatene.

For å lese data fra en *GeoPackage* -fil til en `geopandas.GeoDataFrame` (en geospatiale versjon av en `pandas.DataFrame`), bruk `geopandas.read_file()`:

```{code-cell} python
import geopandas
kommuner = geopandas.read_file(
    DATA_DIRECTORY / "finland_municipalities" / "finland_municipalities_2021.gpkg"
)
kommuner.head()
```

Å lese en lokal GPKG-fil er mest sannsynlig den enkleste oppgaven for en GIS-pakke. Imidlertid, i perfekt Python 'Swiss pocket knife' stil, kan geopandas også lese Shapefiles **innenfor en ZIP-arkiv**, og/eller direkte **fra en Internett-URL**. For eksempel, nedlasting, utpakking og åpning av et datasett av NUTS-regioner fra [European Union’s GISCO/eurostat download page](https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts) er en linje med kode:

```{code-cell} python
nuts_regions = geopandas.read_file("https://gisco-services.ec.europa.eu/distribution/v2/nuts/shp/NUTS_RG_60M_2021_3035.shp.zip")
nuts_regions.head()
```

```{code-cell} python
nuts_regions = geopandas.read_file(DATA_DIRECTORY / "europe_nuts_regions.geojson")
nuts_regions.head()
```

#### Skrive geospatiale data til en fil

Å skrive data til en fil er like enkelt: bruk bare [`to_file()` metoden](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_file.html#geopandas.GeoDataFrame.to_file) til en `GeoDataFrame`.

Hvis vi vil beholde en lokal kopi av NUTS-region datasettet vi nettopp åpnet 'on-the-fly' fra en internettadresse, lagrer følgende dataene til en GeoJSON-fil (filformatet blir gjettet fra filnavnet):

```{code-cell} python
nuts_regions.to_file(DATA_DIRECTORY / "europe_nuts_regions.geojson")
```

:::{note}

Lesing og skriving av geospatiale data fra eller til en fil er nesten identisk for alle filformater som støttes av geopandas, fiona, og GDAL. Sjekk ut [geopandas’ dokumentasjon](https://geopandas.org/en/stable/docs/user_guide/io.html) for tips om hvordan du kan finjustere lesing eller skriving av en fil, og hvordan du kan bruke forskjellige filtre (f.eks. begrensningsbokser).
:::


### Lesing og skriving fra og til databaser (RDBMS)

Geopandas har innebygd støtte for lese/skrive-tilgang til PostgreSQL/PostGIS-databaser, ved hjelp av dens [`geopandas.read_postgis()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_postgis.html) funksjon og [`GeoDataFrame.to_postgis()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_postgis.html) metode. For databasetilkoblingen kan du bruke, for eksempel, `sqlalchemy`-pakken.

```{code-cell} python
import sqlalchemy
DB_CONNECTION_URL = "postgresql://myusername:mypassword@myhost:5432/mydatabase";
db_engine = sqlalchemy.create_engine(DB_CONNECTION_URL)

countries = geopandas.read_postgis(
    "SELECT name, geometry FROM countries",
    db_engine
)
countries.to_postgis(
    "new_table", 
    db_engine
)
```

### Lesing av data direkte fra en WFS (Web feature service) endepunkt

Geopandas kan også lese data direkte fra en WFS-endepunkt, som for eksempel geodata-APIene til [Helsinki Region Infoshare](https://hri.fi). Å konstruere en gyldig WFS-URI (adresse) er ikke en del av dette kurset (men sjekk, for eksempel, egenskapene til et lag lagt til QGIS).

Følgende kode laster et befolkningsrutenett fra Helsinki fra 2022. Parameterne kodet inn i WFS-adressen spesifiserer lagets navn, en begrensningsboks, og det forespurte referansesystemet.

```{code-cell} python
population_grid = geopandas.read_file(
    "https://kartta.hsy.fi/geoserver/wfs"
    "?service=wfs"
    "&version=2.0.0"
    "&request=Get
    "&typeName=asuminen_ja_maankaytto:Vaestotietoruudukko_2022"
    "&srsName=EPSG:3879"
    "&bbox=25494767,6671328,25497720,6673701,EPSG:3879",
    crs="EPSG:3879"
)
population_grid.head()
```

```{code-cell} python
population_grid = geopandas.read_file(
    "https://avoidatastr.blob.core.windows.net/avoindata/AvoinData/"
    "6_Asuminen/Vaestotietoruudukko/Shp/Vaestotietoruudukko_2021_shp.zip"
)
population_grid.head()
```
