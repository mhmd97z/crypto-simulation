## Bitcoin Transaction
We are going to submit transactions on the Bitcoin network and learn the Bitcoin script along the way. Since Bitcoins are a bit costly, we will be working with the testnet [^1] instead.

First we are going to generate key pairs for you, Alice and Bob on the Bitcoin Testnet. Using ```keygen.py```, generate private keys for my private key, alice secret key BTC and bob secret key BTC, and record these keys in ```config.py```.

Next, we want to get some test coins for my private key and alice secret key BTC.
- Go to the Bitcoin Testnet faucet this [faucet](https://coinfaucet.eu/en/btc-testnet/) and paste in the corresponding addresses of the users. Note that faucets will often rate-limit requests for coins based on Bitcoin address and IP address, so try not to lose your test Bitcoin too often.
- Record the transaction hash the faucet provides, as you will need it for the next step. Viewing the transaction in a block explorer [blockcypher](https://live.blockcypher.com/btc-testnet/) will also let you know which output of the transaction corresponds to your address, and you will need this utxo index for the next step as well.
- The faucet doesn’t allow you to try too many times and it might block or delay your Bitcoin address and/or IP address. Since you are going to need a lot of TX outputs for the following parts, we suggest you use ```split_test_coins.py``` to split the given output to many parts. A perfect run needs around 15 outputs but we suggest 30 to give room for error. Split Alice’s coins as well.
- Next, we are going to create generate key pairs for Alice and Bob on the BlockCypher testnet
  - Sign up for an account with Blockcypher to get an API token [here](https://accounts.blockcypher.com/).
  - Create BCY testnet keys for Alice and Bob and place into ```config.py```. (run this command)
    - ```curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN```
  - Give Bob’s address bitcoin on the Blockcypher testnet (BCY) to get some funds.
    - ```curl -d ‘f\address": \BOBS BCY ADDRESS", \amount": 1000000g’ https://api.blockcypher.com/v1/bcy/test/faucet?token=$YOURTOKEN```
- Let’s also split Bob’s coins using ```split_test_coins.py```. Make sure to edit the parameters at the bottom of the file. Each time you are switching between the Bitcoin and BlockCypher testnets, make sure to visit ```config.py``` and adjust the network type variable. Make sure to record the transaction hash.

### The Problems can be found at ```Foundation_Blockchain_Practical_HW2.pdf```, and the codes are provided with solutions.


[^1]: The testnet is a network that functions similar to the mainnet of Bitcoin, but the bitcoins in it are free. It’s purpose is to help developers test their codes and play around with their tools before trying them out on the mainnet. You can read more about it [here](https://en.bitcoin.it/wiki/Testnet)
