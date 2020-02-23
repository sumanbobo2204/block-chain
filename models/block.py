import json
from hashlib import sha256


class Block(object):
    def __init__(self, index, transactions, created_at, previous_hash):
        self.index = index
        self.transactions = transactions
        self.created_at = created_at
        self.previous_hash = previous_hash

    def get_hash(self):
        block_str = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_str.encode()).hexdigest()
