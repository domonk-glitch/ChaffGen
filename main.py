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


def split_paragraphs(text):
    paragraphs = text.split("\n\n")
    return paragraphs


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

def make_dino(paragraphs):
    cipher_map = {
        "a": "u", 
        "b": "r",
        "c": "s",
        "d": "t",
        "e": "o",
        "f": "v",
        "g": "w",
        "h": "x",
        "i": "a",
        "j": "z",
        "k": "b",
        "l": "c",
        "m": "m",
        "n": "d",
        "o": "e",
        "p": "f",
        "q": "g",
        "r": "h",
        "s": "j",
        "t": "k",
        "u": "i",
        "v": "l",
        "w": "n",
        "x": "p",
        "y": "o",
        "z": "q",
        "A": "U", 
        "B": "R",
        "C": "S",
        "D": "T",
        "E": "O",
        "F": "V",
        "G": "W",
        "H": "X",
        "I": "A",
        "J": "Z",
        "K": "B",
        "L": "C",
        "M": "M",
        "N": "D",
        "O": "E",
        "P": "F",
        "Q": "G",
        "R": "H",
        "S": "J",
        "T": "K",
        "U": "I",
        "V": "L",
        "W": "N",
        "X": "P",
        "Y": "O",
        "Z": "Q"
    }
    for paragraph in paragraphs:
        


def write_chaff(hashed, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        for h in hashed:
            f.write(h + "\n")
