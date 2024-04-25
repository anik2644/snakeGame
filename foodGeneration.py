import random

# Function to generate random coordinates
def generate_random_coordinates(num_points):
    coordinates = [(random.randint(-450, 450), random.randint(-350, 350)) for _ in range(num_points)]
    return coordinates

# Function to save coordinates to a text file
def save_coordinates_to_file(coordinates, filename):
    with open(filename, 'w') as file:
        for coordinate in coordinates:
            file.write(f"{coordinate[0]}, {coordinate[1]}\n")

# Main function
def main():
    num_points = 100
    coordinates = generate_random_coordinates(num_points)
    save_coordinates_to_file(coordinates, "foods.txt")
    print(f"{num_points} random coordinates saved to foods.txt")

# Call the main function
if __name__ == "__main__":
    main()
