# Scalabale blockchain system

For many years, numerous cryptocurrencies have been supported by the 
innovative technology known as blockchain. This decentralized system, 
despite having many unique characteristics, falls behind centralized 
currency systems in terms of scalability and cannot be adopted by other 
platforms. Increasing throughput and reducing the dependence on huge storage 
are the goals of this project.
## Description

An in-depth paragraph about your project and overview of use.
![system overview](images/system_overview.PNG)

Transaction verification

## Getting Started

### Dependencies

* base58==2.0.1
* certifi==2020.12.5
* cffi==1.14.4
* chardet==3.0.4
* cryptography==3.3.1
* ecdsa==0.16.1
* idna==2.10
* ipfshttpclient==0.6.1
* jsonpickle==1.4.2
* llvmlite==0.36.0
* multiaddr==0.0.9
* netaddr==0.8.0
* numba==0.53.1
* numpy==1.20.3
* p2pnetwork==1.0
* Pillow==8.2.0
* pycoin==0.80
* pycparser==2.20
* pytesseract==0.3.7
* requests==2.25.0
* six==1.15.0
* starkbank==2.2.2
* starkbank-ecdsa==1.0.0
* tinyec==0.3.1
* urllib3==1.26.2
* varint==1.0.2
* IPFS

### Installing

* How/where to download your program
* Either fork or download the project 
* It is recommended to open this project in pycharm
* Install all the dependencies
* install ipfs
* run ipfs daemon in cmd
* forward a port in router
* put your local ip and port number that you forwarded in my_own_p2p_application_json.py

### Executing program
There are two parts of this program. One is the user end where a user generates 
a transaction and sends it to the validators. And the other part is the miner
end where the miner validates the transaction that the user sent and adds this 
transaction to the blockchain after validation.
* For both ends at first run the server.py to start the web server.
* A web interface will be hosted at http://localhost:5000
* Go to http://localhost:5000 in your browser (preferably Google Chrome) and use the web interface according to the need.


[comment]: <> (* How to run the program)

[comment]: <> (* Step-by-step bullets)

[comment]: <> (```)

[comment]: <> (code blocks for commands)

[comment]: <> (```)
#### User End
  * How to run the program
  * By going to http://localhost:5000 address in the browser a home page will be found
  * Click the user end button to go to the user end page
  * Click the button in the user end page to generate a new public-private key pair and an address.
  * Store these information locally.
  * Share the newly generated address with the sender that will make the transaction.
  * The sender will then click the button in "" to go to the transaction generation page.
  * In transaction generation page the sender will fill up a form with corresponding data and click the button to genrate a transaction.
  * In the next page the sender/ user will review the transaction and press the button "send" to send the transaction to the miners.
  * Step-by-step bullets

[comment]: <> (  ```)

[comment]: <> (  code blocks for commands)

[comment]: <> (    ```)
#### Miner End
  * How to run the program
  * By going to http://localhost:5000 address in the browser a home page will be found.
  * In the miner end page there is a button to start the mining process
  * After clicking the button the system will start to verify transactions and generate raw block and hash block.
  * And will add these blocks to the corresponding blockchains and will broadcast the hash block among other miners.

[comment]: <> (  * )

[comment]: <> (  * Step-by-step bullets)

[comment]: <> (    ```)

[comment]: <> (    code blocks for commands)

[comment]: <> (    ```)
## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Minhaz Mamud  
[@linkedin](https://www.linkedin.com/in/minhaz18)  
[@gmail](mailto:minhaz18061997@gmail.com)

## Version History

* 0.1
    * Initial Release
    * See [commit change]() or See [release history]()



## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)