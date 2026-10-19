items = {}


with open("exp_trac.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        food_, price = line.split(",")
        items[str(food_)] = int(price)
print(items)
x = input("add,delete,view,total: ").lower().rstrip()


def add(food, cost):
    with open("exp_trac.txt", "a") as file:
        file.write(f"{food},{cost}\n")
        items[food] = int(cost)

def delete(food):
    cost = items[food]
    to_remove = f"{food},{cost}\n"
    with open("exp_trac.txt", "r") as file:
        lines = file.readlines()
        lines.remove(to_remove)
    with open("exp_trac.txt", "w") as file:
        file.writelines(lines)
    items.pop(food)


def view():
    print(items)


def total():
    x = 0
    for costs in items.values():
        x += costs
    return x


if x == "add":
    food = input("food: ")
    cost = input("cost: ")
    add(food, cost)
elif x == "delete":
    delete_ = input("food: ")
    delete(delete_)
elif x == "total":
    print(total())
elif x == "view":
    for x, y in items.items():
        print(f"{x} - ₹{y}")
