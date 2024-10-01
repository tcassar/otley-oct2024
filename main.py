"""
Pairing Constraints
---

- Weightlifting can only be assigned to boys
- No pairs can be the same as last year

"""
import random

boys = {
    "Marco",
    "Joe",
    "Thumb",
    "Cass",
    "Guano",
    "Kez",
    "Monty",
    "Sebba",
    "Felix",
    "Louis",
    "Elot",
    "Josh",
}

girls = {
    "Tilly",
    "Farrer",
    "Harris",
    "McKillop",
    "Immy",
    "Bea",
    "Cos",
    "Alick",
}

sports = [
    "Swimming",
    "Skiing",
    "Tennis",
    "Rugby",
    "Boxing",
    "Golf",
    "Fishing",
    "Hockey",
    "Cycling",
    "Weightlifting",
]

previous_pairs = [
    ("Tilly", "Kez"),
    ("Bea", "Elot"),

    # Alice, Monty, Guano were a three
    ("Alice", "Monty"),
    ("Alice", "Guano"),
    ("Monty", "Guano"),

    # Felix, Farrer, Max were a three
    ("Felix", "Farrer"),
]

folk = list(boys.union(girls))


def assign_pairs() -> list[tuple[str, str]]:
    """Assign pairs for this year at random"""
    pairs = []
    three_needed = len(folk) % 2

    random.shuffle(folk)

    first_split, second_split = folk[:len(folk)//2], folk[len(folk)//2:]

    for p1, p2 in zip(first_split, second_split):
        pairs.append((p1, p2))

    if three_needed:
        pairs[-1] = (pairs[-1][0], pairs[-1][1], second_split[-1])

    return pairs


def main():
    while True:
        out = ""
        pairs = assign_pairs()
        boy_pairs = 0

        for (p1, p2), sport in zip(pairs, sports):
            if (p1, p2) in previous_pairs or (p2, p1) in previous_pairs:
                break

            if sport == "Weightlifting" and p1 in girls or p2 in girls:
                break

            if p1 in boys and p2 in boys:
                boy_pairs += 1

                if boy_pairs > 3:
                    break

            out += f"{p1:<15}{p2:<15}{sport:<15}\n"
        else:
            print(out[:-1])
            break


if __name__ == "__main__":
    print("=" * 46)
    print(f"{'OTLEY RUN 2024':^45}")
    print("- " * 23)
    main()
    print("=" * 46)
