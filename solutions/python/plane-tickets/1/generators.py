def generate_seat_letters(number):
    for i in range(number):
        yield chr(65 + (i % 4))

def generate_seats(number):
    seat_count = 0
    row = 1
    while seat_count < number:
        if row == 13:
            row += 1
            continue
        for letter in 'ABCD':
            if seat_count >= number:
                return
            yield f"{row}{letter}"
            seat_count += 1
        row += 1

def assign_seats(passengers):
    seats = generate_seats(len(passengers))
    return {passenger: next(seats) for passenger in passengers}

def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        code = seat + flight_id
        yield code + '0' * (12 - len(code))

