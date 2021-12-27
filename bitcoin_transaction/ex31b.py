from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (faucet_address, network_type,
                    faraz_private_key, faraz_public_key, faraz_address,
                    ata_private_key, ata_public_key, ata_address,
                    shareholder1_private_key, shareholder1_public_key, shareholder1_address,
                    shareholder2_private_key, shareholder2_public_key, shareholder2_address,
                    shareholder3_private_key, shareholder3_public_key, shareholder3_address,
                    shareholder4_private_key, shareholder4_public_key, shareholder4_address,
                    shareholder5_private_key, shareholder5_public_key, shareholder5_address
                    )
from ex1 import P2PKH_scriptPubKey
from ex31a import Q31a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0001026  # amount of BTC in the output you're splitting minus fee
txid_to_spend = (
        '25815d773ec2c8c9bd405800d71e922771c55d713bbf06b614aed788f0b2f7e4')
utxo_index = 0  # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q31a_txout_scriptPubKey
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
txin = create_txin(txid_to_spend, utxo_index)
txout = create_txout(amount_to_send, txout_scriptPubKey)

faraz_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, faraz_private_key)
ata_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, ata_private_key)
shareholder1_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder1_private_key)
shareholder2_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder2_private_key)
shareholder3_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder3_private_key)
shareholder4_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder4_private_key)
shareholder5_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder5_private_key)


######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
txin_scriptSig = [
        OP_0, shareholder1_signature, shareholder2_signature, shareholder3_signature, OP_0, faraz_signature
    ]
######################################################################
response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
