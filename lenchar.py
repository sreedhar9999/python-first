def main():
    full_name = input("Please enter in a full name: ").split()
    t = 0
    for x in full_name:
        t += len(x)
    print(t)
