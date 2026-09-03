# 📖 Læringsmål

På denne siden finner du læringsmålene for emnet fordelt på hver uke.

Emnet gir en innføring i programmering for geografiske analyser og programmatisk behandling av geografiske data. Gjennom emnet vil du få en innføring i ulike analysemetoder innenfor geografisk informasjonsvitenskap (GIS), og praktisk erfaring i databehandling og analyse med geografiske data.

Studenten skal etter gjennomført kurs være i stand til å utføre grunnleggende analyser av og med geografiske data i Python, skrive kode som analyserer og visualiserer geografiske data, samt kunne lese og forstå programmer på tilsvarende kompleksitetsnivå.

## Uke 1 - Introduksjon, oppsett og en smakebit av Python

_Introduksjon til emnet, Python-miljø og de mest grunnleggende Python-byggeklossene._

Første uke består av informasjon av emnet og introduksjon til hvordan sette opp et fungerende miljø for kurset. Vi starter også med en liten praktisk innføring i Python.

**Etter denne uka skal du kunne:**

* sette opp et fungerende conda-miljø for kurset og kjøre en Jupyter Notebook
* definere og bruke variabler, og velge beskrivende variabelnavn
* identifisere og bruke sentrale datatyper: heltall, flyttall, streng, boolsk, liste og ordbok
* forklare hvordan disse datatypene representerer romlig informasjon som koordinater og attributter
* utføre enkle operasjoner på datatypene: aritmetikk, indeksering, `.append()`, oppslag i ordbok
* bruke `if/elif/else`, `for`-løkker og enkle funksjoner (`def/return`), og importere moduler med import

## Uke 2 - Geometriske objekter i Shapely

_Hvordan enkeltgeometrier representeres i Python og defensiv programmering._

**Etter denne uka skal du kunne:**

* finne og vurdere relevante Python-pakker for GIS og romlig analyse
* forklare hvordan punkt, linje og polygon representeres og lagres i shapely, inkludert well-known text (WKT)
* opprette shapely-geometrier fra koordinatverdier og hente ut egenskaper som `geom_type`, koordinater, lengde og areal
* beregne avstand mellom geometrier og teste romlige relasjoner som `intersects()` og `touches()`
* bruke assert med informative feilmeldinger for å fange ugyldige inndata i egne funksjoner, og forklare forskjellen på `AssertionError` og `TypeError`

## Uke 3 – GeoPandas og vektordata

_Fra enkeltgeometrier til hele datasett: lese, utforske og skrive vektordata._

**Etter denne uka skal du kunne:**

* bygge robuste filstier med pathlib og skille rådata fra resultater med konstanter
* lese vektordata i ulike formater og fra ulike kilder (lokal fil, zip, URL, WFS) med `geopandas.read_file()`
* liste tilgjengelige filformat/drivere og skrive en GeoDataFrame til fil med `to_file()`
* forklare oppbygningen av en GeoDataFrame: rader, attributtkolonner og geometry-kolonnen
* gruppere data med `groupby()` og iterere over gruppene, f.eks. for å skrive én fil per gruppe

## Uke 4 – Projeksjoner, geometriske operasjoner og geokoding

_Koordinatsystem, avledede geometrier og å gå fra stedsnavn til koordinater._

__Etter denne uka skal du kunne:__

* inspisere en GeoDataFrame sitt koordinatsystem med `.crs` og reprojisere med `to_crs()`
* skille mellom geografiske og projiserte koordinatsystem og forklare hvorfor areal- og avstandsberegninger krever et projisert CRS
* angi et CRS på flere måter (EPSG-kode, WKT, PROJ-streng)
* utføre geometriske operasjoner: `centroid`, `buffer()`, `dissolve()` (med `aggfunc`), `simplify()`, `convex_hull`, `envelope`, `union_all()`
* hente koordinater for stedsnavn/adresser med geokoding (Nominatim) og koble resultatet til en tabell med `join()`/`merge()`

## Uke 5 – Romlige utvelgelser og koblinger

_Å velge og kombinere data ut fra hvordan objekter ligger i forhold til hverandre._

__Etter denne uka skal du kunne:__

