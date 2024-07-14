#!/bin/bash

generate_private_prm()
{
    openssl genrsa -aes128 -out ${1} 1024 
}

generate_public_prm()
{
    openssl rsa -in ${1} -pubout -out ${2}
}

openssl_encrypt()
{
    openssl rsautl -encrypt -inkey ${1} -pubin -in ${2} -out ${3}
}

openssl_decrypt()
{
    openssl rsautl -decrypt -inkey ${1} -pubin -in ${2} > ${3}
}

openssl_sign()
{
    openssl dgst -md5 -out ${1} -sign ${2} ${3}
}

openssl_check_sign()
{
    openssl dgst -md5 -verify ${1} -signature ${2} ${3}
}

