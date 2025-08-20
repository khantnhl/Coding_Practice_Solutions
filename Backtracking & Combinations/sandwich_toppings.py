def generateCombs(topping : list[str]):

    result = []
    def backtrack(path, index):
        # Base case 
        result.append(path[:])

        for i in range(index, len(topping)):
            path.append(topping[i])
            backtrack(path, i + 1)
            path.remove(topping[i])
    
    backtrack([], 0)
    return result

toppings = ["cheese", "ham", "tomato", "sausage"]
print(generateCombs(toppings))