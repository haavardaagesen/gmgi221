# 📖 Prosjektarbeid

<iframe style="overflow: hidden;" src="https://haavardaagesen.github.io/presentations/gmgi221/h_2026/13/13_notes.html" width="720" height="405"></iframe>

I prosjektoppgaven er målet å bruke Python-programmering til å automatisere en GIS-analyseprosess. Hovedmålet er å lage en arbeidsflyt for GIS-prosesser som enkelt kan gjentas for lignende input-data.

Du kan velge et forhåndsdefinert tema, eller utvikle ditt eget forskningsspørsmål. Du bør dra nytte av dine programmeringsferdigheter (grunnleggende bruk av Python, definere dine egne funksjoner, lese og skrive data, dataanalyse ved hjelp av Pandas, romlig analyse ved hjelp av Geopandas, lage statiske og/eller interaktive datavisualiseringer, med mer), og gode kodingspraksiser (skrive lesbar og godt dokumentert kode) når du gjør den endelige prosjektoppgaven.

## Tema

Du kan velge mellom disse to prosjektoppgavene:

* [Urbane indikatorer](#urbane-indikatorer)
* [Kommuneplanens arealdel](#kommuneplanens-arealdel)
* [Egendefinert prosjekt](#egendefinert-prosjekt)

Tenk på prosjektoppgaven som en utfordring for deg selv og en mulighet til å vise og implementere ferdighetene du har lært i emnet så langt.

## Struktur

Her er den foreslåtte strukturen på prosjektoppgaven, som også er utgangspunktet for vurderingen:

* Datainnsamling (Henting av data, delsett av data, lagring av mellomliggende resultater osv.)

* Dataanalyse (Beriking og analyse av data, f.eks. romlig kobling, overlapp, buffring, andre beregninger)

* Visualisering (Visualisering av hovedresultater og annen relevant informasjon som kart og grafer)


Du kan skrive koden din i Python-skriptfiler og/eller jupyter-notebooks. Du kan fritt organisere prosjektoppgaven i en enkelt fil, eller flere filer (for eksempel, skrive dine egne funksjoner i en separat .py-fil og bruke dem i en eller flere jupyter-notebook .ipynb-filer.

Arbeidsflyten skal være gjentakbar og godt dokumentert. Med andre ord, alle som får en kopi av koden din skal kunne kjøre koden din, og lese koden din.

## Bruk av KI

I emnet er bruk av KI tillat, men utelukker samtidig bruk av agentisk KI. Dersom du bruker KI skal det dokumenteres grundig i en form hvor du beskriver hvordan du har brukt KI, til hva og hvorfor du har tatt det i bruk. Bruk av KI skal til enhver tid være i tråd med universitetets retningslinjer. 

### Erklæring om bruk av KI

Alle innleveringer skal inneholde en erklæring om bruk av KI, også dersom du ikke har brukt KI. Erklæringen skrives enten som en egen seksjon nederst i README.md, med overskriften '## Bruk av KI', eller i en egen fil som har navnet 'KI-erklaering.md', som det lenkes til fra README.md. For hvert verktøy du har brukt, skal du oppgi navnet på verktøyet (f.eks. ChatGPT, Copilot eller Claude), hva du brukte det til, og hvilke deler av prosjektet det gjelder (f.eks. hvilke funksjoner, notatbøker eller deler av teksten). Du skal også kort forklare hvorfor du valgte å bruke KI, og hvordan du kontrollerte og eventuelt endret det du fikk. Ta gjerne med eksempler på spørsmål (prompts) du brukte. Du er selv ansvarlig for all kode og tekst du leverer, og du må kunne forklare den. Hvis du ikke har brukt KI, skriver du det. Husk at agentisk KI, altså verktøy som selv skriver, kjører og endrer koden din uten at du styrer hvert steg, ikke er tillatt i emnet.

## Hva skal leveres?

Organiser all koden din / notebooks i en mappe og legg til lenker til alle relevante filer i README.md-filen. Man skal kunne lese koden din og dokumentasjonen og forstå hva som skjer, og kjøre koden din for å reprodusere de samme resultatene. Du leverer inn **èn zip-mappe** med alle relevante filer på Canvas. 

Merk: Hvis koden din krever noen python-pakker som ikke er brukt ellers i emnet, vennligst nevn dem også i README.md-filen og gi installasjonsinstruksjoner.

Frist for å levere er **15.12.2026**.

## Vurdering

Se detaljerte [vurderingskriterier her](#13_prosjektkarakter). Den endelige oppgaven vurderes basert på:

* Datainnhenting og databehandling

* Romlig analyse og indikatorer  

* Visualisering   

* Kodekvalitet og gjentakbarhet  

* Dokumentasjon og rapport

God dokumentasjon av koden og prosjektet ditt er høyt verdsatt! Du bør legge til nødvendige detaljer i README.md-filen, og bruke inline kommentarer og Markdown celler for å dokumentere arbeidet ditt underveis. Ta en titt på disse tipsene for å bruke markdown:

* [General Markdown syntax guide](https://guides.github.com/features/mastering-markdown/)

* [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Prosjekter

### Urbane indikatorer

I denne oppgaven er målet å utvikle et verktøy for urban analyse og anvende det på minst to bydeler i Oslo. Hovedideen er å beregne et sett med målinger / indikatorer basert på den urbane formen og/eller befolkningen, og å sammenligne bydelene basert på disse målingene. Denne oppgaven er ikke nøyaktig definert, da ideen er å la deg bruke din egen fantasi og interesse til å utforske forskjellige datasett og utføre analyser som interesserer deg, samtidig som du gir nyttige innsikter om de urbane områdene ved å bruke et spesifikt sett med indikatorer (du bør bruke 2-4 forskjellige indikatorer, se eksempler nedenfor).

### Data
Du kan bruke hvilken som helst (romlig) data som du kan finne, og generere din egen rapport som beskriver hvordan bydelene skiller seg fra hverandre basert på forskjellige perspektiver (se nedenfor for hint om mulige analyser). Du kan bruke hvilken som helst data som er tilgjengelig, for eksempel fra følgende kilder:

* OpenStreetMap (f.eks. gater, bygninger, interessepunkter) etter tilnærmingen fra uke 9.
* [Geonorge](https://www.geonorge.no/kartdata/datasett-i-geonorge/)
* [SSB sin statistikkbank](https://www.ssb.no/statbank)
* [Oslo kommunes statistikkbank](https://statistikkbanken.oslo.kommune.no/)
* Data fra [Oslo Bysykkel](https://oslobysykkel.no/apne-data)
* Datakilder er ikke begrenset til disse, så du kan også bruke andre data fra hvilken som helst kilde du kan finne (husk å dokumentere hvor dataene kommer fra!).

#### Eksempelanalyser

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
 - Beregn gatenettverksmålinger (se forelesning om nettverksanalyse og eksempler fra [her](https://github.com/gboeing/osmnx-examples/tree/master/notebooks))
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
* Når du skriver kodene, anbefaler vi sterkt at du bruker og skriver funksjoner for repeterende deler av koden. Som en motivasjon: tenk at du skal gjenta analysene dine for alle byer i Norge, skriv kodene dine på en måte som gjør dette mulig. Videre anbefaler vi at du lagrer disse funksjonene i en egen .py-skriptfil som du importerer til notatboken

### Kommuneplanens arealdel

I denne oppgaven er målet å utvikle et verktøy som analyserer en kommuneplans arealdel, og å bruke det på kommuneplanen for Aurskog-Høland. Kommuneplanens arealdel er det juridisk bindende kartet som viser hva arealene i kommunen kan brukes til (arealformål), og hvilke hensyn som må tas (hensynssoner for blant annet flom, skred, støy, kulturmiljø og drikkevann). Du skal sammenligne minst to steder i kommunen (f.eks. tettstedene Bjørkelangen, Aursmoen, Løken, Hemnes eller Rømskog) ut fra et sett med indikatorer. Du velger selv hvordan du avgrenser stedene, for eksempel med SSB sine tettstedsavgrensninger eller en buffer rundt sentrum.

Det overordnede spørsmålet er: **Hvor planlegger kommunen ny utbygging, og hvilke konflikter og hensyn berører denne utbyggingen?** Du skal beregne 2-4 indikatorer, og velge dem selv ut fra hva du synes er interessant (se eksempler nedenfor).

### Data

Du finner kommuneplanen for Aurskog-Høland som shapefiler i én zip-fil på canvas. De viktigste lagene er:

| Lag                   | Innhold                                     | Viktige kolonner                                                                          |
| --------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `KpArealformålOmråde` | Arealformål (1725 polygoner)                | `KPAREALFOR` (formålskode), `AREALST` (1 = nåværende, 2 = framtidig), `PLANID`, `OMRNAVN` |
| `KpOmråde`            | Plangrensen (yttergrensen for planen)       | `PLANID`, `PLANNAVN`                                                                      |
| `KpFareSone`          | Faresoner                                   | `KPFARE` (310 = skred, 320 = flom, 370 = høyspent)                                        |
| `KpStøySone`          | Støysoner                                   | `KPSTØY` (210 = rød sone, 220 = gul sone)                                                 |
| `KpAngittHensynSone`  | Hensyn til kulturmiljø og friluftsliv       | `KPANGITTHE` (570 = kulturmiljø, 530 = friluftsliv), `BESKRIVELS`                         |
| `KpBåndleggingSone`   | Båndlagte områder (naturvern, kulturminner) | `KPBÅNDLEGG` (710/720/730), `BESKRIVELS`                                                  |
| `KpSikringSone`       | Nedslagsfelt for drikkevann                 | `KPSIKRING` (110)                                                                         |
| `KpSamferdselLinje`   | Veger i planen                              | `TYPESAMFLI`, `HOLDNINGSK`                                                                |

Formålskodene følger SOSI-standarden for plan. De viktigste kodene er: 1110 boligbebyggelse, 1120 fritidsbebyggelse, 1130 sentrumsformål, 1160 offentlig eller privat tjenesteyting, 1300 næringsvirksomhet, 1400 idrettsanlegg, 2010 veg, 3001/3020/3040 grønnstruktur, 5100 LNFR (landbruks-, natur- og friluftsformål), 5200/5210 LNFR spredt bebyggelse og 6600/6700 natur- og friluftsområde i vassdrag. Den fullstendige kodelisten finner du i [SOSI-produktspesifikasjonen for plan](https://sosi.geonorge.no/produktspesifikasjoner/). En del av oppgaven er å lage en oppslagstabell som oversetter kodene til lesbare navn.

**Merk:** Dataene kommer rett fra kommunens plansystem og er ikke ferdig vasket. Du må regne med at noe datarensing er nødvendig før analysen (f.eks. tegnkoding, verdier med skjulte tegn, objekter som overlapper hverandre, og tomme lag). Beskriv hva du finner og hvordan du har håndtert det.

Du skal kombinere kommuneplanen med minst én annen datakilde, for eksempel:

* [AR5 arealressurskart](https://www.geonorge.no/) fra NIBIO (fulldyrka jord, skog, myr) via Geonorge
* Befolkning på rutenett (250 m) og tettstedsavgrensninger fra SSB
* Bygninger, skoler, butikker og veinett fra OpenStreetMap, etter tilnærmingen fra forelesning
* NVEs aktsomhetskart for flom og skred via [NVE Atlas](https://atlas.nve.no/) eller Geonorge
* [SSB sin statistikkbank](https://www.ssb.no/statbank) (befolkningsutvikling, boligbygging)

#### Eksempelanalyser

Verktøyet skal beregne 2-4 indikatorer for de områdene du sammenligner. Her er noen eksempler:

**Arealregnskap**

- Beregn hvor stor andel av arealet som er avsatt til de ulike formålene, både nåværende og framtidig
- Beregn hvor mye nytt areal som er avsatt til bolig, fritidsbolig og næring
- Visualiser arealfordelingen som kart og grafer (f.eks. stolpediagram per sted)

**Konflikt med fare og støy**

- Finn hvor mye av de framtidige byggeområdene som ligger innenfor flom-, skred- eller støysoner (overlay)
- Beregn andelen per formål og per sted, og finn de mest utsatte områdene
- Lag kart som viser konfliktområdene

**Jordvern**

- Hent AR5-data og finn hvor mye fulldyrka jord som ligger i framtidige byggeområder
- Sammenlign stedene
- Visualiser resultatene i kart og grafer

**Lokalisering og tilgjengelighet**

- Beregn avstand fra nye boligområder til tettstedssenter, skole eller butikk (buffer, nærmeste nabo, eller korteste vei i et nettverk)
- Vurder om ny utbygging legges nær eksisterende sentre eller spres utover
- Visualiser fordelingen av avstander (f.eks. histogram) og lag kart

**Vern og hensyn**

- Finn hvor mye av utbyggingsarealet som berører hensynssoner for kulturmiljø, naturvern eller drikkevann
- Oppsummer hvilke hensyn som oftest blir berørt

#### Struktur i oppgaven for kommuneplanens arealdel

Strukturen er den samme som for urbane indikatorer. Arbeidet bør inkludere:

* Et emne for arbeidet ditt (f.eks. "Kommuneplanens arealdel: utbygging, flomfare og jordvern i Bjørkelangen og Løken").
* En kort introduksjon til emnet (presenter 2-4 forskningsspørsmål som du vil besvare ved hjelp av indikatorene)
* Kort beskrivelse av datasettene du brukte, og hvordan du har (pre-)prosessert dataene
* Kort generell beskrivelse av metodene du brukte
* Faktiske koder og visualiseringer for å produsere resultatene
* Kort diskusjon relatert til resultatene (hva bør vi forstå og se fra dem?)
* Kort refleksjon om analysen, for eksempel: Hvilke antakelser, skjevheter eller usikkerheter er knyttet til dataene og/eller analysene? (Hint: hvor nøyaktig er en plangrense, og hva betyr det at et byggeområde overlapper en faresone med noen få kvadratmeter?)

#### Tekniske hensyn

Pass på at du:

* Dokumenterer analysene dine godt ved å bruke Markdown-celler og beskriver 1) hva du gjør og 2) hva du kan se fra dataene og resultatene dine.
* Bruker informative visualiseringer
  * Lag kart (statisk eller interaktivt), med en fargeskala som gjør det lett å skille arealformålene fra hverandre
  * Lag andre typer grafer (f.eks. stolpediagrammer, histogrammer osv.)
  * Bruk flere plott som gjør det enkelt å sammenligne områdene side om side
* Skriver funksjoner for de repeterende delene av koden, og lagrer dem i en egen .py-fil som du importerer i notatboken. Som en motivasjon: alle kommuner i Norge leverer kommuneplanen sin etter den samme SOSI-standarden. Skriv koden slik at den kan kjøres på kommuneplanen til en annen kommune, eller på andre steder i kommunen, bare ved å endre inndata eller parametere.


### Egendefinert prosjekt

Utvikle ditt eget emne! Generelt bør ditt eget emne også inneholde disse seksjonene:

* Datainnhenting (Hente data, filtrere data, lagre midlertidig utdata osv.)

* Dataanalyse (Berike og analysere dataene, f.eks. romlig koblinger, overlay, buffering, andre beregninger..)

* Visualisering (Visualisere hovedresultater og annen relevant informasjon som kart og grafer)

Men føl deg fri til å være kreativ! Ditt eget prosjekt kan for eksempel være relatert til et prosjekt i andre fag eller masteroppgave. Husk å beskrive tydelig hva du gjør i den endelige oppgavens README.md-fil. Hvis du velger et egendefinert prosjekt, må du få godkjenning på prosjektet før du setter ordentlig i gang.

Det som minst kreves av det endelige prosjektet, er at du har:

* Fungerende kode for oppgaven / problemet / analysene som løser oppgaven

* God dokumentasjon (dvs. en veiledning) som forklarer hvordan verktøyet ditt fungerer ELLER en rapport om analysene dine og hva vi kan lære av dem
