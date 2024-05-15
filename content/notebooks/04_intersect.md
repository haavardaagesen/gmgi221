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

# Kryss

Liknende de romlige forholdene `within` og `contains` som ble dekket i [forrige seksjon](point-in-polygon-queries), stiller en annen vanlig geospatial forespørsel om to geometrier krysser eller berører.

Begge spørringene er implementert i `shapely`:
- [`intersects()`](https://shapely.readthedocs.io/en/stable/manual.html#object.intersects): to objekter krysser hvis grensen eller innsiden av et objekt krysser på noen måte med grensen eller innsiden av det andre objektet.
- [`touches()`](https://shapely.readthedocs.io/en/stable/manual.html#object.touches): to objekter berører hvis objektene har minst ett punkt felles, men innsidene deres krysser ikke med noen del av det andre objektet.

La oss prøve disse funksjonene ut, for eksempel ved å bruke to linjer:

```{code-cell} python
import shapely.geometry

line1 = shapely.geometry.LineString([(0, 0), (1, 1)])
line2 = shapely.geometry.LineString([(1, 1), (0, 2)])
```

```{code-cell} python
line1.intersects(line2)
```

Linjene krysser. Berører de også?

```{code-cell} python
line1.touches(line2)
```

`line1` berører `line2`. Ved å legge dem begge til en multi-linje er en rask måte å
tegne dem inne i en Jupyter-notatbok:

```{code-cell} python
shapely.geometry.MultiLineString([line1, line2])
```

Vi kan se her, at de deler punktet `(1, 1)`, der `line1` slutter, og
`line2` begynner. De to linjene krysser ikke ellers (‘i deres indre’),
så spådommet ’`touch()`’ - som definert ovenfor - er sant.

Hvis linjene skulle dele noe av innsiden deres, ville det ikke bli regnet som
berøring. For eksempel, `line1` berører ikke `line1` (seg selv), men oppfyller
alle krav for å bli regnet som `intersect()`ing med seg selv:

```{code-cell} python
line1.touches(line1)
```

```{code-cell} python
line1.intersects(line1)
```