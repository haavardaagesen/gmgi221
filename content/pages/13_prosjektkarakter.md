# 📖 Karaktersetting for prosjektoppgaven

Prosjektoppgaven utgjør 60 % av karakteren i emnet, og øvingsoppgavene 40 %. Prosjektoppgaven vurderes med **120 poeng**, og øvingsoppgavene gir til sammen **80 poeng**. Til sammen kan du altså få **200 poeng**, og den endelige karakteren settes ut fra prosentandelen av disse.

| Karakter | Prosent    | Poeng (av 200) |
| -------- | ---------- | -------------- |
| A        | 90–100 %   | 180–200        |
| B        | 80–89 %    | 160–179        |
| C        | 60–79 %    | 120–159        |
| D        | 50–59 %    | 100–119        |
| E        | 40–49 %    | 80–99          |
| F        | under 40 % | under 80       |

Vurderingen skjer i to steg: først sjekkes minstekravene, deretter gis det poeng etter vurderingskriteriene.

## Steg 1: Minstekrav

Før oppgaven får poeng, sjekkes det at innleveringen oppfyller disse kravene:

* Innleveringen er **én zip-mappe** på Canvas, levert innen fristen.
* Mappen inneholder en **README.md** som forklarer hva prosjektet handler om, og som lenker til alle relevante filer.
* Koden **kan kjøres** fra start til slutt med dataene som følger med eller som er beskrevet i README.md. Pakker som ikke er brukt i emnets python-miljø, skal være nevnt i README.md med installasjonsinstruksjoner.
* Oppgaven oppfyller **kravene til prosjektet du har valgt** (f.eks. 2-4 indikatorer og minst to områder som sammenlignes). Egendefinerte prosjekter må være godkjent på forhånd.
* Det er levert en **erklæring om bruk av KI**, også dersom du ikke har brukt KI, enten som en del av README.md eller som en egen Markdown-fil.

Hvis koden ikke kjører på grunn av små feil, som en filsti som må endres, retter sensor feilen og trekker poeng under kriterium D. Hvis større deler av koden ikke kjører, vurderes bare de delene som fungerer. Bruk av agentisk KI, eller bruk av KI som ikke er dokumentert, behandles etter universitetets regler for juks.

## Steg 2: Vurderingskriterier

| Kriterier                           | Poeng   |
| ----------------------------------- | ------- |
| A. Datainnhenting og databehandling | 20      |
| B. Romlig analyse og indikatorer    | 30      |
| C. Visualisering                    | 20      |
| D. Kodekvalitet og gjentakbarhet    | 20      |
| E. Dokumentasjon og rapport         | 20      |
| F. Ekstra                           | 10      |
| **Sum**                             | **120** |



### A. Datainnhenting og databehandling (20 poeng)

Lesing av data fra filer eller API-er, datarensing, filtrering, tabellkoblinger, håndtering av koordinatsystemer og lagring av mellomresultater.

| Poeng | Beskrivelse                                                                                                                                                           |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0–5   | Dataene leses inn, men lite eller ingen behandling. Feil i dataene oppdages ikke.                                                                                     |
| 6–11  | Grunnleggende behandling (filtrering, utvalg av kolonner). Noen åpenbare datafeil er ikke håndtert, eller koordinatsystemer er ikke kontrollert.                      |
| 12–16 | Dataene renses og kobles på en riktig måte. Koordinatsystemer er håndtert. Valgene er forklart.                                                                       |
| 17–20 | Som over, og i tillegg grundig kontroll av datakvaliteten, flere datakilder kombinert på en god måte, og mellomresultater lagret slik at arbeidsflyten blir effektiv. |

### B. Romlig analyse og indikatorer (30 poeng)

Valg og gjennomføring av analysemetoder (f.eks. romlig kobling, overlay, buffer, nettverksanalyse, aggregering), og om indikatorene faktisk svarer på forskningsspørsmålene. Vanskelighetsgraden i analysen vurderes her.

