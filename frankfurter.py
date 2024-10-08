from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    url = f"{BASE_URL}/currencies"
    status_code, content = get_url(url)

    if status_code == 200:
        currencies = json.loads(content)
        return list(currencies.keys())
    else:
        return None
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """
    

def get_latest_rates(from_currency, to_currency, amount):
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}"
    status_code, content = get_url(url)

    if status_code == 200:
        data = json.loads(content)
        rate = data["rates"][to_currency]
        date = data["date"]
        return date, rate
    else:
        None, None
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    

def get_historical_rate(from_currency, to_currency, from_date, amount):
    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}"
    status_code, content = get_url(url)

    if status_code == 200:
        data = json.loads(content)
        conversion_rate = data.get("rates",{}).get(to_currency)
        return conversion_rate
    else:
        None

    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """
    

