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
    bottles = starting_bottles
    continue_singing = True
    while continue_singing:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print("Take one down and pass it around, " + ("no more" if bottles-1 == 0 else str(bottles-1)) + " bottles of beer on the wall.")
        bottles -= 1
        if bottles == 0:
            continue_singing = False
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, no more bottles of beer on the wall.")

if __name__ == "__main__":
    starting_bottles = get_starting_number()
    sing(starting_bottles)