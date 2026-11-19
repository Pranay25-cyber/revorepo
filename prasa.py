def process_orders(orders):
    results = []
    total = 0
    for order in orders:
        price = order.get("price")
        quantity = order.get("quantity")
        if price is None or quantity is None or price < 0 or quantity == 0:
            continue
        discount = order.get("discount", 0.1)
        final_price = price * quantity * (1 - discount)
        total += final_price
        results.append({"id": order.get("id"), "amount": final_price})
    if len(results) > 0:
        average = total / len(results)
    else:
        average = 0
    results.sort(key=lambda x: x["amount"], reverse=True)
    return {"results": results, "average": average, "total": total}
