filmy = [
    ("The Shawshank Redemption", 1994, 9.3),
    ("The Godfather", 1972, 9.2),
    ("The Dark Knight", 2008, 9.0),
    ("Pulp Fiction", 1994, 8.9),
    ("Forrest Gump", 1994, 8.8),
    ("Inception", 2010, 8.8),
    ("Fight Club", 1999, 8.8),
    ("The Matrix", 1999, 8.7),
    ("Interstellar", 2014, 8.6),
    ("Parasite", 2019, 8.6)
]


filmy_21stoleti = [film for film in filmy if film[1] >= 2000]
print(filmy_21stoleti)


serazene_podle_hodnoceni = sorted(filmy, key=lambda f: f[2], reverse=True)


import matplotlib.pyplot as plt

hodnoceni = [f[2] for f in filmy]

plt.hist(hodnoceni, bins=5, edgecolor="black")
plt.title("Histogram hodnocení filmů")
plt.xlabel("Hodnocení")
plt.ylabel("Počet filmů")
plt.show()
