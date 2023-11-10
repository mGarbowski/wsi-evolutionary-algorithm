# Ćwiczenie 2 - sprawozdanie
Mikołaj Garbowski

Przedmiotem zadania jest
* implementacja klasycznego algorytmu ewolucyjnego
  * selekcja turniejowa
  * sukcesja generacyjna
  * ograniczenia kostkowe przestrzeni do $[-100, 100]$
  * bez krzyżowania
* Optymalizacja funkcji f2 i f13 z pakietu CEC2017 w 10 wymiarach
  * budżet $10 000$ ewaluacji funkcji celu
  * dobranie najlepszych parametrów algorytmu (rozmiar populacji i siła mutacji) drogą eksperymentalną
  * powtórzenie eksperymentu z dobranymi parametrami i budżetem $50 000$ ewaluacji funkcji celu

Implementacja algorytmu znajduje się w module `evolution.py`.
Kod wykonujący eksperymenty i pomiary, na podstawie których powstały poniższe tabele znajduje się w module `benchmark.py`.

## Wyniki eksperymentów dla funkcji $f2$
Eksperymenty wykonywane przy budżecie ewaluacji funkcji celu $n = 10 000$ (chyba że powiedziane inaczej).
Przedstawione wyniki są zagregowane z 25 powtórzeń algorytmu.

### Siła mutacji $\sigma = 3.0$ i różne rozmiary populacji
Najmniejsza minimalna wartość funkcji celu dla $\mu = 16$.

| Function | Samples | Sigma | Mu | Avg        | Std        | Min      | Max         |
|----------|---------|-------|----|------------|------------|----------|-------------|
| f2       | 25      | 3.0   | 4  | 242407.25  | 271422.62  | 22681.78 | 1221276.00  |
| f2       | 25      | 3.0   | 8  | 641217.79  | 1129079.81 | 13959.04 | 5791445.88  |
| f2       | 25      | 3.0   | 16 | 370691.77  | 595703.81  | 6689.14  | 2786913.69  |
| f2       | 25      | 3.0   | 32 | 534202.86  | 560058.36  | 19144.70 | 2387554.33  |
| f2       | 25      | 3.0   | 64 | 1658965.43 | 2795865.57 | 15916.55 | 10266689.93 |

### Populacja $\mu = 16$ i różne siły mutacji
Najmniejszą średnią wartość funkcji celu, najmniejsze odchylenie standardowe dają parametry $(\mu = 16, \sigma = 1.0)$.
Najmniejszą wartość minimalną funkcji celu dały parametry $(\mu = 16, \sigma = 0.5)$

| Function | Samples | Sigma | Mu | Avg                | Std                 | Min          | Max                  |
|----------|---------|-------|----|--------------------|---------------------|--------------|----------------------|
| f2       | 25      | 0.5   | 16 | 2475752.24         | 9395141.75          | 211.75       | 47960608.69          |
| f2       | 25      | 1.0   | 16 | 10590.86           | 7850.15             | 448.90       | 26471.98             |
| f2       | 25      | 2.0   | 16 | 133610.69          | 234868.58           | 1165.76      | 1087886.96           |
| f2       | 25      | 3.0   | 16 | 550647.39          | 1456009.36          | 6112.84      | 7285039.42           |
| f2       | 25      | 5.0   | 16 | 4970614.57         | 10172104.63         | 69827.51     | 35395454.57          |
| f2       | 25      | 10.0  | 16 | 40830815.83        | 49114837.37         | 553428.03    | 225968124.07         |

### Najlepsze parametry z poprzednich eksperymentów i 5-krotnie większy budżet
Budżet $n = 50 000$ ewaluacji funkcji celu.

Wartości minimalnie są dla obu przypadków lepsze niż przy mniejszym budżecie.
Rozstrzał znalezionych wartości jest znacznie mniejszy niż przy mniejszym budżecie
(średnia bardziej zbliżona do minimum, mniejsze odchylenie standardowe, mniejsza różnica między minimum a maximum)

| Function | Samples | Sigma | Mu | Avg     | Std     | Min    | Max      |
|----------|---------|-------|----|---------|---------|--------|----------|
| f2       | 25      | 0.5   | 16 | 268.79  | 47.35   | 201.68 | 344.07   |
| f2       | 25      | 1.0   | 16 | 1407.53 | 2306.83 | 238.41 | 10603.82 |

## Wyniki eksperymentów dla funkcji $f13$

### Siła mutacji $\sigma = 3.0$, różne rozmiary populacji
Najlepsze wyniki są zbliżone dla rozmiarów populacji $\mu = 8$ i $\mu = 16$

