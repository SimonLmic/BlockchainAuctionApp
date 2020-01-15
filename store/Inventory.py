import numpy as np
import pandas as pd
import sqlite3

class InventoryStore():
   def __init__(self):
      self.conn = sqlite3.connect("example.db")
      self.c = self.conn.cursor()

   def load():
      return

   def top(self):
      tupleList = []
      # SQL top publishers
      for row in self.c.execute('SELECT * FROM publisher_stocks ORDER BY price limit 10'):
         tupleList.append(row)
      inventory = pd.DataFrame(tupleList)
      print(inventory)

   def view(self):
      tupleList = []
      # SQL store view
      for row in self.c.execute('SELECT * FROM publisher_stocks ORDER BY account'):
         tupleList.append(row)
      inventory = pd.DataFrame(tupleList)
      print(inventory)
