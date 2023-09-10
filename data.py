# from openpyxl import load_workbook
import os.path


def check_files(num):
    for i in range(1, num + 1):
        if not os.path.exists(f'decks\\cards{i}.xlsx'):
            return 1
    return 0


if __name__ == "__main__":
    userInput = int(input("Enter number: "))
    for j in range(1, userInput + 1):
        print(j)
