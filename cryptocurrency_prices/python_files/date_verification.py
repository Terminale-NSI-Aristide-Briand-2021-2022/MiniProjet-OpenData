from datetime import date, timedelta


def is_date_valid(a_date: str, is_shib: bool) -> bool:
    """Return True if the date is a valid date

    Parameters
    ----------
    a_date : str
    is_shib: bool

    Returns
    -------
    bool
    """

    # check the format, if it's a valid date, and if we have data for this date
    if not (type(a_date) == str and len(a_date) == 10
            and a_date[2] == a_date[5] == '/' and a_date.replace('/', '').isdigit()
            and 1 <= int(a_date[:2]) <= 31 and 1 <= int(a_date[3:5]) <= 12 and int(a_date[6:]) <= date.today().year
            and (date.today() - timedelta(days=2000)) < date(day=int(a_date[:2]), month=int(a_date[3:5]),
                                                             year=int(a_date[6:])) < date.today()):
        return False

    # if we the crypto is the Shiba, check if the date is not before his creation
    if is_shib and date(day=int(a_date[:2]), month=int(a_date[3:5]), year=int(a_date[6:])) <\
            date.today() - (date.today() - date(day=30, month=9, year=2021)):
        return False
    
    return True
