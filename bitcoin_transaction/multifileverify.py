import hashlib
from config import network_type
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from ex1 import P2PKH_scriptPubKey, send_from_P2PKH_transaction
from config import my_private_key
from fileverify import file_sha256
import math


def calculate_merkle_root(_filenames):
    n = len(_filenames)

    if n == 0:
        return "Error"

    elif n == 1:
        return file_sha256(_filenames[0])

    else:
        hashes = []
        for i in range(n):
            hashes.append(file_sha256(_filenames[i]))

        for iter in range(math.ceil(math.log(n, 2))):
            if n % 2 == 1:
                hashes[n] = hashes[n - 1]
                n = n + 1
            for k in range(0, n - 1, 2):
                x = hashlib.sha256()
                x.update(str(hashes[k]).encode())
                x.update(str(hashes[k + 1]).encode())
                hashes[int(k / 2)] = x.digest()
            n = int(n / 2)

        return hashes[0]


filenames = []


private_key = CBitcoinSecret.from_secret_bytes(calculate_merkle_root(filenames))
calculated_address = P2PKHBitcoinAddress.from_pubkey(private_key.pub)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000001
    txid_to_spend = (
        '0996f685bbb16ef38f57d109f7bc750511f717a1c0d191d1fb231e8dc04ce6de')
    utxo_index = 21
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(calculated_address)
    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
