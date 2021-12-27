from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type,
                    faraz_private_key, faraz_public_key, faraz_address,
                    ata_private_key, ata_public_key, ata_address,
                    shareholder1_private_key, shareholder1_public_key, shareholder1_address,
                    shareholder2_private_key, shareholder2_public_key, shareholder2_address,
                    shareholder3_private_key, shareholder3_public_key, shareholder3_address,
                    shareholder4_private_key, shareholder4_public_key, shareholder4_address,
                    shareholder5_private_key, shareholder5_public_key, shareholder5_address
                    )
from ex1 import send_from_P2PKH_transaction

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3-2
Q32a_txout_scriptPubKey = [
        1, faraz_public_key, ata_public_key, 2, OP_CHECKMULTISIGVERIFY,
        3, shareholder1_public_key, shareholder2_public_key, shareholder3_public_key, shareholder4_public_key,
        shareholder5_public_key, 5, OP_CHECKMULTISIG
    ]

######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00040260 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        '0996f685bbb16ef38f57d109f7bc750511f717a1c0d191d1fb231e8dc04ce6de')
    utxo_index = 3 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q32a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
