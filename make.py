from jinja2 import Environment, FileSystemLoader
from .wandering-monster-tables import render

outfile = "homebrewery-endless-dungeon.md"
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template(f"{outfile}.j2")

#with open(outfile, mode="w", encoding="utf-8") as message:
#    message.write(content)
#    print(f"... wrote {outfile}")

w = wandering-monster-tables.render()
print(w)
