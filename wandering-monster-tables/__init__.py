import csv



def load_data(file):
#    load file
#    return data
    with open("data/" + file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        output = []
        for row in spamreader:
            #print(", ".join(row))
            output.append({
                    "name": row[0],
                    "size": row[1],
                    "cr": row[2],
                    "type": row[3],
                    "alignment": row[4],
            })
        return output

def transform_data(data, keyname, keys):
    out = {}
    for key in keys:
        out[key] = []
    for row in data:
        for key in keys:
            if row[keyname] == key:
                out[key].append(row)
    return out

{
"1/8" : [ {"name": "bandit"}, {"name": "skeleton"}, ],
"1/4" : [ {"name": "bandit"}, {"name": "skeleton"}, ],
"1/2" : [ {"name": "bandit"}, {"name": "skeleton"}, ],
}

# 1. load csv
# 2. generate markdown output

# need
#Number of groups
#Which group a monster is in

files = [
    "cave.csv",
    "dungeon.csv",
    "forest.csv",
    "grassland.csv",
]
crs = [
    "1/8",
    "1/4",
    "1/2",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
]
difficulties = [
    "easy",
    "medium",
    "hard",
    "deadly",
]
levels = [
    #easy        medium       hard        deadly
    #lvl1
    {
        "easy": {
            "1/8": "1d4",
            "1/4": "1d3",
            "1/2": "1",
        },
        "medium": {
            "1/8": "1d6",
            "1/4": "1d4",
            "1/2": "1d2",
        },
        "hard": {
            "1/8": "2d4",
            "1/4": "1d6",
            "1/2": "1d2",
            "1": "1",
        },
        "deadly": {
            "1/8": "2d6",
            "1/4": "2d4",
            "1/2": "1d4",
            "1": "1d2",
        },
    },
    #lvl2
    {
        "easy": {
            "1/8": "1d8",
            "1/4": "1d6",
            "1/2": "1d4",
            "1": "1",
        },
        "medium": {
            "1/8": "2d4",
            "1/4": "1d6",
            "1/2": "1d4",
            "1": "1d2",
            "2": "1",
        },
        "hard": {
            "1/4": "2d4",
            "1/2": "1d6",
            "1": "1d2",
            "2": "1d2",
            "3": "1",
        },
        "deadly": {
            "1/4": "2d6",
            "1/2": "1d8",
            "1": "1d4",
            "2": "1d2",
            "3": "1",
            "4": "1",
        },
    },
    #lvl3
    {
        "easy": {
            "1/8": "2d4",
            "1/4": "1d6",
            "1/2": "1d4",
            "1": "1d2",
            "2": "1",
        },
        "medium": {
            "1/4": "2d4",
            "1/2": "1d4+1",
            "1": "1d2+1",
            "2": "1d2",
            "3": "1",
        },
        "hard": {
            "1/4": "2d6+2",
            "1/2": "1d6+2",
            "1": "1d4",
            "2": "1d2",
            "3": "1d2",
            "4": "1",
        },
        "deadly": {
            "1/2": "2d4+2",
            "1": "1d6+1",
            "2": "1d4",
            "3": "1d2",
            "4": "1d2",
            "5": "1",
        },
    },
    #lvl4
    {
        "easy": {
            "1/4": "3d4",
            "1/2": "1d4+2",
            "1": "1d4",
            "2": "1d2",
            "3": "1",
        },
        "medium": {
            "1/2": "2d4",
            "1": "1d4",
            "2": "1d2",
            "3": "1d2",
            "4": "1",
        },
        "hard": {
            "1/2": "1d6+2",
            "1": "1d4+1",
            "2": "1d4",
            "3": "1d2",
            "4": "1d2",
            "5": "1",
        },
        "deadly": {
            "1": "1d8+2",
            "2": "1d4+2",
            "3": "1d4",
            "4": "1d2",
            "5": "1d2",
            "6": "1",
            "7": "1",
        },
    },
    #lvl5
    {
        "easy": {
            "1": "1d4+2",
            "2": "1d4",
            "3": "1d2",
            "4": "1",
            "5": "1",
        },
        "medium": {
            "1": "1d6+1",
            "2": "1d4",
            "3": "1d4",
            "4": "1d2",
            "5": "1",
            "6": "1",
            "7": "1",
        },
        "hard": {
            "2": "1d4+1",
            "3": "1d4+1",
            "4": "1d4",
            "5": "1d2",
            "6": "1d2",
            "7": "1d2",
            "8": "1",
        },
        "deadly": {
            "2": "1d4+3",
            "3": "1d4+2",
            "4": "1d4",
            "5": "1d2",
            "6": "1d2",
            "7": "1d2",
            "8": "1d2",
            "9": "1",
        },
    },
    #lvl6
    {
        "easy": {
            "1": "1d4+2",
            "2": "1d4",
            "3": "1d2",
            "4": "1d2",
            "5": "1d2",
            "6": "1",
        },
        "medium": {
            "1": "1d6+2",
            "2": "1d4+1",
            "3": "1d4",
            "4": "1d2",
            "5": "1d2",
            "6": "1d2",
            "7": "1",
        },
        "hard": {
            "2": "1d4+2",
            "3": "1d4",
            "4": "1d2+1",
            "5": "1d2+1",
            "6": "1d2+1",
            "7": "1d2",
            "8": "1",
            "9": "1",
        },
        "deadly": {
            "2": "1d6+2",
            "3": "1d6+2",
            "4": "1d4+2",
            "5": "1d4+1",
            "6": "1d2+1",
            "7": "1d2+1",
            "8": "1d2+1",
            "9": "1d2",
            "10": "1",
        },
    },
]
groups = [
    [],
    [],
    [],
    [],
]

#CR,NAME,SIZE,TYPE,ALIGNMENT,"LVL1","LVL2","LVL3","LVL4","LVL5","LVL6","LVL7","LVL8","LVL9","LVL10"
if __name__ == "__main__":
    rows = 0
    columns = 1
    column_max_rows = 16
    for level in enumerate(levels):
        print(f"\n### Level {level[0]+1}, Party of 4\n")
        for difficulty in difficulties:
            print(f"#### {difficulty}\n".title())
            print(f"| How Many | Challeng Rating |")
            print(f"|:---------------|:----- |")
            rows = rows + 1
            rows = rows + 1
            rows = rows + 1
            for cr in crs:
                try:
                    print(f"| &emsp;  {level[1][difficulty][cr]} | CR {cr} |")
                    rows = rows + 1
                except:
                    pass
            print(f"\n")
        if rows > column_max_rows:
            print(f"\column")
            rows = 0
            if columns == 2:
                print(f"\page")
                columns = 0
            else:
                columns = 2

    max_rows = 48
    rows_padding = 15
    for file in files:
        title = file.replace(".csv","")
        data = load_data(file)
        data = transform_data(data, "cr", crs)

        print(f"{{{{wide")
        print(f"### {title}".title())
        print(f"}}}}")
        print("| d100 | Monster |")
        print("|:------------------| :--- |")
        row_num = 0
        col_num = 1
        for group in data:
            num_rows = len(data[group])

            try:
                num_per_group = 100 / num_rows
            except:
                num_per_group = 0

            if num_per_group > 0:
                i = 1
                last = 0
                rows_remaining = max_rows - row_num
                if num_rows > rows_remaining:
                    if col_num == 2:
                        print(f"\page")
                        col_num = 1
                    else:
                        print(f"\column")
                        col_num = 2
                    print("| d100 | Monster |")
                    print(f"| **CR {group}** | |")
                    print("|:------------------| :--- |")
                    row_num = 1
                else:
                    print(f"| **CR {group}** | |")
                for row in data[group]:
                    row_num = row_num + 1
                    this = round(num_per_group + last)
                    print(f"| {i + last} - {this} | {row['name']} |")
                    last = this 
                    near_end = max_rows - row_num
                    if near_end > 2 and row_num % max_rows  == 0:
                        print(f"\column")
                        print("| d100 | Monster |")
                        print("|:------------------| :--- |")
        print(f"\page")
# 
# #### CR 1/8
# |d100 | Monster |
# |:------------------| :--- |
# | 1-12 | bandit               |
# | 13 - 24 | skeltion             |
# | 13 - 24 | skeltion             |
# | 13 - 24 | skeltion             |
# | 13 - 24 | skeltion             |
# | 13 - 24 | skeltion             |
# | 13 - 24 | skeltion             |
# | 13 - 24 | skeltion             |


# {'cr': '7', 'name': 'Oni', 'size': 'Large', 'type': 'Giant', 'alignment': 'lawful evil', 'lvl1': '0', 'lvl2': '0', 'lvl3': '0', 'lvl4': '0', 'lvl5': '0', 'lvl6': '1d2', 'lvl7': '', 'lvl8': '', 'lvl9': '', 'lvl10': ''},



#### Level 1
#| How Many | Challeng Rating |
#|:---------------|:----- |
#| **Easy** | |
#| &emsp; 1d4 | CR1 |
#| &emsp; 1d6 | CR2 |
#| **Hard** | |
#| &emsp; 1d8 | CR1 |
#| &emsp; 1d10. | CR2 |
#}}
#
