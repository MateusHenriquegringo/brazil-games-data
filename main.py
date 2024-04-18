import csv as csv

from tools import dataformat

brasilgames = []
header = "date,home_team,away_team,home_score,away_score,tournament,city,country,neutral"

with open("./archive/results.csv", "r") as results:
    data = list(csv.reader(results))
    for row in data:
        if row[1]=="Brazil" or row[2] == "Brazil":
            brasilgames.append(row)

with open("./archive/brazilresults.csv", "w") as brazil:
    data = csv.writer(brazil, quotechar=",", quoting=csv.QUOTE_MINIMAL)
    brasilgames.insert(0, header)
    for row in brasilgames:
        print(row)
        data.writerow(dataformat(row))

## transformar lista em dicionario
## formatar data