* forklare romlige predikat (`within`, `contains`, `intersects`)
* velge ut objekter basert på romlig relasjon, f.eks. punkt-i-polygon
* utføre en romlig kobling med `geopandas.sjoin()` og begrunne valg av `how` og `predicate`
* kontrollere at lag har samme CRS før en kobling, f.eks. med en `assert`
* lage et enkelt koroplettkart av resultatet med klasseinndeling (`scheme`, `cmap`)

## Uke 6 – Reklassifisering og aggregering

_Å gjøre kontinuerlige verdier om til klasser, og å slå sammen data._

__Etter denne uka skal du kunne:__

* klassifisere kontinuerlige verdier med `mapclassify`-metoder som Natural Breaks og kvantiler, og hente ut klassegrensene (`.bins`)
* begrunne valg av klassifiseringsmetode og antall klasser, og vise grensene i et histogram
* lage egne klassifiseringsregler med en funksjon eller `lambda` og `apply()`
* aggregere data romlig med `dissolve()` og en passende `aggfunc` (`sum`, `gjennomsnitt`), og velge en meningsfull grupperingsvariabel

## Uke 7 – Overlay-analyse (og oppstart av prosjekt)

_Å kombinere to polygonlag, og introduksjon til prosjektoppgaven._

__Etter denne uka skal du kunne:__

* forklare forskjellen på overlay-operasjonene `intersection`, `union`, `difference` og `symmetric difference`
* kombinere to polygonlag med `geopandas.overlay()` og tolke resultatet
* visualisere hva en overlay-operasjon gjør, f.eks. med en hjelpefunksjon

## Uke 8 – Statiske og interaktive kart

_Kartografi i praksis, både for trykk og for web._

__Etter denne uka skal du kunne:__

* lage et statisk kart med flere lag i `matplotlib`/`GeoPandas` og styre farge, klasseinndeling, gjennomsiktighet og utsnitt (`scheme`, `cmap`, `alpha`, `set_xlim`/`set_ylim`)
* legge til tittel, tegnforklaring og bakgrunnskart (`contextily`), og forklare hvorfor bakgrunnskart krever Web Mercator
* lage et interaktivt Leaflet-kart med `folium`: markører, GeoJSON-lag, popup/tooltip og koroplett
* lagre et interaktivt kart som en HTML-fil
* vurdere kartografiske valg kritisk – klasseinndeling, fargevalg, lesbarhet

## Uke 9 – OpenStreetMap-data og nettverksanalyse

_Å hente data fra OSM og regne på gatenettet._

__Etter denne uka skal du kunne:__

* hente geodata fra OpenStreetMap med `osmnx`: gatenett, bygninger, POI-er, grøntområder (`graph_from_place`, `features_from_place`)
* konvertere et gatenett mellom graf og GeoDataFrame (`graph_to_gdfs`) og projisere grafen
* finne nærmeste node til et punkt og beregne korteste vei mellom to punkt (`nearest_nodes`, `shortest_path`)
* visualisere en rute på nettverket og hente ut enkel nettverksstatistikk (`basic_stats`)
* lagre en beregnet rute til fil

## Uke 10 – Rasteranalyse (og prosjektveiledning)

%Den andre hoveddatatypen i GIS: rasterdata.
%
%Etter denne uka skal du kunne:
%
%* forklare hvordan et raster representeres som et 2D-array med et koordinatsystem og en romlig oppløsning (10_raster)
%* indeksere og dele opp arrays med numpy-slicing (10_raster)
%* lese og skrive rasterdata med xarray/rioxarray og inspisere rio.crs (10_raster)
%* hente ut og regne på enkeltbånd, f.eks. beregne NDVI med båndaritmetikk (10_raster)
%* visualisere et raster med imshow og et passende fargekart (10_raster)
%
## Prosjektarbeid

_Å sette sammen alt til én sammenhengende, reproduserbar arbeidsflyt._

__Etter prosjektet skal du kunne:__

* planlegge og gjennomføre en sammenhengende, automatisert GIS-arbeidsflyt fra rådata til ferdig analyse og kart
* skille gjenbrukbar kode ut i funksjoner i .py-moduler som importeres i notebooks
* dokumentere prosjektet slik at en annen person kan kjøre det på nytt (README, mappestruktur, miljøfil)
* gjøre rede for eventuell bruk av KI-verktøy i arbeidet (00_bruk_av_ai)

