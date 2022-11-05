hi: dict[str, int] = {"a": 1, "b": 2}
for thing in hi:
    print(thing)

# howdy: list[int] = [1, 2, 3]
hi["c"] = 4
print(hi)

hi.pop("c")
print(hi)