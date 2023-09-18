
def generate_random_data():
    random_string = 'Owner pressure opportunity traditional fine.'
    random_number = 9

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Owner pressure opportunity traditional fine.")
        print(f"Random Number: 9")

if __name__ == "__main__":
    main()
