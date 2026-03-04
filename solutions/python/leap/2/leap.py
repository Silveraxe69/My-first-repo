"""Determine if a year is a leap year."""

def leap_year(year):
    """Check if given year is a leap year.
    
    :param year: int - the year to check
    :return: bool - True if leap year, False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
