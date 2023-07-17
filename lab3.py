import hashlib
file_path ="./Lab5-6-2023(1).pdf"
def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

# Step 1.b: Accept the online hash as input and store it
online_hash = input("Enter the online hash: ")

# Step 1.c: Calculate the hash of the imported file
imported_file_path = "path/to/your/file.ext"  # Replace with the actual file path
imported_hash = calculate_file_hash(imported_file_path)

# Step 1.d: Compare the hashes and print the result
if online_hash == imported_hash:
    print("The hashes match!")
else:
    print("The hashes do not match.")
