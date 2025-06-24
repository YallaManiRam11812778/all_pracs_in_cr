import hashlib

# Simulated storage for idempotency keys and results
idempotency_store = {}

def idempotent_api(idempotency_key, payload):
    # Generate a hash of the payload for validation
    payload_hash = hashlib.sha256(str(payload).encode()).hexdigest()
    print("payload_hash ============ ",payload_hash, "\npaylod is ===============",payload)
    if idempotency_key in idempotency_store:
        # Check if the payload matches the stored request
        stored_payload_hash, result = idempotency_store[idempotency_key]
        if payload_hash != stored_payload_hash:
            return {"error": "Payload mismatch for this idempotency key"}
        return {"status": "Success", "data": result, "message": "Reused result"}
    
    # Process the request (simulate creating a new resource)
    result = f"Resource created with payload: {payload}"
    # Store the idempotency key with payload hash and result
    idempotency_store[idempotency_key] = (payload_hash, result)
    
    return {"status": "Success", "data": result, "message": "Processed request"}

# Example usage
print(idempotent_api("key123", {"amount": '[100,200]'}),"\n\n")
print(idempotent_api("key123", {"amount": '[100,200]'}),"\n\n")  # Reuses result
print(idempotent_api("key123", {"amount": '[200,100]'}),"\n\n")  # Error: Payload mismatch
print("\n\n\n",idempotency_store,">"*100)
