# 📖 Geokoding

## Oversikt over Geokodere

Geokoding er prosessen med å transformere stedsnavn eller adresser til
koordinater. I denne leksjonen vil vi lære hvordan du geokoder adresser med
Geopandas og [geopy](https://geopy.readthedocs.io/en/stable/).

Geopy og andre geokoderbiblioteker (som
[geocoder](http://geocoder.readthedocs.io/)) gjør det enkelt å finne plasseringen av
koordinatene til adresser, byer, land og landemerker over hele kloden
ved hjelp av nettjenester ("geokodere"). I praksis er geokodere ofte applikasjons
programmeringsgrensesnitt (APIer) der du kan sende forespørsler, og motta
svar i form av stedsnavn, adresser og koordinater.

Geopy gir tilgang til flere geokodetjenester, inkludert:

- [ESRI ArcGIS](https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm)
- [Baidu Maps](http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding)
- [Bing](https://msdn.microsoft.com/en-us/library/ff701715.aspx)
- [GeocodeFarm](https://www.geocode.farm/geocoding/free-api-documentation/)
- [GeoNames](http://www.geonames.org/export/geonames-search.html)
- [Google Geocoding API (V3)](https://developers.google.com/maps/documentation/geocoding/)
- [HERE](https://developer.here.com/documentation/geocoder/)
- [IGN France](https://geoservices.ign.fr/documentation/geoservices/index.html)
- [Mapquest](https://developer.mapquest.com/documentation/open/)
- [OpenCage](https://opencagedata.com/api)
- [OpenMapQuest](http://developer.mapquest.com/web/products/open/geocoding-service)
- [Open Street Map Nominatim](https://wiki.openstreetmap.org/wiki/Nominatim)
- [What3words](https://developer.what3words.com/public-api/docsv2#overview)
- [Yandex](https://tech.yandex.com/maps/doc/geocoder/desc/concepts/input_params-docpage/)

Sjekk [geopy dokumentasjonen](https://geopy.readthedocs.io/en/stable/) for
flere detaljer om hvordan du bruker hver tjeneste via Python.

Som du ser, er det mange geokodere å velge mellom! Kvaliteten på
geokoderne kan variere avhengig av underliggende data. For eksempel, noen
adresser kan eksistere på OpenStreetMap, men ikke på Google Maps og derfor kan de
geokodes ved hjelp av Nominatim geokoderen, men ikke ved bruk av Google
Geocoding API - og omvendt.

Geokodetjenester kan kreve en **API-nøkkel** for å bruke dem. (dvs. du
må registrere deg for tjenesten før du kan få tilgang til resultater fra deres API).
Videre begrenser **ratebegrensning** også bruken av disse tjenestene. Geokoding
prosessen kan ende opp i en feil hvis du gjør for mange forespørsler
i en kort tidsperiode (f.eks. prøver å geokode et stort antall adresser). Se
tips for å håndtere ratebegrensning når du geokoder pandas DataFrames fra
[geopy dokumentasjonen](https://geopy.readthedocs.io/en/stable/#usage-with-pandas).
Hvis du betaler for geokodingstjenesten, kan du naturligvis gjøre flere forespørsler til
API.

I denne leksjonen vil vi bruke Nominatim geokoderen for å lokalisere en relativt
lite antall adresser. Bruk av Nominatim geokodingstjenesten er
ratebegrenset til 1 forespørsel per sekund (3600 / time). Du kan lese mer om
Nominatim brukerpolitikk i
[her](https://operations.osmfoundation.org/policies/nominatim/)

Heldigvis, Nominatim, som er en geokoder basert på OpenStreetMap data krever ikke
en API-nøkkel for å bruke tjenesten hvis den brukes til å geokode bare et lite
antall adresser.

:::{note}
Sjekk alltid vilkårene for tjenesten til geokodingstjenesten du bruker!
:::

:::{caution}
Som bemerket i [geopy-dokumentasjonen for Nominatim-geokoderen](https://geopy.readthedocs.io/en/stable/#nominatim)
vi må spesifisere en tilpasset `user_agent` parameter når vi lager forespørsler for ikke å bryte
[Nominatim brukerpolitikk](https://operations.osmfoundation.org/policies/nominatim/).
:::