# 📖 Prosjektarbeid

I prosjektoppgaven er målet å bruke Python-programmering til å automatisere en GIS-analyseprosess. Hovedmålet er å lage en arbeidsflyt for GIS-prosesser som enkelt kan gjentas for lignende input-data.

Du kan velge et forhåndsdefinert tema, eller utvikle ditt eget forskningsspørsmål. Du bør dra nytte av dine programmeringsferdigheter (grunnleggende bruk av Python, definere dine egne funksjoner, lese og skrive data, dataanalyse ved hjelp av Pandas, romlig analyse ved hjelp av Geopandas, lage statiske og/eller interaktive datavisualiseringer, med mer), og gode kodingspraksiser (skrive lesbar og godt dokumentert kode) når du gjør den endelige prosjektoppgaven.

## Tema

Du kan velge mellom disse to prosjektoppgavene:

* [Urbane indikatorer](#urbane-indikatorer)
* [Egendefinert prosjekt](#egendefinert-prosjekt)

Tenk på prosjektoppgaven som en utfordring for deg selv og en mulighet til å vise og implementere ferdighetene du har lært i emnet så langt.

## Struktur

Her er den foreslåtte strukturen på prosjektoppgaven, som også er utgangspunktet for vurderingen:

* Datainnsamling (Henting av data, delsett av data, lagring av mellomliggende resultater osv.)

* Dataanalyse (Beriking og analyse av data, f.eks. romlig kobling, overlapp, buffring, andre beregninger)

* Visualisering (Visualisering av hovedresultater og annen relevant informasjon som kart og grafer)


Du kan skrive koden din i Python-skriptfiler og/eller jupyter-notebooks. Du kan fritt organisere prosjektoppgaven i en enkelt fil, eller flere filer (for eksempel, skrive dine egne funksjoner i en separat .py-fil og bruke dem i en eller flere jupyter-notebook .ipynb-filer.

Arbeidsflyten skal være gjentakbar og godt dokumentert. Med andre ord, alle som får en kopi av koden din skal kunne kjøre koden din, og lese koden din.

## Hva skal leveres?

Organiser all koden din / notebooks i en mappe og legg til lenker til alle relevante filer i README.md-filen. Man skal kunne lese koden din og dokumentasjonen og forstå hva som skjer, og kjøre koden din for å reprodusere de samme resultatene. Du leverer inn **èn zip-mappe** med alle relevante filer på Canvas. 

Merk: Hvis koden din krever noen python-pakker som ikke er brukt ellers i emnet, vennligst nevn dem også i README.md-filen og gi installasjonsinstruksjoner.

Frist for å levere er **03.12.2024**.

## Vurdering

Vurderingen av prosjektoppgaven er basert på en typisk 0-5 skala. Se detaljerte [vurderingskriterier her](#13_prosjektkarakter). Den endelige oppgaven vurderes basert på:

* Hovedanalysesteg (datainnhenting, dataanalyse, visualisering)

* Gjentakbarhet (det skal være mulig å gjenta hovedanalysetrinnene for forskjellige inngangsfiler / inngangsparametere)

* Kvalitet på visualiseringer (kart og grafer)

* Generell dokumentasjon av arbeidet (bruk markdown celler for å strukturere arbeidet, og kodekommentarer for å forklare detaljer)

God dokumentasjon av koden og prosjektet ditt er høyt verdsatt! Du bør legge til nødvendige detaljer i README.md-filen, og bruke inline kommentarer og Markdown celler for å dokumentere arbeidet ditt underveis. Ta en titt på disse tipsene for å bruke markdown:

* [General Markdown syntax guide](https://guides.github.com/features/mastering-markdown/)

* [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Prosjekter

### Urbane indikatorer

I denne oppgaven er målet å utvikle et verktøy for urban analyse og anvende det på minst bydeler i Oslo. Hovedideen er å beregne et sett med målinger / indikatorer basert på den urbane formen og/eller befolkningen, og å sammenligne bydelene basert på disse målingene. Denne oppgaven er ikke nøyaktig definert, da ideen er å la deg bruke din egen fantasi og interesse til å utforske forskjellige datasett og utføre analyser som interesserer deg, samtidig som du gir nyttige innsikter om de urbane områdene ved å bruke et spesifikt sett med indikatorer (du bør bruke 2-4 forskjellige indikatorer, se eksempler nedenfor).

### Data
Du kan bruke hvilken som helst (romlig) data som du kan finne, og generere din egen rapport som beskriver hvordan bydelene skiller seg fra hverandre basert på forskjellige perspektiver (se nedenfor for hint om mulige analyser). Du kan bruke hvilken som helst data som er tilgjengelig, for eksempel fra følgende kilder:

* OpenStreetMap (f.eks. gater, bygninger, interessepunkter) etter tilnærmingen fra leksjon 6.
* [Geonorge](https://www.geonorge.no/kartdata/datasett-i-geonorge/)
* [SSB sin statistikkbank](https://www.ssb.no/statbank)
* [Oslo kommunes statistikkbank](https://statistikkbanken.oslo.kommune.no/)
* Data fra [Oslo Bysykkel](https://oslobysykkel.no/apne-data)
* Datakilder er ikke begrenset til disse, så du kan også bruke andre data fra hvilken som helst kilde du kan finne (husk å dokumentere hvor dataene kommer fra!).

#### Eksempel analyser

Verktøyet bør beregne 2-4 indikatorer om de urbane områdene. Her er noen eksempler på potensielle målinger:

**Befolkningsfordeling og demografi**

 - Håndtering av inndata (tabellkoblinger, datarensing osv.)
 - Beregn nøkkelstatistikker
 - Lag kart og grafer

**Urban befolkningsvekst**

 - Hent befolkningsdata fra minst to forskjellige år
 - Sammenlign statistikk fra forskjellige år
 - Visualiser som grafer og kart
<!-- 
**Tilgjengelighet**:

 - Bestem hvilke reisetider du fokuserer på (gåing, kjøring, offentlig transport..)
 - Bestem hvilke typer destinasjoner du fokuserer på (transportstasjoner, helsetjenester, utdanning, idrettsanlegg..)
 - Få reisetidsdata fra Travel Time Matrix ELLER beregn korteste veier i et nettverk
 - Beregn reisetids- / reiseavstandsmål, eller dominansområder
 - Visualiser resultatene som grafer og kart
-->

**Grønt areal-indeks**

 - Hent grønne arealpolygoner og filtrer dataene om nødvendig
 - Beregn prosentandelen av grønne områder i bydelene + andre statistikker
 - Visualiser resultatene

**Gate nettverksmålinger**

 - Hent gatenettverksdata
 - Beregn gatenettverksmålinger (se forelesning 12 og eksempler fra [her](https://github.com/gboeing/osmnx-examples/tree/master/notebooks))
 - Visualiser resultatene

**Bygningsdensitet**

 - Hent dataene, og filtrer om nødvendig
 - Beregn bygningsdensitet og andre målinger
 - Lag kart som viser bygningstyper og densitet

#### Struktur i oppgaven for urbane indikatorer

Du kan designe strukturen på oppgaven din fritt. Vi foreslår at du lager funksjoner i separate skriptfiler og demonstrerer bruken av disse funksjonene i en eller flere notatbøker. I tillegg bør du gi grunnleggende informasjon i README.md-filen til din endelige oppgave. Alt i alt bør arbeidet inkludere disse komponentene:

* Et emne for arbeidet ditt (f.eks. "Urbane indikatorer: analysere gatenettverksstrukturen i Stovner og Frogner").
* En kort introduksjon til emnet (presenter 2-4 forskningsspørsmål som du har som mål å besvare ved hjelp av indikatorene)
* Kort beskrivelse av datasettene du brukte
* Kort generell beskrivelse av metodene du brukte
* Faktiske koder og visualiseringer for å produsere resultatene
* Kort diskusjon relatert til resultatene (hva bør vi forstå og se fra dem?)
* Kort refleksjon om analysen, for eksempel: - Hvilke antakelser, skjevheter eller usikkerheter er relatert til dataene og/eller analysene du gjorde? - Andre merknader som leseren bør vite om analysen

#### Tekniske hensyn

Pass på at du:

* Dokumenterer analysene dine godt ved å bruke Markdown-celler og beskriver 1) hva du gjør og 2) hva du kan se fra dataene og resultatene dine.
* Bruker informative visualiseringer
    * Lag kart (statisk eller interaktivt)
    * Lag andre typer grafer (f.eks. stolpediagrammer, linjediagrammer, spredningsplott osv.)
    * Bruk underplott som gjør det enkelt å sammenligne resultater side om side
* Når du skriver kodene, anbefaler vi sterkt at du bruker og skriver funksjoner for repeterende deler av koden. Som en motivasjon: tenk at du skal gjenta analysene dine for alle byer i Finland, skriv kodene dine på en måte som gjør dette mulig. Videre anbefaler vi at du lagrer disse funksjonene i en egen .py-skriptfil som du importerer til notatboken

### Egendefinert prosjekt

Utvikle ditt eget emne! Generelt bør ditt eget emne også inneholde disse seksjonene:

* Datainnhenting (Hente data, filtrere data, lagre midlertidig utdata osv.)

* Dataanalyse (Berike og analysere dataene, f.eks. romlig koblinger, overlay, buffering, andre beregninger..)

* Visualisering (Visualisere hovedresultater og annen relevant informasjon som kart og grafer)

Men føl deg fri til å være kreativ! Ditt eget prosjekt kan for eksempel være relatert til et prosjekt i andre fag eller masteroppgave. Husk å beskrive tydelig hva du gjør i den endelige oppgavens README.md-fil. Hvis du velger et egendefinert prosjekt, må du få godkjenning på prosjektet før du setter ordentlig i gang.

Det som minst kreves av det endelige prosjektet, er at du har:

* Fungerende kode for oppgaven / problemet / analysene som løser oppgaven

* God dokumentasjon (dvs. en veiledning) som forklarer hvordan verktøyet ditt fungerer ELLER en rapport om analysene dine og hva vi kan lære av dem