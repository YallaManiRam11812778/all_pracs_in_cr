from cryptography.fernet import Fernet
message = "hello geGSekKs"
# key = Fernet.generate_key()
key = "P9Z_BQyIXWFbi54aynKZrMmKGQo24gc73EVAvPNEW1g="
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)