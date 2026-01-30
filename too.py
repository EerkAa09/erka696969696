a = int(input("ehnii toogoo oruul"))
b = int(input("hoyrdoh toogoo oruul"))
uildel=input("temdegtee oruulnu(+, -, *, /)")
if uildel == "+":
    def nemekh(x, y):
        return x + y
    hariu = nemekh(a, b)
if uildel == "-":
    def hasah(x, y):
        return x - y
    hariu = hasah(a, b)
if uildel == "*":
    def urjih(x, y):
        return x * y
    hariu = urjih(a, b)
if uildel == "/":
    def huvaah(x, y):
        return x / y
    hariu = huvaah(a, b)


print(f"""
┌───────────────┐
│{hariu:^15}│
├───────────────┤
│ 7 │ 8 │ 9 │ + │
├───┼───┼───┼───┤
│ 4 │ 5 │ 6 │ - │
├───┼───┼───┼───┤
│ 1 │ 2 │ 3 │ * │
├───┼───┼───┼───┤
│ 0 │ . │ = │ / │
└───┴───┴───┴───┘
""")