# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

# Prices and production costs for each hot dog type
PRICES = {
    "Traditional": 5.00,
    "Veggie": 6.00,
    "Curry": 7.00,
    "BBQ": 10.00,
    "Spicy": 7.50
}

PRODUCTION_COSTS = {
    "Traditional": 2.00,
    "Veggie": 2.50,
    "Curry": 3.00,
    "BBQ": 4.10,
    "Spicy": 3.00
}

def calculate_profit(sales, hot_dog_type):
    """Calculate profit for each hot dog type."""
    price = PRICES[hot_dog_type]
    cost = PRODUCTION_COSTS[hot_dog_type]
    revenue = sales * price
    total_cost = sales * cost
    return revenue - total_cost

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sales', methods=['POST'])
def sales():
    # Get sales data from form
    sales_data = {
        'Traditional': int(request.form['traditional']),
        'Veggie': int(request.form['veggie']),
        'Curry': int(request.form['curry']),
        'BBQ': int(request.form['bbq']),
        'Spicy': int(request.form['spicy'])
    }

    total_sales = sum(sales_data.values())
    profits = {hot_dog: calculate_profit(sales, hot_dog) for hot_dog, sales in sales_data.items()}

    best_hot_dog = max(profits, key=profits.get)
    best_profit = profits[best_hot_dog]

    return render_template('result.html', sales_data=sales_data, total_sales=total_sales, profits=profits, best_hot_dog=best_hot_dog, best_profit=best_profit)

if __name__ == '__main__':
    app.run(debug=True)
