# 📖 Installering av Python og Python-pakker

I dette emnet anbefales det sterkt at du setter opp et Python-miljø på din egen
datamaskin. Under finner du en steg-for-steg-guide. Får du det ikke til, kom
innom øvingstimene – da hjelper vi deg i gang.

Vi bruker **conda** til å håndtere Python og alle pakkene vi trenger. Alle
pakkene i emnet (`geopandas`, `shapely`, `rasterio` med flere) samles i ett
*miljø* (`environment`) som heter `gmgi221`, definert i fila `environment.yml` i
[emnets GitHub-repo](https://github.com/haavardaagesen/gmgi221).

```{admonition} Kort versjon (for deg som har gjort dette før)
:class: tip

Installer **Miniforge**, last ned `environment.yml`, og kjør:

    conda env create -f environment.yml
    conda activate gmgi221
    jupyter lab
```

## 1. Installer Miniforge

Vi anbefaler å bruke **Miniforge**, for å håndtere oppsett av Python-miljø, hvis du ikke allerede har et fungerende miljø.

1. Gå til [Miniforge-nedlastingssiden](https://conda-forge.org/download/).
2. Last ned installasjonsprogrammet for operativsystemet ditt (Windows, macOS
   eller Linux).
3. Installer:
   - **Windows**: Kjør `.exe`-fila og følg veiviseren. Bruk standardvalgene.
   - **macOS / Linux**: Åpne en terminal, gå til mappen der fila lastet ned, og
     kjør skriptet, f.eks.:

         bash Miniforge3-MacOSX-arm64.sh

     Svar `yes` når du blir spurt om å initialisere conda.
4. **Lukk terminalen / kommandovinduet og åpne et nytt.** På Windows får du nå
   en oppføring som heter **Miniforge Prompt** i Start-menyen – det er den du
   skal bruke. På macOS/Linux skal det stå `(base)` foran ledeteksten i
   terminalen.

## 2. Hent miljøfila til emnet

Du trenger fila `environment.yml` fra emnets repo. Velg **én** av måtene:

- **Enklest:** Last ned filen `environment.yml` fra canvas.
- **Last ned fra GitHub:** Åpne
  [environment.yml](https://github.com/haavardaagesen/gmgi221/blob/main/environment.yml)
  på GitHub og trykk **Download raw file** (nedlastingsikonet oppe til høyre).
- **Kan du git?** `git clone https://github.com/haavardaagesen/gmgi221.git`

## 3. Opprett miljøet

1. Åpne **Miniforge Prompt** (Windows) eller en terminal (macOS/Linux).
2. Naviger til mappa der `environment.yml` ligger. Bruk `cd`, f.eks.:

       cd Downloads/gmgi221

   (På Windows: `cd C:\Users\dittnavn\Downloads\gmgi221`.)
3. Opprett miljøet:

       conda env create -f environment.yml

   Dette tar noen minutter – conda laster ned og setter opp alle pakkene.

```{admonition} «CondaValueError: prefix already exists»
:class: note

Får du denne feilmeldingen? Da finnes miljøet fra før. Oppdater det i stedet – se
[Oppdatere miljøet](#oppdatere-miljøet) nederst på siden.
```

## 4. Aktiver miljøet

    conda activate gmgi221

Ledeteksten skal nå starte med `(gmgi221)` i stedet for `(base)`. Miljøet må
aktiveres i **hvert nytt terminalvindu** før du jobber med emnet.

For å gå ut av miljøet igjen:

    conda deactivate

## 5. Sjekk at alt virker

Med `(gmgi221)` aktivert, kjør:

    python -c "import geopandas, shapely, rasterio, osmnx; print('OK', geopandas.__version__)"

Får du `OK` og et versjonsnummer, er du klar.

## 6. Start JupyterLab

    conda activate gmgi221
    jupyter lab

JupyterLab åpner seg i nettleseren. Når du lager eller åpner en notebook, må du
velge **kjernen (kernel)** som heter `Python 3 (ipykernel)` fra `gmgi221`-miljøet
– sjekk øverst til høyre i notebooken at riktig miljø er valgt.

Avslutt JupyterLab med `Ctrl + C` i terminalen når du er ferdig.

## Daglig bruk

Hver gang du skal jobbe med emnet:

1. Åpne Miniforge Prompt / en terminal
2. `conda activate gmgi221`
3. `jupyter lab`


## Oppdatere miljøet

`environment.yml` kan bli oppdatert i løpet av semesteret. Da henter du den nye
fila (steg 2) og kjører, fra mappa der den ligger:

    conda activate gmgi221
    conda env update -f environment.yml --prune

`--prune` fjerner pakker som ikke lenger står i fila.

## Får du det ikke til?

Kom innom øvingstimene, eller send en melding på Canvas. Ta gjerne med en
skjermdump av feilmeldingen du får.
