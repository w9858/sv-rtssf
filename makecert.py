# https://stackoverflow.com/a/60804101
# https://stackoverflow.com/a/44118545

from OpenSSL import crypto, SSL
import random

def cert_gen(
    commonName="*.relefra.jp",
    countryName="JP",
    localityName="Sorasaki-city",
    stateOrProvinceName="Sorasaki-city",
    organizationName="Tsukikage",
    validityStartInSeconds=0,
    validityEndInSeconds=10*365*24*60*60,
    KEY_FILE = "./cert/privkey.pem",
    CERT_FILE = "./cert/fullchain.pem",
    SAN = "DNS:*.relefra.jp, DNS:relefra.jp, DNS:api.relefra.jp, DNS:img.relefra.jp"):
    #can look at generated file using openssl:
    #openssl x509 -inform pem -in selfsigned.crt -noout -text
    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)
    # create a self-signed cert
    cert = crypto.X509()
    cert.set_version(2)
    cert.get_subject().C = countryName
    cert.get_subject().ST = stateOrProvinceName
    cert.get_subject().L = localityName
    cert.get_subject().O = organizationName
    cert.get_subject().CN = commonName
    # Add base constraints
    cert.add_extensions([
        crypto.X509Extension(
            b"keyUsage", False,
            b"Digital Signature, Key Encipherment"),
        crypto.X509Extension(
            b"basicConstraints", False, b"CA:TRUE"),
        crypto.X509Extension(
            b'extendedKeyUsage', False, b'serverAuth'),
    ])
    cert.add_extensions([crypto.X509Extension(b"subjectAltName", False, SAN.encode())])
    cert.set_serial_number(random.randint(50000000,100000000))
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')
    with open(CERT_FILE, "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
    with open(KEY_FILE, "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))

try:
    cert_gen()
    print("Done.")
except Exception as e:
    print(e)
    print("Failed!")

input()
