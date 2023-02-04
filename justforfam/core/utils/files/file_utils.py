import hashlib


def get_file_md5_hash(hash_file):
    hash_md5 = hashlib.md5()
    with hash_file as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
