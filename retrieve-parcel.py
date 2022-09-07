import shippo
import config
from sys import argv


shippo.config.api_key = config.access_token


def retrive_parcel(objectId, idType):
    parcel = None
    if idType == "Shipment":
        shipment = shippo.Shipment.retrieve(objectId)
        parcel = shippo.Parcel.retrieve(shipment.parcels[0].object_id) 
    elif idType == "Parcel":
        parcel = shippo.Parcel.retrieve(objectId)
    return parcel
    
objectId = argv[1]
idType = argv[2] #Shipment or Parcel 
print (retrive_parcel(objectId, idType))
