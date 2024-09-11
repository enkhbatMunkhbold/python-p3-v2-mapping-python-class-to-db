# lib/config.py
import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

# CONN.close()

# import os
# os.remove('company.db')
