import threading
import time
from imaginary_trader import ImaginaryTrader
from demo_trader import DemoTrader

def main():
    mode = input("Wähle den Modus (1 für Imaginär, 2 für Demo): ")

    if mode == '1':
        trader = ImaginaryTrader(initial_capital=10000)
    elif mode == '2':
        trader = DemoTrader()
    else:
        print("Ungültige Auswahl.")
        return

    # Startet den Trader in einem separaten Thread
    trader_thread = threading.Thread(target=trader.start_trading)
    trader_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        trader.stop_trading()
        trader_thread.join()

if __name__ == "__main__":
    main()
