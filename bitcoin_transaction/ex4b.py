from utils import *
from config import (my_private_key, my_public_key, faucet_address, network_type)
from ex1 import P2PKH_scriptPubKey
from ex4a import Q4a_txout_scriptPubKey
from ex1 import P2PKH_scriptSig

######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0000026  # amount of BTC in the output you're splitting minus fee
txid_to_spend = (
        '07b645691d229a4a29f5c59ea466503f084020b0bdbe2df25d464f479e031355')
utxo_index = 0  # index of the output you are spending, indices start at 0
######################################################################

######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
txout = create_txout(amount_to_send, txout_scriptPubKey)

txin_scriptPubKey = Q4a_txout_scriptPubKey
txin = create_txin(txid_to_spend, utxo_index)
txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey, my_private_key, my_public_key)

######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
