import hashlib
import time

class StructuralBlock:
    def __init__(self, index, record_payload, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.payload = record_payload
        self.previous_hash = previous_hash
        self.hash = self.compute_signature()
        self.next = None  # Pointer to upcoming link node
        self.prev = None  # Pointer to preceding link node

    def compute_signature(self):
        raw_map = f"{self.index}{self.timestamp}{self.payload}{self.previous_hash}"
        return hashlib.sha256(raw_map.encode()).hexdigest()
