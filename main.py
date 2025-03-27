import json
import os
import random
from faker import Faker

fake = Faker()
os.makedirs("output", exist_ok=True)

def maybe_null(generator_func):
    """Return a value from generator_func or None randomly."""
    return generator_func() if random.choice([True, False]) else None

def generate_user():
    return {
        "id": maybe_null(fake.uuid4),
        "name": maybe_null(fake.name),
        "address": maybe_null(fake.address),
        "email": maybe_null(fake.email),
        "birthdate": maybe_null(lambda: fake.date_of_birth().isoformat())
    }

if __name__ == "__main__":
    users = [generate_user() for _ in range(10)]
    with open("output/users.json", "w") as f:
        json.dump(users, f, indent=2)
    print("Generated users.json at output/users.json")
