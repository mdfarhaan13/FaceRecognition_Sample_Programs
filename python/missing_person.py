class MissingPerson:
    def __init__(self, name, age, last_seen):
        self.name = name
        self.age = age
        self.last_seen = last_seen

    def display_details(self):
        print("Missing Person Details")
        print("----------------------")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Last Seen  : {self.last_seen}")


if __name__ == "__main__":
    person = MissingPerson(
        name="Arun Kumar",
        age=28,
        last_seen="Chennai Railway Station"
    )

    person.display_details()
