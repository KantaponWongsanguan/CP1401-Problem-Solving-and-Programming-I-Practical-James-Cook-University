NAME_TO_HEX = {"BROWN1": "#ff4040", "BROWN2": "#ee3b3b", "BROWN3": "#cd3333",
               "BROWN4": "#8b2323", "BLUE1": "#0000ff", "BLUE2": "#0000ee",
               "BLUE4": "#00008b", "BLACK": "#000000", "BLOND": "#faf0be",
               "AQUA": "#00ffff"}
print(NAME_TO_HEX)
print("Enter blank to quit")

colour_name = input("Enter colour name from the dictionary: ").upper()
while colour_name != '':
    try:
        print(f"{colour_name},'s hex code is, {NAME_TO_HEX[colour_name]}")
    except KeyError:
        print("This colour name does not exist in our Dictionary")
    colour_name = input("Enter colour name from the dictionary: ").upper()

print("Farewell")
