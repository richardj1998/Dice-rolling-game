
from rolled_function import rolled_function

print("Welcome to rolling dice application")

rolled_function()

while True:
    response = input("Do you want to roll again? Yes or No: ").lower()
    if response == "yes":
        rolled_function()
        continue

    else:
        break
print("Thanks for rolling with us")
