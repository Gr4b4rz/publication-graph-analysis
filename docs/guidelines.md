# Temat projektu
PB3 - Należy pobrać z bazy IEEE Xplore listę publikacji afiliowanych przy „Warsaw University
of Technology” w latach 2017-2020, utworzyć na jej podstawie graf, którego wierzchołkami
są publikacje i autorzy (tylko autorzy z afiliacją WUT), a krawędziami autorstwo publikacji
(jest to graf dwudzielny), a następnie poddać ten graf analizie (rozkład stopni, rozkład
długości drogi między wierzchołkami reprezentującymi autorów, i in.).

## Pobieranie danych
Dane niezbędne do realizacji zadania zostaną pobrane bezpośrednio ze strony: <https
://ieeexplore.ieee.org> w formacie ‘csv’. Wolumen danych nie przekracza maksymalnie
oferowanych 2000 rekordów, dzięki czemu wszystkie publikacje(około 1240) z roczników
2017-2020 będą mogły być poddane analizie.

## Analiza danych
W ramach analizy należy wykonać następujące zadania:
- Wyznaczyć rozkład stopni wierzchołków - Graf jest dwudzielny i ma dwie kategorie
  wierzchołków (publikacje i autorzy). Z tego powodu trzeba wyznaczyć osobny rozkład
  dla publikacji i dla autorów.
- Wyznaczyć rozkład długości drogi między wierzchołkami reprezentującymi autorów -
Trzeba stworzyć graf pochodny (graf współautorstwa), w którym wierzchołkami są tylko
autorzy, a krawędziami współautorstwo artykułu i dla tak utworzonego grafu, wyznaczyć
rozkład długości drogi.

- Zbadać spójność grafu i podać rozkład liczby wierzchołków składowych spójnych -  Rozkłady
wierzchołków należy wyznaczyć osobno dla dwóch typów wierzchołków.
- Dla grafu współautorstwa wyznaczyć rozkład stopnia zwielokrotnienia równoległych krawędzi
grafu - Będzie to rozkład liczby wspólnych publikacji dla każdej pary autorów. Z takiego
rozkładu będzie można dowiedzieć się jak często ci sami autorzy publikują razem.

- Wyznaczyć rozkład odsetka wspólnych publikacji - Dla pary autorów, odsetek ten, będzie
stosunkiem liczby wspólnych publikacji do liczby publikacji tego autora, który ma ich
mniej. W analizie zostaną uwzględnieni tylko ci autorzy, którzy mają co najmniej 3
publikacje. Z owego rozkładu można będzie dowiedzieć się, jak ścisła jest współpraca
między autorami.

- Z grafu współautorstwa utworzyć graf prosty i wykonać następujące analizy:
  - Obliczyć gęstość grafu
  - Wyznaczyć średnią wartość współczynnika klasteryzacji wierzchołków. Należy przyjąć,
    że wierzchołki izolowane i wierzchołki wiszące mają współczynnik klasteryzacji równy 0.
  - Wyznaczyć rozkład współczynnika klasteryzacji wierzchołków. Należy uwzględnić tylko
    wierzchołki stopnia 4 i więcej.
  - Wylistować współczynniki klasteryzacji wierzchołków dla 25 autorów o największej
    liczbie publikacji. W większości będą to prawdopodobnie profesorowie. Ze stworzonej
    listy będzie można dowiedzieć się czy utworzyli oni współpracujące ze sobą zespoły

Wstępnie zakładamy, że powyższe analizy zostaną wykonane w języku Python przy użyciu
biblioteki NetworkX.
