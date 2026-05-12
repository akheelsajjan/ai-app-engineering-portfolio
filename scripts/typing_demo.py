from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    is_active: bool


def create_user(name: str, age: int) -> User:
    return {
        "name": name,
        "age": age,
        "is_active": True,
    }


def main():
    user = create_user("Akheel", 28)

    print(user)
    print(user["name"])


if __name__ == "__main__":
    main()