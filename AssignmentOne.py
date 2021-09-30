def main():
    print("Please select color of your shirt!")
    print("1: Black\n2: Blue\n3: Violet\n4: Neon")
            # Validate that the choice made is correct
    while True:
        try:
            color = int(input("Enter your choice: "))
            break
        except:
            print("That's not a valid option!")

    if color == 1 or color == 2 or color == 3 or color == 4:
        print("Please pick your choice of between polo shirt or t-shirt")
        print("1: Polo Shirt\n2: T-Shirt")
            # Validate that the choice made is correct
        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except:
                print("Invalid type of shirt")

        else:
            print("Invalid choice picked.")
    else:
        print("Invalid color selected.")


# To Execute the main function
if __name__ == "__main__":
    main()