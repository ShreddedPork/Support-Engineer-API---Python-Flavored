import shippo
import config
from sys import argv


shippo.config.api_key = config.access_token


def retrieve_rates(shipmentId):
    rates = shippo.Shipment.get_rates(shipmentId)
    return rates

shipmentId = argv[1]
print(retrieve_rates(shipmentId))
