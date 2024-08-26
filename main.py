import hashlib

def calculate_hash(file_path):
    hash_obj = hashlib.sha1()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(1024):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
        return None

# File paths
file1_path = input("Enter the path of file-1")
file2_path = input("Enter the path of file-2")

file1 = file1_path
file2 = file2_path

# Calculate hashes
hash1 = calculate_hash(file1)
hash2 = calculate_hash(file2)

# Compare and print result
if hash1 and hash2:
    if hash1 == hash2:
        print("These files are identical")
    else:
        print("These files are not identical")
else:
    print("One or both files could not be read")