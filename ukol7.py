def is_adult(age):
    return age >= 18

def is_name_valid(username):
    return len(username) >= 4

def create_user(username, age, email):
    if not is_adult(age):
        return {
            "success": False,
            "error": "Uživatel musí být starší 18 let."
        }

    if not is_name_valid(username):
        return {
            "success": False,
            "error": "Uživatelské jméno musí mít nejméně 4 znaky."
        }

    return {
        "success": True,
        "user": {"username": username, "age": age, "email": email}
    }

def print_user_info(result):
    if result["success"]:
        user = result["user"]
        print("Uživatel je vytvořen:")
        print(f" Jméno: {user['username']}")
        print(f" Věk: {user['age']}")
        print(f" Email: {user['email']}")
    else:
        print("Chybová zpráva: ", result["error"])

users = [
    create_user("David", 22, "david@seznam.cz"),
    create_user("Martina", 17, "martina@gmail.com"),
    create_user("Zoe",  35, "zoe@email.cz"),
    create_user("Pavel",  22, "pavel@email.cz")
]
for user in users:
    print_user_info(user)
    print("-" * 40)