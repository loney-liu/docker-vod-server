#### The original file link 
https://gist.github.com/taoyuan/39d9bc24bafc8cc45663683eae36eb1a

#### Generation of a Self Signed Certificate
Generation of a self-signed SSL certificate involves a simple 3-step procedure:

*STEP 1*: Create the server private key

```
openssl genrsa -out cert.key 2048
```

*STEP 2*: Create the certificate signing request (CSR)
```
openssl req -new -key cert.key -out cert.csr
```

*STEP 3*: Sign the certificate using the private key and CSR

```
openssl x509 -req -days 3650 -in cert.csr -signkey cert.key -out cert.crt
```

Congratulations! You now have a self-signed SSL certificate valid for 10 years.

### Put everything in one command

```
openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=CN/ST=BJ/L=BJ/O=Global Security/OU=Test Department/CN=f.ll.tt" \
    -keyout cert.key  -out cert.crt
```

### Generate combined_cert.pem

```
cat cert.key cert.crt> combined_cert.pem
```