def create_deck():
    values = list(range(1, 14));
    suits = ["S", "H", "D", "C"]
    deck = []

    for suit in suits:
        for value in values:
            deck.append((suit, value))

create_deck()
