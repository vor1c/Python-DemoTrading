import time
import threading
import alpaca_trade_api as tradeapi

class DemoTrader:
    def __init__(self):
        self.api = tradeapi.REST(
            'PKN7GZE4SD9WMHB6F53P',  # Füge hier deinen API-Schlüssel ein
            'hTljqJ2gRvlGRXFIIodZyB5zeKEqPd20W3s7FfrC',  # Füge hier deinen Geheimschlüssel ein
            'https://paper-api.alpaca.markets'
        )
        self.is_running = False

    def start_trading(self):
        self.is_running = True
        print("Starte Demo-Handel...")
        while self.is_running:
            self.execute_trade()
            time.sleep(5)  # Wartezeit zwischen Trades

    def stop_trading(self):
        self.is_running = False
        print("Beende Demo-Handel...")

    def execute_trade(self):
        symbol = 'AAPL'
        qty = 1

        try:
            order = self.api.submit_order(
                symbol=symbol,
                qty=qty,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            print(f"Order ausgeführt: Gekauft {qty} Aktien von {symbol}")
        except Exception as e:
            print(f"Fehler beim Ausführen der Order: {e}")
