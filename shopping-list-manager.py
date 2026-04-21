# create an empty list
shopping_items = []

# define menu
def shopping_menu():
    print("\n1. Show all items")
    print("2. Add new item")
    print("3. Delete an item")
    print("4. Clear all items")
    print("5. Quit\n")

while True:
    shopping_menu()
    choice_number = int(input("What is your choice number:\n"))

    if choice_number == 1:
        print("\nShopping Items:\n")
        if not shopping_items:
            print("No items to show\n")
        else:
            for index, item in enumerate(shopping_items, start=1):
                print(f"{index}. {item}")

    elif choice_number == 2:
        new_item = input("\nEnter item to add:\n")
        shopping_items.append(new_item)
        print(f"{new_item} is added to the shopping list\n")

    elif choice_number == 3:
        delete_item = input("\nEnter item you want to delete:\n")
        if delete_item in shopping_items:
            shopping_items.remove(delete_item)
            print(f"{delete_item} is removed from the shopping list\n")
        else:
            print(f"{delete_item} not found in shopping list\n")

    elif choice_number == 4:
        shopping_items.clear()
        print("All items are cleared\n")

    elif choice_number == 5:
        print("Goodbye!")
        break

    else:
        print("Please enter a valid choice\n")