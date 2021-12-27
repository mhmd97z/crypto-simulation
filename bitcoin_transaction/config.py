from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress

SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

my_private_key = CBitcoinSecret(
    'cSUG4kbSYXCL7RV3f6Vc2PhrXvTu4BGnMB9FF7YJtL3uSK83FHuH')
# Address: mheXzFYsXfeVS56VTvYy7fsUKN58spy3gb
# TX_first: 3af2de1ff0ba4af64cca89e9a753115734280e684842a991fc81b372490ebd1a
# TX_first2: 2c14d0bc6673f8bf09a7ba90ba4c12b125198bed9e2132c86acd8efc377d11c5    0.02507807

my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################

faraz_private_key = CBitcoinSecret(
    'cPuCfRTMjLQ2KWxCFFDtt4KJVxqBws2soRNJzSvo43AgcvCD6irW')
# Address: mmxWnVAbz34y4UfWLAK35eqA7ZDExdTZ1p
faraz_public_key = faraz_private_key.pub
faraz_address = P2PKHBitcoinAddress.from_pubkey(faraz_public_key)


ata_private_key = CBitcoinSecret(
    'cViQsb3mrSA826VGT3QXY2taewrW7R8UriBJjC2phAhzwW3XYwfq')
# Address: msTrWLioxH6NhkFZC2e1ha7g9rjsr8N8tF
ata_public_key = ata_private_key.pub
ata_address = P2PKHBitcoinAddress.from_pubkey(ata_public_key)

shareholder1_private_key = CBitcoinSecret(
    'cRuXvFBHeWU5afwQLYwbb8MoVTLJtsgHrdhBjDRxShaoeHkhYFxE')
# Address: mq5s26eyM1TX9vWRebcKYJjfuLJQo56JuG
shareholder1_public_key = shareholder1_private_key.pub
shareholder1_address = P2PKHBitcoinAddress.from_pubkey(shareholder1_public_key)

shareholder2_private_key = CBitcoinSecret(
    'cN6ED2Zg64sq1M1JeuR9Qe63SozadXJHRw4xJ7TdmHqwNbfdSupA')
# Address: mn4odtfBGoGPS5qcEGHJR4tAdV5UR4uzRG
shareholder2_public_key = shareholder2_private_key.pub
shareholder2_address = P2PKHBitcoinAddress.from_pubkey(shareholder2_public_key)

shareholder3_private_key = CBitcoinSecret(
    'cRJzh1tT6by3JiNJHg1acDWXD4kEsybEWbZ4EQwmq2ojJv2M6u1X')
# Address: mg4Qe5fHUo54jPiTD84yYemhWShCFWBeU3
shareholder3_public_key = shareholder3_private_key.pub
shareholder3_address = P2PKHBitcoinAddress.from_pubkey(shareholder3_public_key)

shareholder4_private_key = CBitcoinSecret(
    'cP5VHiLTyc3xqHbJq68U2qgsiTDLwBuyEP6HwsQ4b19Y2cxDc61g')
# Address: mtMsHBQet3QdNcjqL2E7idCNGJbuQpc3SB
shareholder4_public_key = shareholder4_private_key.pub
shareholder4_address = P2PKHBitcoinAddress.from_pubkey(shareholder4_public_key)

shareholder5_private_key = CBitcoinSecret(
    'cQY6jE93w7kPQksyB2ph6nfbpW7yqCXbVhVvTeMVfGcrV8XXbr5n')
# Address: mjf1bZuUrMAZYe1j5pZWPRf3CTE3wCoGrn
shareholder5_public_key = shareholder5_private_key.pub
shareholder5_address = P2PKHBitcoinAddress.from_pubkey(shareholder5_public_key)

######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cNyoNjiSmKJ5ohjJqu9YRVAeNr94EoHahGt8ZonJbFKnxsjsvYdk')
# Address: mi7z5W3RukyruizHPmw2cShCgygaCTzMzH
# Tx: 1d19241d11f7faa25e1cd8d9107d2b5d55fd0306f7e858530b254fb7dacfcfd2

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cNG3gJq9iLZvQzowMhMRTPcAm78H9GxHr2Fo5LiykYvv21NdP7aj')
# Address: n3ycb29B5pmQrvqKX5ABXDYoGuis6U1Zrv

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('22d2403d5c2209ff20fb2d7481680e41eb04e39eb73dc7b93918049d04f3d3f6'))

'''
{
  "private": "22d2403d5c2209ff20fb2d7481680e41eb04e39eb73dc7b93918049d04f3d3f6",
  "public": "0370f598081948595fafbd23573d198a4722179a33919f8a83fe993d10ed7999ab",
  "address": "ByEfVrGQLgh66ubofBunQng98wbRhzuaYZ",
  "wif": "BpVieMiFpUeCPvHefY1Q51W211Q7HSwaA5z2YeyCZKuybsbQVL1k"
}
'''

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('42db155dfee436cb34b95afc00f29ed4d43de97a8304763328fd8adbd2a67b52'))
'''
{
  "private": "42db155dfee436cb34b95afc00f29ed4d43de97a8304763328fd8adbd2a67b52",
  "public": "02d160ef35f1cfb3bccf35fe5d7c974007715c8f2bdcefeedc5b3b01d7edfdbc7f",
  "address": "BwsN5W8KT9nxQvZruyG7rFtAGCnJ2EXiVs",
  "wif": "BqZzMcoqA1RMVmgU6SqRv2Lxwwrp9yYLsSFW788fymyjMBk7MzFV"
}

{
  "tx_ref": "43d9941e06728563f2cb40f045633eca8626b1740584b5cd544ea89bb7ebc25b"
}

splitting Tx: a2aebb8d1b1adabc7d844f74c3bdfecd5c3fc26cda67dded8d1e5bece019a3ee

'''

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################
