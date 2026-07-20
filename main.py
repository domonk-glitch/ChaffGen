import sys
import hashlib
import random
import os

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_file_text(file_path)
    output_path = "output/chaff.txt"
    chunks = make_chunks(text)
    hashed = hash_chunks(chunks)
    write_chaff(hashed, output_path)


def get_file_text(path):
    with open(path) as f:
        return f.read()


def make_chunks(text):
    chunks = []
    p = 0
    while p < len(text):
        r = random.randint(20, 140)
        chunk = text[p:p+r]
        p = p + r
        chunks.append(chunk)
    return chunks


def hash_chunks(chunks):
    hashed_chunks = []
    for chunk in chunks:
        if len(chunk) < 33:
            hashed_chunks.append(hashlib.md5(chunk.encode()).hexdigest())
        elif len(chunk) < 50:
            hashed_chunks.append(hashlib.sha1(chunk.encode()).hexdigest())
        elif len(chunk) < 70:
            hashed_chunks.append(hashlib.sha256(chunk.encode()).hexdigest())
        elif len(chunk) < 110:
            hashed_chunks.append(hashlib.sha384(chunk.encode()).hexdigest())
        else:
            hashed_chunks.append(hashlib.sha512(chunk.encode()).hexdigest())
    return hashed_chunks


def write_chaff(hashed, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        for h in hashed:
            f.write(h + "\n")
