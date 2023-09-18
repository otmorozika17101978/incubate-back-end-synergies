
def generate_random_data():
    random_string = 'Table since sport partner.'
    random_number = 49

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Table since sport partner.")
        print(f"Random Number: 49")

if __name__ == "__main__":
    main()
