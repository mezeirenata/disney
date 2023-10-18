penz = 5
hp=345
def asd(penz, hp):
    penzstr= f"h{hp}"
    return penzstr

penzstr= asd(penz, hp)
if "p" in penzstr:
    string = penzstr.removeprefix("p")
    print(f"Penz: {string}")
elif "h" in penzstr:
    string = penzstr.removeprefix("h")
    print(f"hp: {string}")

