
soubor = "polednice.txt"
with open(soubor, 'r', encoding="utf -8") as f:
     text = f.read()

slova = text.split()
print("pocet slov v textu", len(slova))

text_bez_mezer = text.replace(" ", "").replace("/n", "")

pocty_pismen = {}

for pismeno in text_bez_mezer:
     if pismeno in pocty_pismen:
          pocty_pismen[pismeno] += 1
     else:
        pocty_pismen[pismeno] = 1

seznam_pismen = sorted(pocty_pismen.items(), key = lambda x: x[1], reverse=True)

print("/nejčastější písmena")
for pismeno, pocet in seznam_pismen [:10]:
      print(pismeno, pocet)

osmipismenna = set()

for slovo in slova:
    if len(slovo) == 8:
        osmipismenna.add(slovo)

print("\nPočet různých osmipísmenných slov:")
print(len(osmipismenna))

