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

# Statiske kart

I løpet av de siste ukene har vi allerede blitt kjent med plotting
grunnleggende statiske kart ved hjelp av
[`geopandas.GeoDataFrame.plot()`](http://geopandas.org/mapping.html), for
eksempel i leksjonene [2](../lesson-2/geopandas-an-introduction),
[3](../lesson-3/spatial-join), og [4](../lesson-4/reclassifying-data). Vi lærte også
at `geopandas.GeoDataFrame.plot()` bruker `matplotlib.pyplot`
biblioteket, og at [de fleste av argumentene og alternativene blir akseptert av
geopandas](https://matplotlib.org/stable/api/pyplot_summary.html).

For å friske opp hukommelsen om det grunnleggende i å plotte kart, la oss lage et statisk
tilgjengelighetskart over Helsingfors storbyområde, som også viser veier og
metro linjer (tre lag, overlappet hverandre). Husk at inngangsdataene må være i samme koordinatsystem!


## Data

Vi vil bruke tre forskjellige datasett:
- reisetiden til Helsingfors jernbanestasjon vi brukte i [leksjon
  4](../lesson-4/reclassifying-data), som ligger i `DATA_DIRECTORY /
"helsinki_region_travel_times_to_railway_station"`,
- Helsingfors Metro-nettverk, tilgjengelig via WFS fra byens karttjenester,
  og
- et forenklet nettverk av de viktigste veiene i storbyregionen,
  også tilgjengelig via WFS fra samme endepunkt.

```{code-cell}
import pathlib
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```

```{code-cell}
import geopandas
import numpy
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

accessibility_grid = geopandas.read_file(
    DATA_DIRECTORY
    / "helsinki_region_travel_times_to_railway_station"
    / "helsinki_region_travel_times_to_railway_station.gpkg"
)
accessibility_grid["pt_r_t"] = accessibility_grid["pt_r_t"].replace(-1, numpy.nan)

WFS_BASE_URL = (
    "https://kartta.hel.fi/ws/geoserver/avoindata/wfs"
    "?service=wfs"
    "&version=2.0.0"
    "&request=GetFeature"
    "&srsName=EPSG:3879"
    "&typeName={layer:s}"
)

metro = (
    geopandas.read_file(
        WFS_BASE_URL.format(layer="avoindata:Seutukartta_liikenne_metro_rata")
    )
    .set_crs("EPSG:3879")
)
roads = (
    geopandas.read_file(
        WFS_BASE_URL.format(layer="avoindata:Seutukartta_liikenne_paatiet")
    )
    .set_crs("EPSG:3879")
)
```


:::{admonition} Koordinatreferansesystemer
:class: attention

Husk at forskjellige geo-dataframes må være i samme koordinatsystem
før de plottes på samme kart. `geopandas.GeoDataFrame.plot()` utfører ikke
reprosjisering av data automatisk.

Du kan alltid sjekke det med en enkel `assert` uttalelse.
:::

```{code-cell}
:tags: ["raises-exception"]
assert accessibility_grid.crs == metro.crs == roads.crs, "Inndataenes CRS er forskjellige"
```

Hvis flere datasett ikke deler et felles CRS, finn ut først hvilket CRS
de har tildelt (hvis noen!), deretter transformere dataene til et felles referanse
system:

```{code-cell}
accessibility_grid.crs
```

```{code-cell}
metro.crs
```

```{code-cell}
roads.crs
```

```{code-cell}
roads = roads.to_crs(accessibility_grid.crs)
metro = metro.to_crs(accessibility_grid.crs)
```

```{code-cell}
assert accessibility_grid.crs == metro.crs == roads.crs, "Inndataenes CRS er forskjellige"
```


## Plotting et flerlagskart

:::{admonition} Sjekk forståelsen din
:class: hint

Fullfør de neste trinnene i ditt eget tempo (tøm først kodecellene).
Sørg for å gå tilbake til tidligere leksjoner hvis du føler deg usikker på hvordan du fullfører
en oppgave.

- Visualiser et flerlagskart ved hjelp av `geopandas.GeoDataFrame.plot()` metoden;
- først, plott tilgjengelighetsrutenettet ved hjelp av et 'kvantil' klassifiseringsskjema,
- deretter, legg til vei nettverk og metrolinjer i samme plott (husk `ax`
  parameter)
:::


Husk følgende alternativer som kan sendes til `plot()`:
- stil polygonlaget:
    - definer et klassifiseringsskjema ved hjelp av `scheme` parameteren
    - [endre fargekartet ved hjelp av
      `cmap`](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
    - kontroller lagets gjennomsiktighet med `alpha` parameteren (`0` er fullt
      gjennomsiktig, `1` fullt ugjennomsiktig)
- stil linjelagene:
    - juster [linjefargen](https://matplotlib.org/stable/api/colors_api.html) ved hjelp av
      `color` parameteren
    - endre `linewidth`, etter behov

Lagene har forskjellige omfang (`roads` dekker et mye større område). Du kan
bruke aksenes (`ax`) metoder `set_xlim()` og `set_ylim()` for å sette den horisontale
og vertikale utstrekningen av kartet (f.eks. til en geo-dataframes `total_bounds`).


```{code-cell}
ax = accessibility_grid.plot(
    figsize=(12, 8),

    column="pt_r_t",
    scheme="quantiles",
    cmap="Spectral",
    linewidth=0,
    alpha=0.8
)

metro.plot(
    ax=ax,
    color="orange",
    linewidth=2.5
)

roads.plot(
    ax=ax,
    color="grey",
    linewidth=0.8
)

minx, miny, maxx, maxy = accessibility_grid.total_bounds
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)
```


## Legge til en legend

For å plotte en legend for et kart, legg til parameteren `legend=True`.

For figurer uten et klassifisering `scheme`, består legenden av en farge
gradient bar. Legend er en instans av
[`matplotlib.pyplot.colorbar.Colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html),
og alle argumenter definert i `legend_kwds` blir sendt gjennom til den. Se nedenfor
hvordan du bruker `label` egenskapen for å sette *legend tittelen*:

```{code-cell}
ax = accessibility_grid.plot(
    figsize=(12, 8),

    column="pt_r_t",
    cmap="Spectral",
    linewidth=0,
    alpha=0.8,

    legend=True,
    legend_kwds={"label": "Reisetid (min)"}
)
```

:::{admonition} Sett andre `Colorbar` parametere
:class: hint

Sjekk ut [`matplotlib.pyplot.colorbar.Colorbar`’s
dokumentasjon](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html)
og eksperimenter med andre parametere! Alt du legger til i `legend_kwds`
ordboken vil bli sendt til fargebaren.
:::


---

For figurer som bruker et klassifisering `scheme`, på den annen side, `plot()`
lager en
[`matplotlib.legend.Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend).
Igjen, `legend_kwds` blir sendt gjennom, men parameterne er litt
forskjellige: for eksempel, bruk `title` i stedet for `label` for å sette legenden
tittel:

```{code-cell}
accessibility_grid.plot(
    figsize=(12, 8),

    column="pt_r_t",
    scheme="quantiles",
    cmap="Spectral",
    linewidth=0,
    alpha=0.8,

    legend=True,
    legend_kwds={"title": "Reisetid (min)"}
)
```

:::{admonition} Sett andre `Legend` parametere
:class: hint

Sjekk ut [`matplotlib.pyplot.legend.Legend`’s
dokumentasjon](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend),
og eksperimenter med andre parametere! Alt du legger til i `legend_kwds`
ordboken vil bli sendt til legenden.

Hvilket `legend_kwds` nøkkelord vil spre legenden over to kolonner?
:::


## Legge til et basekart

For bedre orientering er det ofte nyttig å legge til et basekart i et kartplott. En
basekart, for eksempel, fra kartleverandører som
[OpenStreetMap](https://osm.org/) eller [Stamen](https://maps.stamen.com/), legger til
gater, stedsnavn, og annen kontekstuell informasjon.

Python-pakken [contextily](https://contextily.readthedocs.io/) tar seg av
nedlasting av nødvendige kartfliser og gjengir dem i en geopandas plot.

:::{admonition} Web Mercator
:class: caution

Kartfliser fra online kartleverandører er typisk i [Web Mercator-projeksjon
(EPSG:3857](http://spatialreference.org/ref/sr-org/epsg3857-wgs84-web-mercator-auxiliary-sphere/).
Det er generelt tilrådelig å transformere alle andre lag til `EPSG:3857`, også.
:::

```{code-cell}
accessibility_grid = accessibility_grid.to_crs("EPSG:3857")
metro = metro.to_crs("EPSG:3857")
roads = roads.to_crs("EPSG:3857")
```

For å legge til et basekart i en eksisterende plot, bruk
[`contextily.add_basemap()`](https://contextily.readthedocs.io/en/latest/intro_guide.html)
funksjonen, og gi plot’s `ax` objektet som ble oppnådd i et tidligere trinn.

```{code-cell}
import contextily

ax = accessibility_grid.plot(
    figsize=(12, 8),

    column="pt_r_t",
    scheme="quantiles",
    cmap="Spectral",
    linewidth=0,
    alpha=0.8,

    legend=True,
    legend_kwds={"title": "Reisetid (min)"}
)
contextily.add_basemap(ax, source=contextily.providers.OpenStreetMap.Mapnik)
```

[Det er mange
andre nettbaserte kart å velge
fra](https://contextily.readthedocs.io/en/latest/intro_guide.html#Providers).
Alle de andre `contextily.providers` (se lenke ovenfor) kan sendes som en
`source` til `add_basemap()`. Du kan få en liste over tilgjengelige leverandører:

```{code-cell}
contextily.providers
```

På dette zoomnivået, lever fordelene ved å bruke OpenStreetMap (som stedsnavn)
ikke opp til sitt fulle potensial. La oss se på et delsett av reisetidsmatrisen:
rutenettceller som er innenfor 15 minutter fra jernbanestasjonen.

```{code-cell}
ax = accessibility_grid[accessibility_grid.pt_r_t <= 15].plot(
    figsize=(12, 8),

    column="pt_r_t",
    scheme="quantiles",
    k=5,
    cmap="Spectral",
    linewidth=0,
    alpha=0.8,

    legend=True,
    legend_kwds={"title": "Reisetid (min)"}
)
contextily.add_basemap(
    ax,
    source=contextily.providers.OpenStreetMap.Mapnik
)
```

Til slutt kan vi endre tilskrivningen (copyright-meldingen) som vises i
nederste venstre hjørne av kartplottet. Merk at du alltid skal respektere kart
leverandørenes bruksvilkår, som vanligvis inkluderer en datakilde-attribusjon
(*contextily*’s standarder tar hånd om dette). Vi kan og bør imidlertid
legge til en datakilde for alle lag vi la til, slik som reisetidsmatrisen
datasett:

```{code-cell}
ax = accessibility_grid[accessibility_grid.pt_r_t <= 15].plot(
    figsize=(12, 8),

    column="pt_r_t",
    scheme="quantiles",
    k=5,
    cmap="Spectral",
    linewidth=0,
    alpha=0.8,

    legend=True,
    legend_kwds={"title": "Reisetid (min)"}
)
contextily.add_basemap(
    ax,
    source=contextily.providers.OpenStreetMap.Mapnik,
    attribution=(
        "Reisetidsdata (c) Digital Geography Lab, "
        "kartdata (c) OpenStreetMap bidragsytere"
    )
)
```