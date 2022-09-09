#  Support Engineering API - Python Flavored      

## Description

A simple tool that allows users to access the shippo API. A user can 
* create a shipment
* retrieve a shipment 
* retrieve rates for a specific shipment
* retrieve addresses associated with the shipment, 
* retrieve the parcels associated with a shipment.

## Getting Started

### Dependencies

* Please make sure to have python3 installed globally along with PIP in order to install the shippo module. 
* MacOS Catalina preferred
* In order to access the API, please visit [goshippo.com](goshippo.com), click sign up for free, navigate to the API section under headings and click generate test token. Store it somewhere safe!
* Note - The shipment reference JSON object is just there for reference values

### Installing Python

* Python3 can be installed either via the website or as an extension in VScode. 
* [Download from python website](https://www.python.org/downloads/)
* [Download as an extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Installing PIP
* PIP is required for installing the shippo module. Please use the commands below in the CLI to install PIP
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py
```
### Installing Shippo
```
pip3 install shippo
```

## Executing program
* In order to be able to run the program, you will need to create your own config.py file and paste this line of code as follows replacing the brackets with your own token. 
* Place your config file in the root directory
```
access_token = "<INSERT TEST TOKEN HERE>"
```

### API Commands/Descriptions

* this command will create a shipment
* Note - This shipment is created with the JSON object sampleShipment. Feel free to plug your own JSON file in here
```
python3 create-shipment.py 
```

* this command will retrieve a shipment when you plug in a shipments object_id at the end
```
python3 retrieve-shipment.py <INSERT SHIPMENT object_id HERE>
```

* this command will retrieve the rates for a shipment when you plug in a shipments object_id at the end
```
python3 retrieve-rates.py <INSERT SHIPMENT object_id HERE>
```

* this command takes in the shipment object_id / address object_id and the keyword "Shipment" / "Address" and returns both sender and recipient addresses, or the address of the sender/recipient respectively
```
python3 retrieve-address.py <INSERT SHIPMENT object_id> <"Shipment">
python3 retrieve-address.py <INSERT ADDRESS object_id> <"Address">

Ex. python3 retrieve-address.py 12345 Shipment
```

* this command takes in either the parcel object_id / shipment object_id and the keyword "Shipment" / "Parcel" and returns the associated parcel
```
python3 retrieve-parcel.py <INSERT SHIPMENT object_id> <"Shipment">
python3 retrieve-parcel.py <INSERT PARCEL object_id> <"Parcel">

Ex. python3 retrieve-parcel.py 12345 Parcel
```

## Authors 
Ryan Ho 