from csv import reader
def import_csv_layout(path):
    terrain = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter= ',')
        for row in layout:
            terrain.append(list(row))
        return terrain