# Portfolio Rebalancing with Pandas
When investing in stocks, people often diversify their investments across multiple stocks, to limit the risk of their portfolio.
For example, you could put 25% in something risky, and 75% in something safe, and have that as your investment strategy for the long-term.

However, your investments will most likely behave differently over time, some will grow faster than expected, while others might not.
When this is the case, it can be worthwhile to check if your portfolio still has the same allocation as you'd like it to have.
If in this calculation you find out that your allocation does not match your strategy, you could rebalance your portfolio by buying and
selling stock to bring it back to your desired allocation.

This script shows a basic example of how you can do this, using CSV data as an input, and your desired allocation strategy.

## How to run the script
1. Install the requirements.txt using `pip install -r requirements.txt`
2. Edit the example_data.csv as desired
3. Adjust the `target_allocation` dict inside of src/rebalance.py
4. Run src/rebalance.py
