import operator
import itertools


def display_inventory(inventory):
    """Display the inventory"""
    print("Inventory:")
    for key,val in inventory.items():
        print(key, val)
    print("Total number of items:", sum(inventory.values()))


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items"""
    for i in added_items:
        if i not in inventory:
            inventory[i] = 0
        inventory[i] += 1
    return inventory


def print_table(inventory, order):
    """Take the inventory and display it in a well-organized table"""
    if order == "count,asc":
        inventory = sorted(inventory.items(), key=operator.itemgetter(1))
    elif order == "count,desc":
        inventory = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)

    longest_item = max(len(item[0]) for item in inventory)
    print("Inventory:")
    print('{:>7}  {:>{width}}'.format("count", "item name", width = longest_item + 2))
    print("-"*(longest_item + 11))
    for item in inventory:
        print('{:>7}  {:>{width}}'.format(item[1], item[0], width = longest_item + 2))
    print("-"*(longest_item + 11))
    count_items = []
    for item in inventory:
        count_items.append(item[1])
    sum_items = sum(count_items)
    print("Total number of items:", sum_items)


def import_inventory(inventory, filename):
    """Import new inventory items from a file"""
    with open(filename, "r") as f:
        items_f = [word.strip() for line in f.readlines() for word in line.split(",") if word.strip()]
    for i in items_f:
        if i not in inventory:
            inventory[i] = 0
        inventory[i] += 1
    return inventory


def export_inventory(inventory, filename):
    """Export the inventory into a .csv file"""
    with open (filename, "w") as f:
        for i in inventory:
            f.write("%s," %i*inventory[i])


def main():
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    print()
    display_inventory(inv)
    inv = add_to_inventory(inv, dragon_loot)
    print()
    display_inventory(inv)
    print()
    print_table(inv, "count,asc")
    print()
    print_table(inv, "count,desc")
    import_inventory(inv, "import_inventory.csv")
    print()
    print_table(inv, "count,asc")
    export_inventory(inv, "export_inventory.csv")


if __name__ == '__main__':
    main()
