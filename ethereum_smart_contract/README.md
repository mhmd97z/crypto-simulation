## Ethereum Smart Contract
## ERC20 Token
ERC20, which stands for Ethereum Requests for Comment, is a set of programming rules that all Ethereum-based tokens are expected to follow. The Ethereum Developers agreed on these three (optional) variables, six functions, and two logging events as protocol standard for the minimal
viable token, in order to normalize expected behaviors while communicating across the Ethereum network. By establishing this protocol, Ethereum developers are able to more easily integrate and work with token contracts already published to the network. FMI refer [here](https://medium.com/setocean/advanced-cryptocurrency-topics-erc20-interface-7372e97f4a42).

## eBook Library
The manager of an eBook library has decided to lend his books through Ethereum smart contract to show that he follows the latest technology. He wants this smart contract to support the following functionality:
- The eBook library doesn’t accept Ethereum and has its own token named ``ELT``. all users need to exchange their Ether for ELT in order to use the library services
- The admin can add books to the smart contract.
- A book is accessible by 1 user at the same time and until the access of the last user to the book hasn’t been revoked, no one else can access this book even though he/she pay for the book.
- All the books are determined by a unique ID. The contract keeps a list of all books and their specifications including their validity (means that if this bookId has been added by admin before), their genre and their access fee. All the prices are in ```ELT```.
- Any user that wants to access a book, should call ``access`` function and determine the Id of the book he/she wants to access and pay the access fee of that book. If the Id is valid and the book is available (not in access by someone else) access to this book will be granted to the user for an ``accessDuration``.
- The smart contract keeps a mapping of all rented books to the information of the user which has access to them and the ``accessStartTime`` and if the book is available or not.
- The ``accessDuration`` is defined by the admin, and after this passes the admin can revoke the user’s access to the book.
- A user can call ``changeToPremium`` function and pay ``premiumFee`` in SLTs and become a premium user.
- ``premiumFee`` is determined by admin in the constructor.
- Premium users have a special privilege. if they want access to a book that is rented by a regular user, the access of that regular user to that book is revoked and the access fee is transferred to his/her ELT account and the access of the book is granted to the premium user. But if the current renter also has a premium account, the new user can’t access the
book. In other words, premium users have a priority over regular users but they don’t have any priority over other premium users. notice that premium users also should pay for any book they rent like regular users.
- ``EBookLibrary`` contract is a child of the ``CustomERC20`` contract which you completed before.
- There is a function ``deposit`` in the ``EBookLibrary`` contract which accepts Ether and allocates the sender the same amount of ELTs.
- Any user who wants to exit the library, can call the ``withdraw`` function and withdraw his/her unspent ELTs in Ether.
  
Example scenario:
1. Sara creates the smart contract by this input: ("600","EBookLibraryToken", "ELT", "18", "10")
2. Sara adds book ("1", "1", "4") as admin.
3. Ali deposits 4 ELTs and then access the book "1".
4. Mohammad deposits 20 ELTs and then change his account to premium.
5. Mohammad wants to access the book "1". The access duration for Ali hasn’t ended but because Mohammad is a premium user he can access this book and Ali’s ELTs are refunded to him.

## Deploy to a testnet 
We are going to deploy the EBookLibrary app to Reposten public testnet.
Prerequisites:
- Download MetaMask extension from Chrome Web Store
- Go through MetaMask setup steps
- After setup select Ropsten Test Network from the drop down on top of the extension
- Click on deposit and then GET ETHER to get your first test net ethers
- In remix (a favorite Ethereum IDE) change the environment to Injected Web3
- If everything goes right you should be able to see your account and its balance

Deploy the contract to Ropsten network
- Deploy the EBookLibrary to Ropsten Network using remix.
- MetaMask catches your request and asks you to confirm it. You can tweak some variable here too
- If everything goes right, after the confirmation your contract will be deployed to [Ropsten](https://ropsten.etherscan.io) and you can trace your transaction on Etherscan using the links provided in remix as well as MetaMask.