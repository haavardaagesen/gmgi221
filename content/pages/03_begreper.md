# Nøkkelbegreper

:::{admonition} **Sjekk din forståelse**
Før du dykker inn i denne ukens Python-leksjon, bør du allerede være kjent med noen grunnleggende
romlige datafilformater og projeksjonsdefinisjoner, som disse:

- Shapefile
- GeoPackage
- CRS
- Datum
- EPSG
:::

:::{admonition} **Definisjoner**
**Shapefile:** et vektor dataformat for lagring av stedsinformasjon og relaterte attributter.
En shapefile består av flere filer med et felles prefiks som må lagres i samme katalog.
`.shp`, `shx` og `.dbf` er påkrevde filutvidelser i en shapefile. Andre filutvidelser er ikke påkrevd,
men for eksempel filutvidelsen `.prj` er ofte avgjørende. Mer informasjon om Shapefile filutvidelser
finnes [her](<http://help.arcgis.com/en/arcgisdesktop/10.0/help/index.html#/Shapefile_file_extensions/005600000003000000/>).
Shapefile-formatet er utviklet av ESRI.

**GeoPackage:** et åpent kildekodeformat for lagring og overføring av geografisk informasjon.
GeoPackages kan lagre både vektor data og raster data. I mer detalj, er GeoPackage en beholder for
en SQLite database med en `.gpkg`-utvidelse (alt i en fil!). GeoPackage-formatet styres av Open GeoSpatial Consortium.
Mer informasjon på: <https://www.geopackage.org/>

**CRS:** Koordinatreferansesystemer definerer hvordan koordinater relaterer seg til virkelige steder på jorden.
*Geografiske koordinatreferansesystemer* bruker vanligvis bredde- og lengdegrader.
*Projiserte koordinatreferansesystemer* bruker x- og y-koordinater for å representere steder på en flat overflate.
Du vil lære mer om koordinatreferansesystemer i løpet av denne leksjonen!

**Datum:** definerer midtpunktet, orienteringen og skalaen til referanseoverflaten relatert til et koordinatreferansesystem.
Samme koordinater kan forholde seg til forskjellige steder avhengig av datumet! For eksempel er WGS84 et mye brukt globalt datum.
ETRS89 er et datum som brukes i Europa. Koordinatreferansesystemer er ofte navngitt basert på det brukte datumet.

**EPSG:** EPSG-koder refererer til spesifikke referansesystemer.
EPSG står for "European Petroleum Survey Group" som opprinnelig publiserte en database for romlige referansesystemer.
For eksempel, [EPSG:3067](https://spatialreference.org/ref/epsg/3067/) refererer til koordinatreferansesystemet ETRS-TM35FIN som er mye brukt i Finland.
[EPSG:4326](https://spatialreference.org/ref/epsg/4326/) refererer til WGS84. Du kan søke etter EPSG-koder på: <https://spatialreference.org/>
:::