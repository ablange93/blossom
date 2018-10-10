# HASH MAP #
class HashMap:
  # ARRAY 
  def __init__(self, size):
    self.array_size = size
    self.array = [None for i in range(size)]
    
  # HASH FUNCTION | Sum character encodings of each character.
  def hash(self, key):
    hash_code = sum(key.encode())
    
  # COMPRESSION FUNCTION
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  # SETTER
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    self.array[array_index] = [key, value]