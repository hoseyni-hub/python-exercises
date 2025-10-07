# Task: Create a program that writes a list of names to a file, 
# then reads the file and prints the contents.

def write_names_to_file(filename, names):
    with open(filename, "w") as f:
        for name in names:
            f.write(name + "\n")

def read_names_from_file(filename):
    with open(filename, "r") as f:
        return f.readlines()

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "Diana"]
    file = "names.txt"

    write_names_to_file(file, names)
    content = read_names_from_file(file)

    print("File content:")
    for line in content:
        print(line.strip())
