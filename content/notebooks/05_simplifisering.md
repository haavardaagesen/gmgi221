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

# Forenkling av geometrier


Noen ganger kan det være nyttig å kunne forenkle geometrier. Dette kan være
noe å vurdere for eksempel når du har veldig detaljerte romlige egenskaper
som dekker hele verden. Hvis du lager et kart som dekker hele verden, er det unødvendig å ha veldig detaljerte geometrier fordi det er rett og slett
umulig å se de små detaljene fra kartet ditt. Videre tar det en
lang tid å faktisk gjengi et stort antall funksjoner til et kart. Her vil vi
se hvordan det er mulig å forenkle geometriske egenskaper i Python.

Som et eksempel vil vi bruke data som representerer Amazonas-elven i Sør-Amerika,
og forenkle dens geometrier.

La oss først lese dataene og se hvordan elven ser ut:

```{code-cell} python
import pathlib 
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```


```{code-cell} python
import geopandas

amazon = geopandas.read_file(DATA_DIRECTORY / "amazon_river" / "amazon_river.gpkg")

amazon.head()
```

```{code-cell} python
amazon.crs
```

```{code-cell} python
amazon.plot()
```

LineString som presenteres her er ganske detaljert, så la oss se hvordan vi
kan generalisere dem litt. Som vi kan se fra koordinatreferansesystemet,
er dataene projisert i et system som bruker [Mercator-projeksjon basert på
SIRGAS-datum](http://spatialreference.org/ref/sr-org/7868/), og meter som en enhet. 

Generalisering kan enkelt gjøres ved å bruke en Shapely funksjon kalt
`.simplify()`. `tolerance` parameteren kan brukes til å justere hvor mye
geometrier skal generaliseres. **Toleranseverdien er knyttet til
koordinatsystemet til geometriene**. Derfor er verdien vi gir her 20 000
**meter** (20 kilometer).


```{code-cell} python
# Generaliser geometri
amazon['simplegeom'] = amazon.simplify(tolerance=20000)

# Sett geometri til å være vår nye forenklede geometri
amazon = amazon.set_geometry('simplegeom')

# Plott 
amazon.plot()
```

Flott! Som et resultat har vi nå forenklet vår LineString ganske betydelig som vi kan se fra kartet.