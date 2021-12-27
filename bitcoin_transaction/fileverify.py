import hashlib
from config import network_type
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from ex1 import P2PKH_scriptPubKey, send_from_P2PKH_transaction
from config import my_private_key


def file_sha256(filename):
    h = hashlib.sha256()
    file_object = open(filename, "r")
    h.update(file_object.read().encode())
    return h.digest()


private_key = CBitcoinSecret.from_secret_bytes(file_sha256('data.hex'))
calculated_address = P2PKHBitcoinAddress.from_pubkey(private_key.pub)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000001
    txid_to_spend = (
        '0996f685bbb16ef38f57d109f7bc750511f717a1c0d191d1fb231e8dc04ce6de')
    utxo_index = 5
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(calculated_address)
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
