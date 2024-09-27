ogolnie to rozumiem zdecydowana wiekszosc kodu, robilem to oczywiscie z chatem, pierwsza metode zrobilem SelectFromModel, zajelo to okolo godziny, druga juz robilem kolo 15 minut. wyniki porownalem, i sa identyczne w obu przypadkach. nie bede recznie tego sprawdzac by to potwierdzic bo jestem leniem, a pewnie ktos z klasy tak zrobi, a z reszta wtedy sie porowna czy wyszlo to samo. wyniki daje ponizej:

# SelectFromModel:

```py
Wybrane cechy: ['StudyTimeWeekly', 'Absences', 'GPA']
Liczba wybranych cech: 3
Dokładność modelu na wyselekcjonowanych cechach: 91.64%
```

# SelectKBest:

```py
Wybrane cechy: ['StudyTimeWeekly', 'Absences', 'GPA']
Liczba wybranych cech: 3
Dokładność modelu na wyselekcjonowanych cechach: 91.64%
```

# Sa one doslownie identyczne
###### BM 3P
