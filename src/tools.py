import pickle
import os
import datetime

def pick(filename, data):
    # Если filename не содержит пути, добавляем директорию conversation
    if not os.path.dirname(filename):
        filename = os.path.join("conversation", filename)
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def unpick(filename):
    # Если filename не содержит пути, добавляем директорию conversation
    if not os.path.dirname(filename):
        filename = os.path.join("conversation", filename)
    with open(filename, 'rb') as f:
        return pickle.load(f)



