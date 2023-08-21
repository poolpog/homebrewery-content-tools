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
                    "cr": row[0],
                    "name": row[1],
                    "size": row[2],
                    "type": row[3],
                    "alignment": row[4],
                    "lvl1": row[5],
                    "lvl2": row[6],
                    "lvl3": row[7],
                    "lvl4": row[8],
                    "lvl5": row[9],
                    "lvl6": row[10],
                    "lvl7": "",
                    "lvl8": "",
                    "lvl9": "",
                    "lvl10": "",
            })
        return output

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

#CR,NAME,SIZE,TYPE,ALIGNMENT,"LVL1","LVL2","LVL3","LVL4","LVL5","LVL6","LVL7","LVL8","LVL9","LVL10",ROLLS, variables,4,60
if __name__ == "__main__":
    for file in files:
        print(f"== {file} ==")
        groups = [
            [],
            [],
            [],
            [],
        ]
        levels = [
            #easy        medium       hard        deadly
            #lvl1
            [{
                "easy":[
                        ["1/8","1d4"],
                        ["1/4","1d3"]
                        ["1/2","1"],
                    ],
                "medium":[
                        ["1/8","1d6"],
                        ["1/4","1d4"]
                        ["1/2","1d2"],
                    ],
                "hard":[
                        ["1/8","2d4"],
                        ["1/4","1d6"]
                        ["1/2","1d2"],
                        ["1","1"],
                    ],
                "deadly":[
                        ["1/8","2d6"],
                        ["1/4","2d4"]
                        ["1/2","1d4"],
                        ["1","1d2"],
                    ],
                }
            ],
            #lvl2
            [{
                "easy":[
                        ["1/8","1d8"],
                        ["1/4","1d6"]
                        ["1/2","1d4"],
                        ["1","1"],
                    ],
                "medium":[
                        ["1/8","2d4"],
                        ["1/4","1d6"]
                        ["1/2","1d4"],
                        ["1","1d2"],
                        ["2","1"],
                    ],
                "hard":[
                        ["1/4","2d4"]
                        ["1/2","1d6"],
                        ["1","1d2"],
                        ["2","1d2"],
                        ["3","1"],
                    ],
                "deadly":[
                        ["1/4","2d6"]
                        ["1/2","1d8"],
                        ["1","1d4"],
                        ["2","1d2"],
                        ["3","1"],
                        ["4","1"],
                    ],
                }
            ],
            #lvl3
            [{
                "easy":[
                        ["1/8","2d4"],
                        ["1/4","1d6"]
                        ["1/2","1d4"],
                        ["1","1d2"],
                        ["2","1"],
                        ["3","0"],
                        ["4","0"],
                    ],
                "medium":[
                        ["1/4","2d4"]
                        ["1/2","1d4+1"],
                        ["1","1d2+1"],
                        ["2","1d2"],
                        ["3","1"],
                        ["4","0"],
                    ],
                "hard":[
                        ["1/4","2d6+2"]
                        ["1/2","1d6+2"],
                        ["1","1d4"],
                        ["2","1d2"],
                        ["3","1d2"],
                        ["4","1"],
                    ],
                "deadly":[
                        ["1/2","2d4+2"],
                        ["1","1d6+1"],
                        ["2","1d4"],
                        ["3","1d2"],
                        ["4","1d2"],
                        ["5","1"],
                    ],
                }
            ],
            #lvl4
            [{
                "easy":[
                        ["1/4","3d4"],
                        ["1/2","1d4+2"],
                        ["1","1d4"],
                        ["2","1d2"],
                        ["3","1"],
                        ["4","0"],
                        ["5","0"],
                        ["6","0"],
                        ["7","0"],
                    ],
                "medium":[
                        ["1/2","2d4"],
                        ["1","1d4"],
                        ["2","1d2"],
                        ["3","1d2"],
                        ["4","1"],
                        ["5","0"],
                        ["6","0"],
                        ["7","0"],
                    ],
                "hard":[
                        ["1/2","1d6+2"],
                        ["1","1d4+1"],
                        ["2","1d4"],
                        ["3","1d2"],
                        ["4","1d2"],
                        ["5","1"],
                        ["6","0"],
                        ["7","0"],
                    ],
                "deadly":[
                        ["1","1d8+2"],
                        ["2","1d4+2"],
                        ["3","1d4"],
                        ["4","1d2"],
                        ["5","1d2"],
                        ["6","1"],
                        ["7","1"],
                    ],
                }
            ],
            #lvl5
            [{
                "easy":[
                        ["1","1d4+2"],
                        ["2","1d4"],
                        ["3","1d2"],
                        ["4","1"],
                        ["5","1"],
                        ["6","0"],
                        ["7","0"],
                    ],
                "medium":[
                        ["1","1d6+1"],
                        ["2","1d4"],
                        ["3","1d4"],
                        ["4","1d2"],
                        ["5","1"],
                        ["6","1"],
                        ["7","1"],
                    ],
                "hard":[
                        ["2","1d4+1"],
                        ["3","1d4+1"],
                        ["4","1d4"],
                        ["5","1d2"],
                        ["6","1d2"],
                        ["7","1d2"],
                        ["8","1"],
                    ],
                "deadly":[
                        ["2","1d4+3"],
                        ["3","1d4+2"],
                        ["4","1d4"],
                        ["5","1d2"],
                        ["6","1d2"],
                        ["7","1d2"],
                        ["8","1d2"],
                        ["9","1"],
                    ],
                }
            ],
            #lvl6
            [{
                "easy":[
                    ],
                "medium":[
                    ],
                "hard":[
                    ],
                "deadly":[
                    ],
                }
            ],
        ]
        data = load_data(file)
        for x in range(4):
            for row in data:
                for level in levels:
                    if row["cr"] in level[x]["cr"]:
                        groups[x].append(row)
            print("\n".join([str(x) for x in groups[x]]))

