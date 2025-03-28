import hashlib
import hmac


def secure_keyed_hash(input_string, secret_key):
    # Convert the secret key and input string to bytes
    secret_key_bytes = bytes(secret_key, ‘utf-8’)
    input_bytes = bytes(input_string, ‘utf-8’)
    # Generate the HMAC hash using SHA-256 algorithm and the secret key
    hmac_hash = hmac.new(secret_key_bytes, input_bytes, hashlib.sha256)
    # Return the hexadecimal representation of the HMAC hash
    return hmac_hash.hexdigest()


# Example usage
input_string = “Sensitive data to hash”
secret_key = “SecretKey123”
# Generate secure keyed hash
hashed_value = secure_keyed_hash(input_string, secret_key)
# Display the hashed value
print(“Secure keyed hash: ”, hashed_value)
