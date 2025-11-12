# 📥 Øving 2

I denne øvingen skal du jobbe med geometriske objekter ved bruk av Shapely.

Øvingsoppgaven finner du på Canvas under Oppgaver, eller på [dette GitHub-repoet](https://github.com/GMGI221/gmgi221-oving).

Last den ned, åpne den i Jupyter Notebooks/Lab eller den editoren du bruker og følg instruksjonene i Notebooken. Lever den så inn på Canvas etter du har endret navn til "oving2-ditt_navn.ipynb".

## Tips til oppgaven:
### Assertions

Påstander (assertions) er en språkfunksjon i Python som lar programmereren påstå, og sikre, at en viss betingelse er oppfylt. De er en god måte å sjekke at variabler er innenfor et passende område for videre beregning. For eksempel, hvis en funksjon konverterer en temperatur, kan den teste at inputverdien ikke er under absolutt nullpunkt. På en måte fungerer assert-påstander likt som en elektrisk sikring: hvis inngangsstrømmen er høyere enn forventet, går sikringen for å beskytte apparatet som kommer etter. Hvis inputverdiene er utenfor et forventet område, feiler assert-påstanden med en feil, og stopper programmet for å beskytte den påfølgende koden fra å bli kjørt med feil input.

assert-setninger brukes ofte i funksjoner for å sikre at inputverdiene er akseptable. Vurder følgende eksempel:

```python 
def divide(dividend, divisor):
    """Return the division of dividend by divisor."""
    assert divisor != 0, "Cannot divide by zero."
    return (dividend / divisor)
```