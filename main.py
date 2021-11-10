import csv
fv= open("data/volcanoes.tsv","r")
with open('data/volcanoes.tsv') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read())
    csvfile.seek(0)
    reader= csv.DictReader(csvfile, dialect=dialect)
    rows = []
    for row in reader:
        print(rows.append(row))

MAPNAME='data/map1.html'
if __name__ == '__main__':
    import folium
    dir(folium)
    map = folium.Map(location=(35.61,-82.44), zoom_start = 10)
    map.save(MAPNAME)



