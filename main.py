import json
import os
import random
from faker import Faker

fake = Faker()
os.makedirs("output", exist_ok=True)

FIELDS = [
    ("email", fake.email),
    ("birthdate", lambda: fake.date_of_birth().isoformat())
]

def generate_user():
    user = {
        "id": fake.uuid4(),
        "name": fake.name(),
        "address": fake.address()
    }
    for field, func in FIELDS:
        user[field] = func() if random.choice([True, False]) else None
    return user

if __name__ == "__main__":
    users = [generate_user() for _ in range(10)]
    with open("output/users.json", "w") as f:
        json.dump(users, f, indent=2)
    print("Generated users.json at output/users.json")