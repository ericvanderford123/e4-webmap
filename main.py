import csv


MAPNAME='data/map1.html'
if __name__ == '__main__':
    import folium
    dir(folium)
    map = folium.Map(location=(35.61,-82.44), zoom_start = 6)


    with open('data/volcanoes.tsv') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read())
        csvfile.seek(0)
        reader= csv.DictReader(csvfile, dialect=dialect)
        rows = []
        for row in reader:
            if not (row["Volcano Name"]=="Unnamed" or row["Last Known Eruption"]=="?"):
                rows.append(row)
                print(row)
        for i in range(0, len(rows)):
            icon_yellow = folium.Icon(color='yellow')
            folium.Marker(
                location=[rows[i]['Latitude'], rows[i]['Longitude']],
                popup=rows[i]['Volcano Name'], icon=icon_yellow
            ).add_to(map)

    map.save(MAPNAME)


