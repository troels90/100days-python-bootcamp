import data

def report_resources():
    money = data.money
    for res in data.resources:
        amount = data.resources[res]
        type = ""
        if res == "water" or res == "milk":
            type += "ml"
        else:
            type += "g"
        print(f"{res}: {amount}{type}."  )
    print(f"Money: ${money}")


def sufficient_resources(coffee):
    sufficient = ""
    for res in data.MENU[coffee]["ingredients"]:
        req_res = data.MENU[coffee]["ingredients"][res]
        if req_res >= data.resources[res]:
            sufficient += f"Not enough {res}"
            return sufficient
    sufficient = "yes"
    return sufficient


def get_cost(coffee):
    cost = data.MENU[coffee]["cost"]
    return cost


def input_coins():
    quarter = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many dimes? "))
    pennies = int(input("How many dimes? "))
    inserted = round(quarter*0.25
                     + dimes * 0.10
                     + nickles * 0.05
                     + pennies * 0.01,
                     2)
    return inserted


def update_resources(coffee):
    for i in data.MENU[coffee]["ingredients"]:
        value = data.resources[i] - data.MENU[coffee]["ingredients"][i]
        data.resources[i] = value


def update_money(change, inserted):
    data.money += (inserted - change)
