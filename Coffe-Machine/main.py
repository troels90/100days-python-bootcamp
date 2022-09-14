import functions

turned_on = True

while turned_on:
        answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if answer == "report":
            functions.report_resources()
        elif answer == "espresso" or answer == "latte" or answer == "cappuccino":
            sufficient = functions.sufficient_resources(answer)

            if sufficient == "yes":
                cost = functions.get_cost(answer)
                print(f"{answer} costs ${cost}")
                print(" - Please insert Coins -" )
                inserted = functions.input_coins()
                change = inserted - cost

                if change >= 0:
                    print(f"You inserted ${inserted}. Here is ${change} in change")
                    print(f"Here is your {answer} - Enjoy!")
                    functions.update_resources(answer)
                    functions.update_money(change, inserted)
                else:
                    print("Need more money! Start from scratch")

            else:
                print(sufficient)

        elif answer == "off":
            turned_on = False
            print("No more coffee for you")

        else:
            print("Wrong input, Try again")