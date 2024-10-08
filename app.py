import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title("FX Converter")
# Get the list of available currencies from Frankfurter
currencies = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if currencies is None:
    st.error("Unable to fetch currency list.")
else:
    if 'from_currency' not in st.session_state:
        st.session_state.from_currency = get_currencies_list()[0]  # Default to first currency
    if 'to_currency' not in st.session_state:
        st.session_state.to_currency = get_currencies_list()[1]  # Default to second currency

# Add input fields for capturing amount, from and to currencies
amount = st.number_input("Enter the amount to be converted:")

if st.button('Switch Currencies'):
    # Swap the currencies in session state
    st.session_state.from_currency, st.session_state.to_currency = st.session_state.to_currency, st.session_state.from_currency

from_currency = st.selectbox('From currency:',currencies,key='from_currency')
to_currency = st.selectbox('To currency:',currencies,key='to_currency')

# Add a button to get and display the latest rate for selected currencies and amount
if st.button('Get Latest Rate'):
    latest_rates = get_latest_rates(from_currency, to_currency, amount)
    if latest_rates:
        date, rate = latest_rates
        rate = round_rate(rate)
        inverse_rate = reverse_rate(rate)
        total_amount = amount*rate
        text = format_output(date, from_currency, to_currency, rate, amount, total_amount, inverse_rate)
        st.markdown(f"<p style='color: green;'>{text}</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: red;'>Error fetching conversion rate</p>", unsafe_allow_html=True)

# Add a date selector (calendar)
target_date = st.date_input("Select a date for historical rates", datetime.date.today(),max_value=datetime.date.today())

# Add a button to get and display the historical rate for selected date, currencies and amount
if st.button('Get Historical Rate'):
    historical_rate = get_historical_rate(from_currency, to_currency, target_date, amount)
    if historical_rate:
        conversion_rate = round_rate(historical_rate)
        inverse_rate = reverse_rate(conversion_rate)
        total_amount = amount*conversion_rate
        text = format_output(target_date, from_currency, to_currency, conversion_rate, amount, total_amount, inverse_rate)
        st.markdown(f"<p style='color: green;'>{text}</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: red;'>Error fetching historical rate</p>", unsafe_allow_html=True)










