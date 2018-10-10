# HASH MAP #
class HashMap:
  # ARRAY 
  def __init__(self, size):
    self.array_size = size
    self.array = [None for i in range(size)]
    
  # HASH FUNCTION | Sum character encodings of each character.
  def hash(self, key):
    hash_code = sum(key.encode())