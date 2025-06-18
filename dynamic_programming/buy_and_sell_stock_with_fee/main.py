from .algo import max_profit


def main():
    profit = max_profit([1, 3, 2, 8, 4, 9], 2)
    print(f"Profit: {profit}")


if __name__ == "__main__":
    main()
