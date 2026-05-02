import os
import json
import random
import string
class FileUtility:
 def __init__(self, directory):
  self.directory = directory
 def create_file(self, filename, content):
  with open(os.path.join(self.directory, filename), 'w') as f:
   f.write(content)
 def read_file(self, filename):
  with open(os.path.join(self.directory, filename), 'r') as f:
   return f.read()
 def delete_file(self, filename):
  os.remove(os.path.join(self.directory, filename))
 def list_files(self):
  return os.listdir(self.directory)
 def generate_random_string(self, length):
  letters = string.ascii_letters
  return ''.join(random.choice(letters) for i in range(length))
 def create_multiple_files(self, count):
  for i in range(count):
   filename = self.generate_random_string(10) + '.txt'
   content = self.generate_random_string(50)
   self.create_file(filename, content)
 def save_to_json(self, filename, data):
  with open(os.path.join(self.directory, filename), 'w') as f:
   json.dump(data, f)
 def load_from_json(self, filename):
  with open(os.path.join(self.directory, filename), 'r') as f:
   return json.load(f)
 def count_files(self):
  return len(self.list_files())
 def clear_directory(self):
  for filename in self.list_files():
   self.delete_file(filename)
 def get_file_size(self, filename):
  return os.path.getsize(os.path.join(self.directory, filename))
