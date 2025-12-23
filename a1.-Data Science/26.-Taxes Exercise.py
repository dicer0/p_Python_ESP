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

        # BUY operation
        if operation == "buy":
            total_cost = unit_cost * quantity
            new_total_quantity = stock_quantity + quantity

            if new_total_quantity > 0:
                weighted_avg_price = (
                    (stock_quantity * weighted_avg_price) + total_cost
                ) / new_total_quantity

            stock_quantity = new_total_quantity
            taxes.append({"tax": 0.0})
            continue

        # SELL operation
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


def main():
    print(
        "Capital Gains Tax Calculator\n"
        "----------------------------------\n"
        "Please check the README.md file.\n"
        "Paste each test case (JSON array) manually in the console and compare the output with the expected results.\n"
        "Press ENTER on an empty line to finish.\n"
    )
    for line in iter(input, ""):
        line = line.strip()
        if not line:
            break

        operations = json.loads(line)
        result = process_operations(operations)
        print("result:")
        print(json.dumps(result), "\n")



if __name__ == "__main__":
    main()