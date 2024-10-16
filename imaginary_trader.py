import time
import random
import threading

class ImaginaryTrader:
    def __init__(self, initial_capital):
        self.capital = initial_capital
        self.portfolio = {}
        self.is_running = False

    def start_trading(self):
        self.is_running = True
        print("Starte imaginären Handel...")
        while self.is_running:
            self.simulate_trade()
            time.sleep(5)  # Wartezeit zwischen Trades

    def stop_trading(self):
        self.is_running = False
        print("Beende imaginären Handel...")

    def simulate_trade(self):
        # Simuliert einen Trade
        symbol = random.choice(['AAPL', 'GOOGL', 'TSLA', 'AMZN'])
        price = random.uniform(100, 500)
        quantity = random.randint(1, 10)
        trade_value = price * quantity

        if self.capital >= trade_value:
            self.capital -= trade_value
            self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
            print(f"Gekauft: {quantity} Aktien von {symbol} zu {price:.2f} USD")
        else:
            print("Nicht genügend Kapital für den Kauf.")

        # Simuliert einen zufälligen Gewinn/Verlust
        unrealized_pnl = random.uniform(-0.05, 0.05) * trade_value
        self.capital += unrealized_pnl
        print(f"Unrealisierter P&L: {unrealized_pnl:.2f} USD, Kapital: {self.capital:.2f} USD")
