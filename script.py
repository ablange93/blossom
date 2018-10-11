from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

# HASH MAP #
class HashMap:
  # ARRAY 
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
    
  # HASH FUNCTION | Sum character encodings of each character.
  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  # COMPRESSION FUNCTION
  def compress(self, hash_code):
    return hash_code % self.array_size
    
  # SETTER
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    
    #Check each node in an array's linked list
    for node in list_at_array:
      
      # If a key matches then overwrite value
      if node[0] == key:
        node[1] = value
    
    # If no key matches then add key-value
    list_at_array.insert(payload)
        
  # GETTER
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    
    for node in list_at_index:
      if node[0] == key:
        return node[1]
      else:
        return None

    if payload is not None:
      if payload[0] == key:
        return payload[2]
      
# MAIN #
print("Creating Hash Map...")
blossom = HashMap(len(flower_definitions))
print("Hash Map sucessfully created.")

blossom.assign('begonia', 'cautiousness')
print(blossom.retrieve('begonia'))