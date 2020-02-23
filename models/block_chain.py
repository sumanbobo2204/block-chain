import time
from .block import Block


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self._init_head()

    def add_block(self, block):
        # TODO : add proof of work implementation
        self.chain.append(block)

    @property
    def last_block(self):
        return self.chain[-1]

    def _init_head(self):
        self.head = Block(0, [], time.time(), None)
        self.head.hash = self.head.get_hash()
        self.chain.append(self.head)
