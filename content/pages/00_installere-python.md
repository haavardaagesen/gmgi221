# 📖 Installering av Python og Python pakker



1. **Last ned Miniconda**: Besøk [Miniconda nedlastingssiden](https://docs.conda.io/en/latest/miniconda.html) og last ned installasjonsprogrammet for ditt operativsystem (Windows, macOS eller Linux).

2. **Installer Miniconda**:
   - **Windows**: Kjør installasjonsprogrammet og følg instruksjonene. Sørg for å merke av for å legge til Miniconda i PATH.
   - **macOS/Linux**: Åpne et terminalvindu og kjør det nedlastede skriptet. Følg instruksjonene for å fullføre installasjonen.

3. **Last ned YAML-filen til emnet**
   - Høyreklikk på [denne linken til YAML-filen](https://raw.githubusercontent.com/haavardaagesen/gmgi221/main/content/gmgi221-environment.yml) og lagre den lokalt.

4. **Opprett miljøet fra YAML-filen**:
   - Åpne et terminalvindu (eller Anaconda Prompt på Windows).
   - Naviger til mappen der `gmgmi221-environment.yml` er lagret.
   - Bruk kommandoen: `conda env create -f gmgmi221-environment.yml`

5. **Aktiver miljøet**:
   - **Windows/Linux**: `conda activate gmgi221`
   - **macOS/Linux**: `source activate gmgi221`

6. **Deaktiver miljøet**:
   - Når du er ferdig, deaktiver miljøet med `conda deactivate`.