| Function | Samples | Sigma | Mu | Avg      | Std      | Min      | Max       |
|----------|---------|-------|----|----------|----------|----------|-----------|
| f13      | 25      | 3.0   | 4  | 70687.95 | 74279.41 | 7441.34  | 411567.59 |
| f13      | 25      | 3.0   | 8  | 56627.61 | 34547.14 | 4842.34  | 144844.11 |
| f13      | 25      | 3.0   | 16 | 44024.66 | 33500.39 | 5062.28  | 163755.31 |
| f13      | 25      | 3.0   | 32 | 56805.06 | 44975.23 | 8696.62  | 206196.22 |
| f13      | 25      | 3.0   | 64 | 49152.40 | 20741.93 | 15049.82 | 100653.95 |

### Populacja $\mu \in \{8, 16\}$, różne siły mutacji
Najlepsze wyniki dla $(\mu, \sigma) = (8, 1.0)$ i $(\mu, \sigma) = (16, 0.5)$
(Małe średnie, odchylenia standardowe i wartości minialne)

| Function | Samples | Sigma | Mu | Avg         | Std          | Min      | Max           |
|----------|---------|-------|----|-------------|--------------|----------|---------------|
| f13      | 25      | 0.1   | 8  | 17976.55    | 14634.22     | 3679.23  | 69707.98      |
| f13      | 25      | 0.5   | 8  | 15688.87    | 11469.82     | 2921.41  | 43673.25      |
| f13      | 25      | 1.0   | 8  | 14645.26    | 9611.79      | 2788.78  | 33267.22      |
| f13      | 25      | 2.0   | 8  | 28634.55    | 14274.28     | 5578.03  | 55443.31      |
| f13      | 25      | 3.0   | 8  | 50899.61    | 23186.49     | 4683.57  | 92856.28      |
| f13      | 25      | 5.0   | 8  | 83647.22    | 60841.57     | 10234.62 | 240575.07     |
| f13      | 25      | 10.0  | 8  | 489460.10   | 442514.91    | 24867.89 | 1696281.14    |
| f13      | 25      | 0.1   | 16 | 92663404.93 | 453868182.35 | 2350.97  | 2316154318.58 |
| f13      | 25      | 0.5   | 16 | 16471.38    | 11937.27     | 2353.73  | 42988.89      |
| f13      | 25      | 1.0   | 16 | 18823.59    | 11456.61     | 4825.83  | 51377.23      |
| f13      | 25      | 2.0   | 16 | 28660.25    | 18254.54     | 3080.04  | 71177.25      |
| f13      | 25      | 3.0   | 16 | 39571.62    | 28662.62     | 2525.44  | 132058.68     |
| f13      | 25      | 5.0   | 16 | 107441.06   | 90993.70     | 26504.96 | 339678.24     |
| f13      | 25      | 10.0  | 16 | 400771.72   | 534698.49    | 24310.53 | 1952997.10    |

### Najlepsze parametry z poprzednich eksperymentów i 5-krotnie większy budżet
Budżet $n = 50 000$ ewaluacji funkcji celu.

W obu przypadkach nieznaczna poprawa średniego wyniku i odchylenia standardowego oraz gorsze wartości minimalne względem eksperymentów z mniejszym budżetem.

| Function | Samples | Sigma | Mu    | Avg         | Std         | Min         | Max         |
|----------|---------|-------|-------|-------------|-------------|-------------|-------------|
|      f13 |      25 |   1.0 |     8 |    13780.90 |     9329.16 |     3540.73 |    48721.73 |
|      f13 |      25 |   0.5 |    16 |    12760.74 |    10265.99 |     2367.58 |    39425.68 |

## Wnioski
* Parametry algorytmu dające najlepsze rezultaty były zbliżone dla obu testowanych funkcji
* Poprawa rezultatów wynikająca ze zwiększenia budżetu ewaluacji funkcji celu była bardziej zauważalna dla funkcji $f2$
* Mniejsza populacja rzędu $8$-$16$ (więc dłuższa ewolucja przy stałym budżecie) daje lepsze rezultaty
* Bardzo mała siła mutacji $\mu = 0.1$ dawała najgorsze wartości średnie i maksymalne
* Najlepsze wyniki dawały małe siły mutacji rzędu $0.5$-$1.0$
* Wyniki eksperymentów z jednakowymi parametrami znacząco różnią się między sobą (jak widać po dużych rozbieżnościach między wynikami minimalnymi i maksymalnymi) 