
import sys


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    inventory: dict[str, int] = {}
    args = sys.argv[1:]
    for arg in args:
        arg_pair = arg.split(":")
        if len(arg_pair) != 2:
            print(f"Error - Invalid parameter '{arg}'")
            continue
        if arg_pair[0] in inventory:
            print(f"Redundant item '{arg_pair[0]}' - discarding")
            continue
        try:
            quantity = int(arg_pair[1])
        except ValueError as error:
            print(f"Quantity error for '{arg_pair[0]}': {error}")
            continue
        inventory[arg_pair[0]] = quantity
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory)}")
    item_sum = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {item_sum}")

    if len(inventory):
        most_item: str = ""
        least_item: str = ""
        for item in inventory:
            print(f"Item {item} represents ", end="")
            print(f"{round((inventory[item] * 100) / item_sum, 1)}%")
            if most_item == "" or inventory[most_item] < inventory[item]:
                most_item = item
            if least_item == "" or inventory[least_item] > inventory[item]:
                least_item = item
        print(f"Item most abundant: {most_item} ", end="")
        print(f"with quantity {inventory[most_item]}")

        print(f"Item least abundant: {least_item} ", end="")
        print(f"with quantity {inventory[least_item]}")

        inventory["magic_item"] = 1
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