| Poeng | Beskrivelse                                                                                                                                    |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 0–8   | Lite romlig analyse, eller metodene gir feil resultat. Indikatorene henger ikke sammen med forskningsspørsmålene.                              |
| 9–17  | Enkle analyser som i hovedsak er riktige (f.eks. én type overlay eller enkel aggregering). Indikatorene beregnes, men er lite begrunnet.       |
| 18–25 | Flere romlige analysesteg som er riktig gjennomført. Indikatorene er godt valgt og begrunnet, og områdene sammenlignes på en meningsfull måte. |
| 26–30 | Som over, og i tillegg analyser med høyere vanskelighetsgrad eller som kombinerer flere metoder, med god vurdering av hva resultatene betyr.   |

### C. Visualisering (20 poeng)

Kart og grafer: om de er lesbare og korrekte, og om de støtter konklusjonene.

| Poeng | Beskrivelse                                                                                                                                                                        |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0–5   | Få figurer, eller figurer som er misvisende eller ikke kan leses.                                                                                                                  |
| 6–12  | Figurene finnes, men mangler titler, tegnforklaring, enheter eller passende fargeskala.                                                                                            |
| 13–17 | Tydelige kart og grafer med titler, tegnforklaring og passende fargeskala. Figurene støtter konklusjonene.                                                                         |
| 18–20 | Godt gjennomarbeidede figurer, f.eks. med underplott som gjør det enkelt å sammenligne områdene side om side, eller interaktive kart, som svarer direkte på forskningsspørsmålene. |

### D. Kodekvalitet og gjentakbarhet (20 poeng)

Om koden er modulær (funksjoner og løkker i stedet for gjentakelse), om analysen kan gjentas med andre inndata eller parametere, om koden kjører uten feil, og om den følger PEP8.

| Poeng | Beskrivelse                                                                                                                                                                  |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0–5   | Koden kjører ikke, eller er i stor grad kopiert og limt inn for hvert område.                                                                                                |
| 6–11  | Koden kjører, men har mye gjentakelse. Få eller ingen egne funksjoner. Inndata er hardkodet mange steder.                                                                    |
| 12–16 | Egne funksjoner for de viktigste stegene. Analysen kan gjentas for et nytt område ved å endre noen få parametere. Koden er stort sett i tråd med PEP8.                       |
| 17–20 | Funksjoner er samlet i en egen .py-fil med docstrings, og analysen kan kjøres for nye områder eller nye inndata uten å endre koden. Koden er ryddig og konsekvent formatert. |

### E. Dokumentasjon og rapport (20 poeng)

README.md, Markdown-celler og kodekommentarer. Rapporten bør inneholde problemstilling, beskrivelse av data og metode, resultater, diskusjon, refleksjon om usikkerhet og erklæring om bruk av KI (enten som en del av README-filen, eller som en egen markdown-fil).

| Poeng | Beskrivelse                                                                                                                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0–5   | Lite eller ingen forklaring utover koden. Det er uklart hva prosjektet handler om.                                                                                        |
| 6–11  | Problemstilling og data er beskrevet, men resultatene er lite forklart, og diskusjon eller refleksjon mangler.                                                            |
| 12–16 | Alle delene av rapporten er med. Hvert analysesteg og hver figur er forklart. Funksjonene er beskrevet og vist i bruk.                                                    |
| 17–20 | Som over, og i tillegg en tydelig rød tråd fra forskningsspørsmål til konklusjon, og en gjennomtenkt refleksjon om antakelser, skjevheter og usikkerhet i data og metode. |

### F. Ekstra (10 poeng)

Poeng for noe som går utover kravene i A–E, for eksempel en smart løsning på et vanskelig problem, ekstra funksjonalitet i verktøyet, eller en datakilde eller metode som ikke er gjennomgått i emnet. Det samme arbeidet gir ikke poeng både her og under A–E. De fleste besvarelser vil få 0–5 poeng på dette kriteriet.

Arbeidsflyten skal være gjentakbar og godt dokumentert. Med andre ord, alle som får en kopi av innleveringen din skal kunne kjøre koden din, og lese koden din og forstå den og resultatene.
