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

# Aggregering av data

Dataaggregering refererer til en prosess der vi kombinerer data i grupper. Når
vi gjør romlig dataaggregering, slår vi geometriene sammen til grovere
enheter (basert på noen attributter), og kan også beregne sammendragsstatistikk for
disse kombinerte geometriene fra de opprinnelige, mer detaljerte verdiene. For eksempel,
antar at vi er interessert i å studere kontinenter, men vi har bare
landnivådata som datsettet for land. Hvis vi aggregerer dataene etter
kontinent, vil vi konvertere dataene på landsnivå til et datasett på
kontinentnivå.

I denne opplæringen vil vi aggregere reisetidsdataene våre etter reisetider med bil
(kolonne `car_r_t`), dvs. rutenettcellene som har samme reisetid til
Jernbanestasjonen vil bli slått sammen.

La oss starte med å laste `intersection.gpkg`, utdatafilen fra
[forrige seksjon](overlay-analysis):

```{code-cell} python
import pathlib 
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```

```{code-cell} python
import geopandas
intersection = geopandas.read_file(DATA_DIRECTORY / "intersection.gpkg")
```

For å gjøre aggregeringen vil vi bruke en metode som heter `dissolve()` som tar
som inngang kolonnen som vil bli brukt til å utføre aggregeringen:

```{code-cell} python
# Utføre aggregeringen
dissolved = intersection.dissolve(by="car_r_t")

# Hva fikk vi
dissolved.head()
```

La oss sammenligne antall celler i lagene før og etter aggregeringen:

```{code-cell} python
print(f"Rader i opprinnelig intersection GeoDataFrame: {len(intersection)}")
print(f"Rader i oppløst lag: {len(dissolved)}")
```

Faktisk har antall rader i dataene våre redusert og polygonene ble
slått sammen.

Hva skjedde egentlig her? La oss ta en nærmere titt. 

La oss se hvilke kolonner vi nå har i vår GeoDataFrame:

```{code-cell} python
dissolved.columns
```

Som vi kan se, kan ikke kolonnen som vi brukte for å utføre aggregeringen
(`car_r_t`) finnes lenger i kolonnelisten. Hva skjedde med
den?

La oss ta en titt på indeksene i vår GeoDataFrame:

```{code-cell} python
dissolved.index
```

Aha! Vel nå forstår vi hvor kolonnen vår gikk. Den brukes nå som indeks i
vår `dissolved` GeoDataFrame. 

Nå kan vi for eksempel bare velge slike geometrier fra laget som er for
eksempel nøyaktig 15 minutter unna Helsingfors jernbanestasjon:

```{code-cell} python
# Velg bare geometrier som er innen 15 minutter unna
dissolved.loc[15]
```

```{code-cell} python
# Se datatype
type(dissolved.loc[15])
```


Som vi kan se, har vi nå som et resultat et Pandas `Series` objekt som inneholder
i utgangspunktet en rad fra vår opprinnelige aggregerte GeoDataFrame.

La oss også visualisere disse 15 minutters rutenettcellene.

Først må vi konvertere den valgte raden tilbake til en GeoDataFrame:

```{code-cell} python
# Lag en GeoDataFrame
selection = geopandas.GeoDataFrame([dissolved.loc[15]], crs=dissolved.crs)
```

Plott utvalget på toppen av hele rutenettet:

```{code-cell} python
# Plott alle rutenettcellene, og rutenettcellene som er 15 minutter
# unna jernbanestasjonen
ax = dissolved.plot(facecolor="gray")
selection.plot(ax=ax, facecolor="red")
```

En annen måte å visualisere reisetidene i hele GeoDataFrame på er å plott ved hjelp av en spesifikk kolonne. For å bruke vår `car_r_t` kolonne, som nå er indeksen i GeoDataFrame, må vi tilbakestille indeksen:

```{code-cell} python
dissolved = dissolved.reset_index()
dissolved.head()
```

Som vi kan se, har vi nå vår `car_r_t` som en kolonne igjen, og kan da plott GeoDataFrame ved å sende denne kolonnen ved hjelp av `column` parameteren:

```{code-cell} python
dissolved.plot(column="car_r_t")
```