from bitcoin.core.script import *

######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# TODO: Fill these in to create scripts that are redeemable by both
#       of the above conditions.
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script


# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):

    return [
        OP_DEPTH, 1, OP_EQUAL, OP_IF, OP_HASH160, hash_of_secret, OP_EQUAL, OP_ELSE, public_key_sender,
        OP_CHECKSIGVERIFY, public_key_recipient, OP_CHECKSIG, OP_ENDIF
    ]


# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        secret
    ]


# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        sig_recipient, sig_sender
    ]
######################################################################

######################################################################
#
# Configured for your addresses
#
# TODO: Fill in all of these fields
#


alice_txid_to_spend = "d78e540e7e25dde8d5e0eaf8841cc5842ff385018ba3c3b4d1dc8f3bfd7ec596"
alice_utxo_index  = 0
alice_amount_to_send = 0.0008026

bob_txid_to_spend = "a2aebb8d1b1adabc7d844f74c3bdfecd5c3fc26cda67dded8d1e5bece019a3ee"
bob_utxo_index = 0
bob_amount_to_send = 0.0003333

# Get current block height (for locktime) in 'height' parameter for each blockchain (and put it into swap.py):
#  curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height = 1611983

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height = 2650861

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
## alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.0001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = True

######################################################################
