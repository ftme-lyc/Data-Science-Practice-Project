
def round_rate(rate):
    return round(rate, 4)
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    

def reverse_rate(rate):
    if rate != 0:
        return round(1/rate, 4)
    else:
        return 0
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    
def format_output(date, from_currency, to_currency, rate, amount, total_amount, inverse_rate):
    format_text = f"""The conversion rate on {date} from {from_currency} to {to_currency} was {rate}. 
                    So {amount} in {from_currency} correspond to {total_amount:.2f} in {to_currency}.
                    The inverse rate was {inverse_rate}."""
    return format_text

    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
   