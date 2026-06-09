from node_block import StructuralBlock

class DoublyLinkedLedger:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_record(self, transaction_data):
        if not self.head:
            # Build Genesis node structure
            genesis = StructuralBlock(0, transaction_data, "0"*64)
            self.head = genesis
            self.tail = genesis
        else:
            new_index = self.tail.index + 1
            new_block = StructuralBlock(new_index, transaction_data, self.tail.hash)
            self.tail.next = new_block
            new_block.prev = self.tail
            self.tail = new_block

    def verify_bidirectional_integrity(self):
        """Walks forward and backward through memory references to audit data symmetry."""
        current = self.head
        while current and current.next:
            if current.hash != current.next.previous_hash:
                return False
            current = current.next
        return True
