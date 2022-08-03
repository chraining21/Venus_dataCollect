ing = "Cetyl PEG/​PPG-10/​1 Dimethicone"
ing = ing.replace('\u200b',"")
search=""
for a in ing:
    if (a.isalnum()):
        count = 0
        search += a.lower()

    else:
        search += "-"
print(search)