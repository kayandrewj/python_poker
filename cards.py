DISPLAY_VALUES = {
1: "A",
13: "K",
12: "Q",
11: "J",
2: "2",
3: "3",
4: "4",
5: "5",
6: "6",
7: "7",
8: "8",
9: "9",
10: "10"
}
def create_deck():
    values = list(range(1, 14));
    suits = ["S", "H", "D", "C"]
    deck = []

    for suit in suits:
        for value in values:
            deck.append((suit, value))

    row = "|      |"
    top = "________"
    bottom = "--------"
    for card in deck:
        disp_val = DISPLAY_VALUES[card[1]]
        data_row = "|{0}    {1}|".format(card[0], disp_val)
        print(top)
        print(data_row)
        print(row)
        print(row)
        print(data_row)
        print(bottom)
        print(" ")
create_deck()
