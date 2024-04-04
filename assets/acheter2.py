from ib_insync import *
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import datetime
import sys

ticker = sys.argv[1]
target2 = sys.argv[2]
target2 = float(target2)

target = sys.argv[3]
target = float(target2)



ib = IB()
ib.connect('127.0.0.1', 7497, clientId=2)

# Créer un contrat pour l'action Tesla
contract = Stock(ticker, "SMART", "USD")

market_data = ib.reqMktData(contract)
ib.sleep(1)  # Pause pour s'assurer que les données sont reçues
price = market_data.last

# Calculer le nombre d'actions à acheter
amount_to_spend = 200  # Le montant en dollars que vous voulez dépenser
quantity = amount_to_spend // price  # Utilisez la division entière pour obtenir un entier


# Créer un ordre d'achat avec quantité d'action
order = MarketOrder("BUY", quantity)

# Placer l'ordre pour le compte spécifique
trade = ib.placeOrder(contract, order)
ib.sleep(1)

# Créer un ordre Stop Loss
stop_loss_price = target
stop_loss_order = StopOrder("SELL", quantity, stop_loss_price)
ib.placeOrder(contract, stop_loss_order)

# Créer un ordre Take Profit
take_profit_price = target2
take_profit_order = LimitOrder("SELL", quantity, take_profit_price)
ib.placeOrder(contract, take_profit_order)

# Obtenir le portefeuille
portfolio = ib.portfolio()
print(portfolio)

# Obtenir le portefeuille
portfolio = ib.portfolio()
print(portfolio)

# Se déconnecter de TWS
ib.disconnect()
