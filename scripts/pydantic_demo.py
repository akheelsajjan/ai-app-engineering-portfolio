from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    is_active: bool = True


def main():
    user = User(
        name="Akheel",
        age="s",
    )

    print(user)
    print(type(user.age))


if __name__ == "__main__":
    main()