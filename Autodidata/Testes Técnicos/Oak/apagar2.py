import base64

def base64_to_binary(base64_string):
    byte_array = base64.b64decode(base64_string)
    return ''.join(format(byte, '08b') for byte in byte_array)

def xor_with_fixed_vector(binary_string, fixed_vector):
    fixed_vector = fixed_vector[:len(binary_string)]
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(binary_string, fixed_vector))

def reverse_binary(binary_string):
    return binary_string[::-1]

def invert_binary(binary_string):
    return ''.join('1' if bit == '0' else '0' for bit in binary_string)

def binary_to_string(binary_string):
    char_array = [chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)]
    return ''.join(char_array)

def decrypt(encrypted_base64, fixed_vector):
    xored_binary = base64_to_binary(encrypted_base64)
    reversed_binary = reverse_binary(xored_binary)
    inverted_binary = invert_binary(reversed_binary)
    original_binary = xor_with_fixed_vector(inverted_binary, fixed_vector)
    return binary_to_string(original_binary)

if __name__ == "__main__":
    encrypted_base64 = "Wfvb+dlz2RuZO3szeXMJm8NDW+Pz4w=="
    fixed_vector = "10101010101010101010101010101010" * 10
    decrypted = decrypt(encrypted_base64, fixed_vector)
    print("Decrypted String:", decrypted)
