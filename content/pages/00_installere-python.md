# 📖 Installering av Python og Python pakker

I dette emnet, så anbefales det sterkt at du setter opp et Python-miljø på din egen datamaskin. Under finner du en guide til hvordan du kan gjøre det, og hvis du har utfordringer med å få satt det opp, så anbefaler jeg å møte opp og få hjelp i øvingstimene!

1. **Last ned Miniconda**: Besøk [Miniconda nedlastingssiden](https://docs.conda.io/en/latest/miniconda.html) og last ned installasjonsprogrammet for ditt operativsystem (Windows, macOS eller Linux).

2. **Installer Miniconda**:
   - **Windows**: Kjør installasjonsprogrammet og følg instruksjonene. Sørg for å merke av for å legge til Miniconda i PATH.
   - **macOS/Linux**: Åpne et terminalvindu og kjør det nedlastede skriptet. Følg instruksjonene for å fullføre installasjonen.

3. **Last ned YAML-filen til emnet**
   - Høyreklikk på [denne linken til YAML-filen](https://raw.githubusercontent.com/haavardaagesen/gmgi221/main/content/gmgi221-environment.yml) og lagre den lokalt.

4. **Opprett miljøet fra YAML-filen**:
   - Åpne et terminalvindu (eller Mini Prompt på Windows).
   - Først kan det være lurt å oppdatere conda, bruk kommandoen: `conda update -n base conda`
   - For å gjøre installasjonen raskere kan du installere og bruke libmamba, bruk kommanoen `conda install -n base conda-libmamba-solver`
   - Bruk så kommandoen `conda config --set solver libmamba`
   - Naviger til mappen der `gmgi221-environment.yml` er lagret.
   - Bruk kommandoen: `conda env create -f gmgi221-environment.yml`

5. **Aktiver miljøet**:
   - **Windows/Linux**: `conda activate gmgi221`
   - **macOS/Linux**: `source activate gmgi221`

6. **Deaktiver miljøet**:
   - Når du er ferdig, deaktiver miljøet med `conda deactivate`.


