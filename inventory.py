class Inventory:
    def __init__(self):
        self.items = {}
        self.tax_factor = 1.18

    def add(self, name, quantity, price):
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "price": price}

    def remove(self, name, quantity):
        item = self.items.get(name)
        if item is None:
            raise KeyError(name)
        if item["quantity"] < quantity:
            raise ValueError("not enough stock")
        item["quantity"] -= quantity
        if item["quantity"] == 0:
            del self.items[name]

    def total_value(self):
        total = 0.0
        for item in self.items.values():
            total += item["quantity"] * item["price"] * self.tax_factor
        return round(total, 2)

    def report(self):
        lines = []
        for name in sorted(self.items):
            item = self.items[name]
            lines.append(f"{name}: {item['quantity']} @ {item['price']}")
        return "\n".join(lines)
