# 📥 Øving 3

I denne øvingen skal du jobbe med å lese og bruke romlige data ved hjelp av GeoPandas.

Øvingsoppgaven finner du på Canvas under Oppgaver, eller på [dette GitHub-repoet](https://github.com/GMGI221-2024/gmgi221-ovinger).

Last den ned, åpne den i Jupyter Notebooks/Lab eller den editoren du bruker og følg instruksjonene i Notebooken. Lever den så inn på Canvas etter du har endret navn til "oving3-ditt_navn.ipynb".

## Tips til oppgaven:

### Pandas `apply()`-metoden:

Pandas' DataFrames har en metode `apply()` som kjører en brukerdefinert funksjon på hver rad eller på hver kolonne (avhengig av `axis`-parameteren, hvis `axis=1`, fungerer `apply()` på rader).

Resultatene av å kjøre funksjonen gjentatte ganger (parallelt, for å være presis) samles i en pandas.GeoSeries som er returverdien av `apply()` og kan tilordnes til en ny kolonne eller rad.

For eksempel kan dette brukes for å lage punkt-geometrier:

```python
def create_point(row):
    """Create a Point geometry from a row with x and y values."""
    point = shapely.geometry.Point(row["x"], row["y"])
    return point

point_series = data.apply(create_point, axis=1)
```
#### Bruke en anonym `lambda`-funksjon med `apply()`

Til slutt, for enkle funksjoner som passer på en enkelt linje, kan vi sende funksjonen inn i såkalt 'lambda-notasjon'. Lambda-funksjoner følger syntaksen `lambda argumenter: returverdi`, dvs. nøkkelordet `lambda` etterfulgt av ett eller flere, kommaseparerte argumentnavn (inputvariabler), et kolon (:), og returverdi-setningen (f.eks. en beregning). En lambda-funksjon som aksepterer to argumenter og returnerer summen av dem, vil se slik ut: `lambda a, b: (a + b)`.

Lambda-funksjoner kan bare brukes der de er definert, men tilbyr en praktisk snarvei for å slippe separate funksjoner for enkle uttrykk. De er svært vanlige i datavitenskapsprosjekter, men bør ikke brukes for mye: som en tommelfingerregel, ikke bruk lambda-funksjoner hvis koden deres ikke passer på en (kort) linje.

Les mer om lambda-funksjoner i [Python-dokumentasjonen](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)


### Converting a `pandas.DataFrame`  into a `geopandas.GeoDataFrame`

Sometimes, we work with data that are in a non-spatial format (such as Excel
or CSV spreadsheets) but contain information on the location of records, for
instance, in columns for longitude and latitude values. While geopandas’s
`read_file()` function can read some formats, often, the safest way is to use
pandas to read the data set and then convert it to a `GeoDataFrame`.

Let’s assume, we read the following table using `pandas.read_csv()` into a
variable `df`:

```python
:tags: ["remove-input"]

# sample data
import pandas
df = pandas.DataFrame({
    "longitude": [24.9557, 24.8353, 24.9587],
    "latitude": [60.1555, 60.1878, 60.2029]
})
```

```python
df
```

The `geopandas.GeoDataFrame()` constructor accepts a `pandas.DataFrame` as an
input, but it does not automatically fill the `geometry` column. However, the
library comes with a handy helper function `geopandas.points_from_xy()`. As we
all know, a spatial data set should always have a coordinate reference system
(CRS) defined; we can specify the CRS of the input data, here, too:

```python

import geopandas

gdf = geopandas.GeoDataFrame(
    df,
    geometry=geopandas.points_from_xy(df.longitude, df.latitude),
    crs="EPSG:4326"
)

gdf
```

Now, we have a ‘proper‘ `GeoDataFrame` with which we can do all geospatial
operations we would want to do.



### Creating a new `geopandas.GeoDataFrame`: alternative 1

Sometimes, it makes sense to start from scratch with an empty data set and
gradually add records. Of course, this is also possible with geopandas’ data
frames, that can then be saved as a new geopackage or shapefile.

First, create a completely empty `GeoDataFrame`:

```python
import geopandas

new_geodataframe = geopandas.GeoDataFrame()
```

Then, create shapely geometry objects and insert them into the data frame. To
insert a geometry object into the `geometry` column, and a name into the `name`
column, in a newly added row, use:

```python
import shapely.geometry
polygon = shapely.geometry.Polygon(
    [
        (24.9510, 60.1690),
        (24.9510, 60.1698),
        (24.9536, 60.1698),
        (24.9536, 60.1690)
    ]
)
name = "Senaatintori"

new_geodataframe.loc[
    len(new_geodataframe),  # in which row,
    ["name", "geometry"]    # in which columns to save values
] = [name, polygon]

new_geodataframe
```

Before saving the newly created dataset, don’t forget to define a cartographic
reference system for it. Otherwise, you will have trouble reusing the file in
other programs:

```python
new_geodataframe.crs = "EPSG:4326"
```

:::{hint}
In the example above, we used the `len(new_geodataframe)` as a row index
(which, in a newly created data frame is equivalent to the row number).  Since
rows are counted from 0, the number of rows (length of data frame) is one
greater than the address of the last row. This expression, thus, always adds a
new row, independent of the actual length of the data frame.

Note, that, strictly speaking, the index is independent from the row number,
but in newly created data frames there are identical.
:::


### Creating a new `geopandas.GeoDataFrame`: alternative 2

Often, it is more convenient, and more elegant, to first create a dictionary
to collect data, that can then be converted into a data frame all at once.

For this, first define a `dict` with the column names as keys, and empty `list`s
as values:

```python
data = {
    "name": [],
    "geometry": []
}
```

Then, fill the dict with data:

```python
import shapely.geometry

data["name"].append("Senaatintori")
data["geometry"].append(
    shapely.geometry.Polygon(
        [
            (24.9510, 60.1690),
            (24.9510, 60.1698),
            (24.9536, 60.1698),
            (24.9536, 60.1690)
        ]
    )
)
```

Finally, use this dictionary as input for a new `GeoDataFrame`. Don’t forget to
specify a CRS:

```python
new_geodataframe = geopandas.GeoDataFrame(data, crs="EPSG:4326")
new_geodataframe
```

---

:::{note}
These two approaches result in identical `GeoDataFrame`s. Sometimes, one
technique is more convenient than the other. You should always evaluate
different ways of solving a problem, and find the most appropriate and efficient
solution (there is **always** more than one possible solution).
:::