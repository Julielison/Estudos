from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'Sixteen byte key'
data = 'some text to encrypt'.encode("UTF-8")
data = pad(data, AES.block_size)
encryptor = AES.new(key, AES.MODE_CBC)
iv = encryptor.IV
decryptor = AES.new(key, AES.MODE_CBC, IV=iv)

ciphertext = encryptor.encrypt(data)
print(ciphertext)
plaintext = decryptor.decrypt(ciphertext)
print(unpad(plaintext, 16))