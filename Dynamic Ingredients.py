currentInput = input("Enter the first ingredient: ")
ingredients = []
while currentInput != "END":
    ingredients.append(currentInput)
    currentInput = input("Enter new ingredients or END (stop adding): ")
print(ingredients)
