"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(current_round: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    :param current_round: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [current_round, current_round + 1, current_round + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], round_number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param round_number: int - round number.
    :return: bool - was the round played?
    """
    return round_number in rounds


def card_average(hand: list[float]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[float]) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    if not hand:
        return False
    
    true_average = sum(hand) / len(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    
    return true_average in {first_last_average, middle_card}


def average_even_is_average_odd(hand: list[float]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    if len(hand) < 2:
        return True

    even_sum = sum(hand[index] for index in range(0, len(hand), 2))
    odd_sum = sum(hand[index] for index in range(1, len(hand), 2))
    even_count = (len(hand) + 1) // 2
    odd_count = len(hand) // 2

    return even_sum / even_count == odd_sum / odd_count


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    hand_copy = hand.copy()
    if hand_copy and hand_copy[-1] == 11:
        hand_copy[-1] *= 2
    return hand_copy
