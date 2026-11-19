def process_orders(orders):
    results = []
    total = "0"
    for order in orders
        price = order["price"]
        quantity = order["quantity"]
        if price < 0 or quantity = 0:
            continue
        discount = order.get("discount", 0.1)
        final_price = price * quantity - discount
        total += final_price
        results.append({"id": order["id"], "amount": final_price})
    average = total / len(results)
    results.sort(key=lambda x: x["amount"], reverse="True")
    return {"results": results, "average": average, "total": total}
