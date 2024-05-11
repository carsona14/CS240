# Carson Adams
# 5/3/2024
# CS240 Data Structures and Algorithms
# Chapter 5: Hash Tables

def hash_function(key, base, mod):
    hash_value = 0
    for character in key:
        # Converts character to unicode code point
        code = ord(character)
        # Horner method 
        hash_value = (hash_value * base + code) % mod
    return hash_value

key = "hello world"
base = 69 
mod = 420
index = hash_function(key, base, mod)
print("The hash index for the key" ,key, "is:", index)
