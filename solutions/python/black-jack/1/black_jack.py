def value_of_card(card):
    if card in 'JQK':
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    if v1 > v2:
        return card_one
    if v2 > v1:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    if 'A' in (card_one, card_two):
        return 1
    return 11 if total + 11 <= 21 else 1


def is_blackjack(card_one, card_two):
    return sorted([value_of_card(card_one), value_of_card(card_two)]) == [1, 10]


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total <= 11
