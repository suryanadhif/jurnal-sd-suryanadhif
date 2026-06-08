import random

users = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "User"}
]

def get_users():

    random_number = random.randint(1, 5)

    if random_number == 1:
        return {
            "status": "error",
            "message": "Server sedang sibuk. Silakan coba lagi."
        }

    return {
        "status": "success",
        "data": users
    }