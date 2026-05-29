# program to stores and searches contacts.

contacts = [
    {
        "name": "Aryan",
        "phone": "9876543210",
        "email": "alex@gmail.com"
    },
    {
        "name": "Raj",
        "phone": "9123456780",
        "email": "riya@gmail.com"
    },
    {
        "name": "Rahul",
        "phone": "9988776655",
        "email": "rahul@gmail.com"
    },
    {
        "name": "Ashok",
        "phone": "9090909090",
        "email": "sneha@gmail.com"
    },
    {
        "name": "Kumar",
        "phone": "8888888888",
        "email": "kunal@gmail.com"
    }
]


def find_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return "Contact not found."


search_name = input("Enter contact name: ")

result = find_contact(search_name)

print(result)
