# Building Currency Converter in Python

## Author
Name: Fatemeh Elyasifar
Student ID: 25589351

## Description
The Currency Converter is a Python web application that displays the current exchange rate between two currency codes for the latest date or a selected past date. Additionally, it calculates the inverse exchange rate between the two currencies.
Key features include:
- A number input field where users can enter the amount they wish to convert
- Two dropdown menus displaying all available currencies from Frankfurter
- A button to switch the selected currencies
- A button to fetch the latest conversion rate for the chosen currencies
- Two text boxes providing details of the conversion along with the inverse rate
- A date picker that lets users select a historical date

### Challenges
- Ensuring proper handling of invalid inputs, such as incorrect currency codes or dates
- Connecting to external APIs and managing their responses effectively
- Presenting conversion results in a clear format
- Handling conversion rates for past dates

### Future Features
- Adding user authentication to save previous conversions
- Expanding the list of available currencies for conversion
- Comparing the current exchange rate with rates from a past date
- Visualising the comparison between the current exchange rate and past rates
- Analysing exchange rate trends across different currencies

## How to Setup
Step 1: Install Python 3.12.4
1. Download Python: Visit the Python downloads page and select Python 3.12.4.
2. Install Python: Follow the installation instructions for your operating system.

Step 2: Install Required Packages
1. Install Streamlit 1.38.0: Pip install streamlit==1.38.0
2. Install Requests 2.32.3: Pip install Requests==2.32.3
3. Datetime is part of the standard library, so no additional installation is needed.

Step 3: Create a Streamlit Application
1. Create a file named app.py
2. Write a sample code in app.py
3. Run the code to ensure the setup is complete

Step 4: Run the Application In Terminal
1. Start the Streamlit app: streamlit run app.py
2. Open the provided URL, usually http://localhost:8501, in the web browser.

## How to Run the Program
### Instruction
1. Navigate to the project folder
2. Install Streamlit in the environment
3. Run the Streamlit application

### Example
First, open the terminal and navigate to the folder where your Streamlit application is located by using the command: cd C:\Users\YourUsername\Documents\my_streamlit_app. If you haven’t installed Streamlit yet, install it with: pip install streamlit. After installation, you can run the application by executing: streamlit run app.py. Streamlit will start a local server and provide a URL (usually http://localhost:8501). Open this URL in your web browser to see your web application in action.

## Project Structure
1. **api.py**:
`get_url(url)`: This function takes a URL as input and sends a GET request to that URL using the requests library to fetch data. If the request is successful, it returns a tuple with two values: "status_code" (the HTTP status code of the response) and "content" (the content of the HTTP response as a string). If an error occurs during the GET request, such as an invalid URL, it catches the requests.exceptions.RequestException and handles it by printing an error message.

2. **app.py**:
This file displays the app title and retrieves the list of available currencies from Frankfurter. If the list of currencies is None, it displays an error message in the Streamlit app. Otherwise, it sets default values for two dropdown menus. It also includes input fields for entering the amount and selecting the "from" and "to" currencies. A button labeled "Switch Currencies" swaps the selected currencies, while the "Get Latest Rate" button fetches and displays the latest conversion rate for the chosen currencies and amount. Additionally, a date picker and "Get Historical Rate" button allow users to retrieve and display historical rates for a selected date, currencies, and amount.

3. **frankfurter.py**:
It includes following functions:
    - `get_currencies_list()`: This function fetches a list of available currencies from the Frankfurter API. It sends a GET request to the API endpoint URL, retrieves the response, and parses it as JSON. If the HTTP status code is 200 (indicating a successful request), it returns a list of currency codes extracted from the JSON response. Otherwise, it returns None.
    - `get_latest_rates(from_currency, to_currency, amount)`: This function retrieves the latest exchange rate between two currencies. It takes the source and target currency codes along with the amount to be converted. It constructs a URL with these parameters and sends a GET request to the API endpoint URL. If the API call is successful, it extracts the latest conversion rate and date, returning them as two separate objects. If the request fails, it returns None for both values.
    - `get_historical_rate(from_currency, to_currency, from_date, amount)`: This function retrieves the historical exchange rate between two currencies on a specified date. It takes four parameters: the source currency code, target currency code, historical date, and amount in the source currency to convert. It constructs a URL with these parameters and sends a GET request to the API endpoint for the specified date. If the request is successful, it extracts the exchange rate from the JSON response and returns it. If the request fails, it returns None.

4. **currency.py**:
It includes following functions:
    - `round_rate(rate)`: This function rounds an input float to four decimal places.
    - `reverse_rate(rate)`: This function calculates the inverse rate from the given input rate. If the rate is not equal to zero, it computes the inverse rate and rounds it to four decimal places. If the rate is zero, it returns 0.
    - `format_output(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate)`: This function formats a text output containing conversion information and details. It takes several parameters, including date (the conversion date), from_currency (the source currency code), to_currency (the target currency code), rate (the conversion rate), amount (the original amount), converted_amount (the amount after conversion), and inverse_rate (the inverse conversion rate).

## Citations
- https://docs.streamlit.io/library
- https://frankfurter.app/docs