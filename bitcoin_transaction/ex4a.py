from bitcoin.core.script import *
from config import (my_private_key, my_address, network_type)
from ex1 import send_from_P2PKH_transaction

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q4a_txout_scriptPubKey = [
        0x5E033ED8, OP_CHECKLOCKTIMEVERIFY, OP_DROP, OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIG
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00020260  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '0996f685bbb16ef38f57d109f7bc750511f717a1c0d191d1fb231e8dc04ce6de')
    utxo_index = 8  # index of the output you are spending, indices start at 0
    ######################################################################
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q4a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
