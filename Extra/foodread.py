foodList = []

# Open the file in read mode
with open('foods.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    # Split the content by newline character to get each line
    lines = content.split('\n')
    
    # Initialize an empty list to store pairs of integers
    
    
    # Iterate through each line in the file
    for line in lines:
        # Split each line by comma and space to get pairs of integers
        pair = line.split(', ')
        # Convert each element in the pair to integer and append to foodList
        foodList.append((int(pair[0]), int(pair[1])))

# Print the list of pairs of integers
print("Food List:", foodList)
