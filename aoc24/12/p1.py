def main(document):
    areas = {}
    for lime in document:
        pass
        

if __name__ == "__main__":
    with open("test.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)