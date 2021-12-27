from utils import *
from config import (faucet_address, network_type)
from ex1 import P2PKH_scriptPubKey
from ex2a import Q2a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0002026 # amount of BTC in the output you're splitting minus fee
txid_to_spend = (
        '7933836103a08bab563af7004dfbab57f78c77e250c6c9d9bd443fd6cb172b2d')
utxo_index = 0  # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
txin_scriptSig = [
        0x15B0, 0x0F76
]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
