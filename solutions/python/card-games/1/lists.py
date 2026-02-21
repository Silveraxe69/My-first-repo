def get_rounds(number):
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    true_avg = sum(hand) / len(hand)
    if len(hand) == 0:
        return False
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle = hand[len(hand) // 2]
    return first_last_avg == true_avg or middle == true_avg


def average_even_is_average_odd(hand):
    if len(hand) < 2:
        return True
    even_sum = sum(hand[i] for i in range(0, len(hand), 2))
    odd_sum = sum(hand[i] for i in range(1, len(hand), 2))
    even_avg = even_sum / ((len(hand) + 1) // 2)
    odd_avg = odd_sum / (len(hand) // 2)
    return even_avg == odd_avg


def maybe_double_last(hand):
    if hand and hand[-1] == 11:
        hand[-1] *= 2
    return hand
