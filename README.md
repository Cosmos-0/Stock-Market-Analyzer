# Stock Market Analyzer

## Overview

**Stock Market Analyzer** is a web application that allows users to analyze historical stock data and visualize technical indicators such as Simple Moving Average (SMA), Exponential Moving Average (EMA), Bollinger Bands, and Relative Strength Index (RSI). The app fetches data from Yahoo Finance using the `yfinance` library and presents interactive charts using Streamlit and Plotly.

## Features

- **Historical Stock Data Visualization**: View historical stock prices for any ticker symbol from Yahoo Finance.
- **Technical Indicators**:
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
  - Bollinger Bands
  - Relative Strength Index (RSI)
- **Interactive User Interface**: Select stock tickers, date ranges, and indicators to visualize with an intuitive sidebar.
- **Customizable Date Range**: Choose the start and end dates for the data analysis.

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: Framework for building the web application
- **yfinance**: Python library to fetch financial data from Yahoo Finance
- **pandas**: Data manipulation and analysis library
- **Plotly**: Library for creating interactive plots and visualizations

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/stock-market-analyzer.git
   cd stock-market-analyzer
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   Create a `requirements.txt` file with the following content:

   ```text
   streamlit
   yfinance
   pandas
   plotly
   ```

## Usage

1. **Run the Streamlit app**:

   ```bash
   streamlit run market_analysis.py
   ```

2. **Open the web browser**:

   The app will automatically open in your default web browser. If it does not, open [http://localhost:8501](http://localhost:8501) manually.

3. **Enter the stock ticker and select the desired options**:

   - Input the stock ticker symbol (e.g., `AAPL` for Apple Inc.).
   - Select the date range.
   - Choose the technical indicators to visualize.

## Screenshots

Add some screenshots of your app here to showcase the UI and functionality.

## Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and use a feature branch. Pull requests are encouraged.

1. **Fork the project**.
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`).
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`).
4. **Push to the branch** (`git push origin feature/AmazingFeature`).
5. **Open a Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [LinkedIn Profile](https://www.linkedin.com/in/yourusername)

Project Link: [https://github.com/yourusername/stock-market-analyzer](https://github.com/yourusername/stock-market-analyzer)

---

This README provides a comprehensive overview of your **Stock Market Analyzer** app and can be further customized based on your specific needs and preferences.
