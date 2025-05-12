# Prime Numbers Sliding Window Average

This repo is a simple Python script for afford med exam that connects to an external API to fetch **numbers**, maintains a **sliding window** of the latest unique numbers, and calculates their **average**.

## What It Does

- Fetches a list of prime numbers from a remote API using an access token.
- Maintains a sliding window (`window_range = 10`) of the most recent unique numbers.
- Ensures the numbers in the window are always unique and within the specified size limit.
- Calculates the average of numbers in the current window.
- Displays:
  - The previous state of the window
  - The current state after new numbers are added
  - The new numbers fetched from the API
  - The average of the current window

## How I Implemented It

- Used the `requests` library to make authenticated API calls using a bearer token.
- Used a global list (`window_current`) to store the current window of numbers.
- Created a `filter_nums()` function to deduplicate incoming numbers and enforce the window size limit.
- Wrote `calculate_avg()` to compute the average of the current window.
- Continuously prompt the user for input to fetch and process new numbers in a loop.
- Displayed all relevant information in a clear format using `print()`.

This was built as a basic interactive console application to demonstrate working with APIs, managing state, and performing calculations.
