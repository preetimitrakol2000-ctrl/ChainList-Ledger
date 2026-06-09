from ledger_chain import DoublyLinkedLedger

if __name__ == "__main__":
    print("⛓️  Assembling ChainList-Ledger Bidirectional Framework...")
    
    blockchain_ledger = DoublyLinkedLedger()
    blockchain_ledger.append_record("Block_01: User_Alpha mints 50 tokens")
    blockchain_ledger.append_record("Block_02: User_Beta stakes 20 tokens")
    
    print(f"📦 Head Ledger Signature Block: {blockchain_ledger.head.hash[:20]}...")
    print(f"📦 Tail Ledger Signature Block: {blockchain_ledger.tail.hash[:20]}...")
    
    is_valid = blockchain_ledger.verify_bidirectional_integrity()
    print(f"\n🔍 Bidirectional Node Integrity Verification Step: { 'PASSED ✅' if is_valid else 'FAILED 🚨' }")
