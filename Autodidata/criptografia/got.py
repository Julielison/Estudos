from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_AES(key, data, iv=None):
    if iv is None:
        cipher = AES.new(key, AES.MODE_CBC)
    else:
        iv = base64.b64decode(iv)
        cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt_AES(key, iv, ct):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# Example usage:
key = b'ThisIsASecretKey'  # 128-bit key
data = "Hello, AES encryption!"
custom_iv = 'Rm9vYmFyMTIzNDU2Nzg5MA=='  # Custom IV in base64 format
iv, encrypted_data = encrypt_AES(key, data, custom_iv)
print("Encrypted data:", encrypted_data)
print("IV:", iv)
decrypted_data = decrypt_AES(key, iv, encrypted_data)
print("Decrypted data:", decrypted_data)