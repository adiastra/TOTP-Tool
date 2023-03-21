import pyotp
import base64

# Get the TOTP secret from user input or generate a new one
user_input = input("Enter a secret key (leave blank to generate a new one): ")
if user_input:
    secret = user_input.strip()
else:
    secret = pyotp.random_base32()

# Create a TOTP object with the secret
totp = pyotp.TOTP(secret)

# Get the secret in Base32 and hexadecimal formats
base32_secret = totp.secret
hex_secret = base64.b32decode(base32_secret, casefold=True).hex()

# Print the TOTP token and both formats of the secret
print(f'TOTP Token: {totp.now()}')
print(f'Secret (Base32): {base32_secret}')
print(f'Secret (Hexadecimal): {hex_secret}')
