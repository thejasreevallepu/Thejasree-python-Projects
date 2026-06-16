import os

try:
    folder = input("Enter folder path: ")

    files = os.listdir(folder)

    print("\nDocuments Found:")

    for file in files:
        print(file)

    print("\nCompleted Successfully")

except Exception as e:
    print("Error:", e)