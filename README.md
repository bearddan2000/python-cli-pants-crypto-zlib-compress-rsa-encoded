# python-cli-pants-crypto-zlib-compress-rsa-encoded

## Description
Compare hashed passwords. RSA
is an asymmetric algorithm that
uses a 3072 bit key. Encryption is
done by public key while decryption
is by private key.

Since RSA generates a long encryption we use compression to store and/or transport.

## Tech stack
- pants
- python 3.8

## Docker stack
- pantsbuild/centos7:latest

## To run
`sudo ./install.sh -u`

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credits
https://cryptobook.nakov.com/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples
