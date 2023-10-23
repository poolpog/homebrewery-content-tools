from jinja2 import Environment, FileSystemLoader
import wandering_monsters_tables.render

outfile = "homebrewery-endless-dungeon.md"
environment = Environment(loader=FileSystemLoader("./"))
template = environment.get_template(f"{outfile}.j2")

w = wandering_monsters_tables.render
wmt = w.render()

#with open(outfile, mode="w", encoding="utf-8") as message:
#    message.write(content)
#    print(f"... wrote {outfile}")

