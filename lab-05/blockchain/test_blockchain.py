from blockchain import Blockchain

def main():
    my_blockchain = Blockchain()

    my_blockchain.add_transaction("Tuan", "Hoang", 100)
    my_blockchain.add_transaction("Hoang", "Quynh Anh", 50)

    previous_block = my_blockchain.get_previous_block()
    previous_proof = previous_block.proof
    proof = my_blockchain.proof_of_work(previous_proof)
    previous_hash = previous_block.hash
    my_blockchain.create_block(proof, previous_hash)

    print("Blockchain hop le:", my_blockchain.is_chain_valid(my_blockchain.chain))

    for block in my_blockchain.chain:
        print(block.__dict__)

if __name__ == "__main__":
    main()