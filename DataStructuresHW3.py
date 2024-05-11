# Carson Adams
# 5/3/2024
# CS240 Data Structures and Algorithms
# Chapter 5: Hash Tables
# Hash table with a return of 1
# Hash table using the length of the string as index

class HashTable:
    def __init__(self, words, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.load_words(words)
    
    def hash(self, key):
        raise NotImplementedError("Hash function not implemented.")
    
    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))
        print("Inserted: ", key, value, "at index", index)
    
    def get(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                print("Found:", v, "for key", key, "at index", index)
                return v
        print("Key", key, "not found")
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                print("Deleted key", key, "from index", index)
                return True
        print("Key", key, "not found for deletion")
        return False

    def load_words(self, words):
        for word in words:
            self.insert(word, word)  # Use word itself as value

class HashTableConstant(HashTable):
    def __init__(self, words, size=10):
        super().__init__(words, size)

    def hash(self, key):
        return 1

class HashTableLength(HashTable):
    def __init__(self, words, size=100):
        super().__init__(words, size)

    def hash(self, key):
        return len(key) % self.size

def main():
    # Load words from the uploaded file
    with open("words.txt", "r") as file:
        words = [line.strip() for line in file]

    hash_table_type = input("Enter hash table type (constant or length): ")
    if hash_table_type == "constant":
        hash_table = HashTableConstant(words)
    elif hash_table_type == "length":
        hash_table = HashTableLength(words, size=100)
    else:
        print("Invalid hash table type.")
        return

    word_needed = input("What word would you like to find? ")
    result = hash_table.get(word_needed)
    if result is None:
        print(f"The word '{word_needed}' is not found.")
    else:
        print(f"The word '{word_needed}' is found.")

if __name__ == "__main__":
    main()
