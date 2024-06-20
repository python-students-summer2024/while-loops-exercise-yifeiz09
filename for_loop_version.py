
def get_starting_number():
    while True:
        try:
            number = int(input("How many bottles of beer on the wall? "))
            if number >= 1:
                return number
        except ValueError:
            pass
        print("Please enter a valid integer 1 or greater.")

def sing(starting_bottles):
    for bottles in range(starting_bottles, 0, -1):
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("Take one down and pass it around, " + ("no more" if bottles-1 == 0 else str(bottles-1)) + " bottles of beer on the wall.")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, no more bottles of beer on the wall.")

if __name__ == "__main__":
    starting_bottles = get_starting_number()
    sing(starting_bottles)
