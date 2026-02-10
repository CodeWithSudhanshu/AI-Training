items = []

n = int(input("Enter number of items to add for picnic: "))

for i in range(n):
    item = input(f"Enter item {i+1}: ")
    items.append(item)

choice = input("Do you want to remove any item? (yes/no): ").lower()

if choice == "yes":
    remove_item = input("Enter item name to remove: ")
    if remove_item in items:
        items.remove(remove_item)
        print(f"{remove_item} removed successfully.")
    else:
        print("Item not found in the list.")

print("\nFinal Picnic Item List:")
print(items)