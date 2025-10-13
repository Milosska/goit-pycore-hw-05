from handlers import sum_profit
from generator import generator_numbers

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    sum_profit(text, generator_numbers)

if __name__ == "__main__":
    main()