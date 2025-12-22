# -*- coding: utf-8 -*-
import json


TAX_RATE = 0.20
TAX_FREE_LIMIT = 20000.0


def round_money(value):
    return round(value + 1e-9, 2)


def process_operations(operations):
    stock_quantity = 0
    weighted_avg_price = 0.0
    accumulated_loss = 0.0

    taxes = []

    for op in operations:
        operation = op["operation"]
        unit_cost = float(op["unit-cost"])
        quantity = int(op["quantity"])

        #BUY
        if operation == "buy":
            total_cost = unit_cost * quantity
            new_total_quantity = stock_quantity + quantity

            if new_total_quantity > 0:
                weighted_avg_price = (
                    (stock_quantity * weighted_avg_price) +
                    total_cost
                ) / new_total_quantity

            stock_quantity = new_total_quantity
            taxes.append({"tax": 0.0})
            continue

        #SELL
        total_amount = unit_cost * quantity
        profit = (unit_cost - weighted_avg_price) * quantity
        tax = 0.0

        if profit < 0:
            accumulated_loss += abs(profit)
        else:
            if total_amount > TAX_FREE_LIMIT:
                taxable_profit = profit - accumulated_loss

                if taxable_profit > 0:
                    tax = taxable_profit * TAX_RATE
                    accumulated_loss = 0.0
                else:
                    accumulated_loss -= profit

        stock_quantity -= quantity
        taxes.append({"tax": round_money(max(tax, 0.0))})

    return taxes


#TEST 9 OFFICIAL CASES:
TEST_CASES = [
    #Case 1
    (
        [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 100},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
        ],
        [{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}],
    ),

    #Case 2
    (
        [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
        ],
        [{"tax": 0.0}, {"tax": 10000.0}, {"tax": 0.0}],
    ),

    #Case 3
    (
        [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 5.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 3000},
        ],
        [{"tax": 0.0}, {"tax": 0.0}, {"tax": 1000.0}],
    ),

    #Case 4
    (
        [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "buy", "unit-cost": 25.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 10000},
        ],
        [{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}],
    ),

    #Case 5
    (
        [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "buy", "unit-cost": 25.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 25.00, "quantity": 5000},
        ],
        [{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 10000.0}],
    ),

    #Case 6
    (
        [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 2.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
            {"operation": "sell", "unit-cost": 25.00, "quantity": 1000},
        ],
        [{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 3000.0}],
    ),

    #Case 7
    (
        [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 2.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 2000},
            {"operation": "sell", "unit-cost": 25.00, "quantity": 1000},
            {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 5000},
            {"operation": "sell", "unit-cost": 30.00, "quantity": 4350},
            {"operation": "sell", "unit-cost": 30.00, "quantity": 650},
        ],
        [
            {"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0},
            {"tax": 3000.0}, {"tax": 0.0}, {"tax": 0.0},
            {"tax": 3700.0}, {"tax": 0.0}
        ],
    ),

    #Case 8
    (
        [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 50.00, "quantity": 10000},
            {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 50.00, "quantity": 10000},
        ],
        [{"tax": 0.0}, {"tax": 80000.0}, {"tax": 0.0}, {"tax": 60000.0}],
    ),

    #Case 9
    (
        [
            {"operation": "buy", "unit-cost": 5000.00, "quantity": 10},
            {"operation": "sell", "unit-cost": 4000.00, "quantity": 5},
            {"operation": "buy", "unit-cost": 15000.00, "quantity": 5},
            {"operation": "buy", "unit-cost": 4000.00, "quantity": 2},
            {"operation": "buy", "unit-cost": 23000.00, "quantity": 2},
            {"operation": "sell", "unit-cost": 20000.00, "quantity": 1},
            {"operation": "sell", "unit-cost": 12000.00, "quantity": 10},
            {"operation": "sell", "unit-cost": 15000.00, "quantity": 3},
        ],
        [
            {"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0},
            {"tax": 0.0}, {"tax": 0.0}, {"tax": 1000.0}, {"tax": 2400.0}
        ],
    ),
]


#TEST RUNNER
def main():
    print("Running Capital Gains validation (9 official cases):")

    for i, (operations, expected) in enumerate(TEST_CASES, start=1):
        result = process_operations(operations)
        status = "PASS" if result == expected else "FAIL"

        print(f"Case #{i}: {status}")
        print("Expected:", json.dumps(expected))
        print("Got     :", json.dumps(result))
        print("-" * 60)


if __name__ == "__main__":
    main()