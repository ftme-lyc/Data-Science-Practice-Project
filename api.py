import requests

def get_url(url: str):
    try:
        resp = requests.get(url)
        status_code = resp.status_code
        content = resp.text
        return status_code, content
    except:
        return resp.exceptions.RequestException
    """
    Function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """

