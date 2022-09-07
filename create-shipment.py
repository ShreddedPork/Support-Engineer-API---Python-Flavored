import shippo
import config
from sys import argv
import json

shippo.config.api_key = config.access_token

with open("sampleShipment.json", "r") as f:
    sampleShipment = json.load(f)
    address_from = sampleShipment["address_from"]
    address_to = sampleShipment["address_to"]
    parcel = sampleShipment["parcels"]
    

#create shipment object
def create_shipment():
    shipment = shippo.Shipment.create(
        address_from = address_from,
        address_to = address_to,
        parcels = parcel
    )
    return shipment

print (create_shipment())

