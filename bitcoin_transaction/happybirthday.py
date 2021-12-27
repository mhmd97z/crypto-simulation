from bitcoin.core.script import *

from config import (my_private_key, network_type)
from ex1 import send_from_P2PKH_transaction

######################################################################
message_hex = "Happy Birthday Hamed".encode().hex().encode()

message_txout_scriptPubKey = [
        OP_RETURN, message_hex
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00030260  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '0996f685bbb16ef38f57d109f7bc750511f717a1c0d191d1fb231e8dc04ce6de')
    utxo_index = 4  # index of the output you are spending, indices start at 0
    ######################################################################
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        message_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
