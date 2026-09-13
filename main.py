phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

user_input = input("Enter the phone number: ")

if not user_input.isdigit() or len(user_input) != 10:
    print("This is invalid number")
elif user_input in phone_book:
    print(f"The owner is: {phone_book[user_input]}")
else:
    print("Sorry, the number is not found")
