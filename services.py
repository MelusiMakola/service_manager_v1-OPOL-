import hashlib

def hash_data(data):
    """Hashes the input data using SHA-256."""
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data

# Example usage:
data_to_hash = input("Data to be hashed: ")
hashed_data = hash_data(data_to_hash)
print("Original data:", data_to_hash)
print("Hashed data:", hashed_data)
