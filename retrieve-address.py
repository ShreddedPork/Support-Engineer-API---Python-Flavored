import shippo
import config
from sys import argv


shippo.config.api_key = config.access_token


#can take in either either address objectID or shipment objectID
def retrieve_addresses(objectId, idType):
    address = 'No Address'
    if idType == "Shipment":
        shipment = shippo.Shipment.retrieve(objectId)
        receipientAddress = shippo.Address.retrieve(shipment.address_to.object_id)
        senderAddress = shippo.Address.retrieve(shipment.address_from.object_id)
        address = "Recipient Address: " + "\n" + str(receipientAddress) + "\n" + "Sender Address: " + "\n" + str(senderAddress) 
    elif idType == "Address":
        address = shippo.Address.retrieve(objectId)
    return address

objectId = argv[1]
idType = argv[2] #Shipment or Address
print(retrieve_addresses(objectId, idType))
