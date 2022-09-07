import shippo
import config
from sys import argv


shippo.config.api_key = config.access_token

def retrive_shipment(shipmentId):
    shipment = shippo.Shipment.retrieve(shipmentId)
    return shipment
    
shipmentId = argv[1] 
print (retrive_shipment(shipmentId))



