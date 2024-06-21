def calculate_profit(
        amount: int, percent: float | int, period: int) -> int:
    return (amount * ((1 + (percent / 100))) ** period)


print(calculate_profit(10000, 10, 3))
