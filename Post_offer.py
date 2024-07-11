import requests
from random import randint
from eth_account import Account
from eth_account.messages import *
import time
from creds import private_key, api_os

private_key = private_key
api_os=api_os
url = "https://api.opensea.io/api/v2/orders/matic/seaport/offers"
startTime= int(time.time())
endTime= int(startTime + 43200)
salt= randint(1,100000)
parameters = {
    "orderType": 3,
    "offerer": "0x900d18C41C1a13A757d66EC0Cd02c32c8446f509",
    "offer": [
        {
            "itemType": 1,
            "token": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
            "identifierOrCriteria": 0,
            "startAmount": 15000,
            "endAmount": 15000
        }
    ],
    "consideration": [
        {
            "itemType": 3,
            "token": "0x22d5f9B75c524Fec1D6619787e582644CD4D7422",
            "identifierOrCriteria": 457,
            "startAmount": 1,
            "endAmount": 1,
            "recipient": "0x900d18C41C1a13A757d66EC0Cd02c32c8446f509"
        },
        {
            "itemType": 1,
            "token": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
            "identifierOrCriteria": 0,
            "startAmount": 375,
            "endAmount": 375,
            "recipient": "0x0000a26b00c1F0DF003000390027140000FAa719" 
        }
    ],
    "startTime": startTime,
    "endTime": endTime,
    "zone": "0x000056F7000000EcE9003ca63978907a00FFD100",
    "zoneHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "salt": salt,
    "conduitKey": "0x0000007b02230091a7ed01230072f7006a004d60a8d4e71d599b8104250f0000",
    "totalOriginalConsiderationItems": 2,
    "counter": "0"
}

msg = {
    "types": {
        "EIP712Domain": [
            {"name": "name", "type": "string"},
            {"name": "version", "type": "string"},
            {"name": "chainId", "type": "uint256"},
            {"name": "verifyingContract", "type": "address"},
        ],
        "OrderComponents": [
            {"name": "offerer", "type": "address"},
            {"name": "zone", "type": "address"},
            {"name": "offer", "type": "OfferItem[]"},
            {"name": "consideration", "type": "ConsiderationItem[]"},
            {"name": "orderType", "type": "uint8"},
            {"name": "startTime", "type": "uint256"},
            {"name": "endTime", "type": "uint256"},
            {"name": "zoneHash", "type": "bytes32"},
            {"name": "salt", "type": "uint256"},
            {"name": "conduitKey", "type": "bytes32"},
            {"name": "counter", "type": "uint256"}
        ],
        "OfferItem": [
            {"name": "itemType", "type": "uint8"},
            {"name": "token", "type": "address"},
            {"name": "identifierOrCriteria", "type": "uint256"},
            {"name": "startAmount", "type": "uint256"},
            {"name": "endAmount", "type": "uint256"},
        ],
        "ConsiderationItem": [
            {"name": "itemType", "type": "uint8"},
            {"name": "token", "type": "address"},
            {"name": "identifierOrCriteria", "type": "uint256"},
            {"name": "startAmount", "type": "uint256"},
            {"name": "endAmount", "type": "uint256"},
            {"name": "recipient", "type": "address"},
        ]
    },
    "primaryType": "OrderComponents",
    "domain": {
        "name": "Seaport",
        "version": "1.6",
        "chainId": 137,
        "verifyingContract": "0x0000000000000068F116a894984e2DB1123eB395",
    },
    "message":parameters
    }

encoded_msg = encode_typed_data(full_message=msg)
signed_message = Account.sign_message(encoded_msg, private_key=private_key)
signature = signed_message.signature.hex()

parameters["startTime"]=str(parameters["startTime"])
parameters["endTime"]=str(parameters["endTime"])
parameters["salt"]=str(parameters["salt"])
parameters["totalOriginalConsiderationItems"]=str(parameters["totalOriginalConsiderationItems"])

parameters["offer"][0]["identifierOrCriteria"]=str(parameters["offer"][0]["identifierOrCriteria"])
parameters["offer"][0]["startAmount"]=str(parameters["offer"][0]["startAmount"])
parameters["offer"][0]["endAmount"]=str(parameters["offer"][0]["endAmount"])

parameters["consideration"][0]["identifierOrCriteria"]=str(parameters["consideration"][0]["identifierOrCriteria"])
parameters["consideration"][0]["startAmount"]=str(parameters["consideration"][0]["startAmount"])
parameters["consideration"][0]["endAmount"]=str(parameters["consideration"][0]["endAmount"])
parameters["consideration"][1]["identifierOrCriteria"]=str(parameters["consideration"][1]["identifierOrCriteria"])
parameters["consideration"][1]["startAmount"]=str(parameters["consideration"][1]["startAmount"])
parameters["consideration"][1]["endAmount"]=str(parameters["consideration"][1]["endAmount"])

payload = {
    "protocol_address": "0x0000000000000068f116a894984e2db1123eb395",
    "parameters": parameters,
    "signature": str(signature)
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": f"{api_os}"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)