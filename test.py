penz = 5
hp=345
def asd(penz, hp):
    penzstr= f"h{hp}"
    return penzstr

penzstr= asd(penz, hp)
if "p" in penzstr:
    string = penzstr.removeprefix("p")
    print(f"Pénz: {string}")
elif "h" in penzstr:
    string = penzstr.removeprefix("h")
    print(f"Életerő: {string}")
elif "e" in penzstr:
    string = penzstr.removeprefix("e")
    print(f"Energia: {string}")

