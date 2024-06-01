# Parallel File Processing: Create a program that processes multiple files simultaneously using multiprocessing.
# Each process should handle the processing of one file, such as counting words or extracting specific information.
import os
import multiprocessing

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Näiteks sõnade lugemine
            word_count = len(file.read().split())
            print(f"Fail: {file_path}, Sõnade arv: {word_count}")
    except Exception as e:
        print(f"Viga faili {file_path} töötlemisel: {e}")

def main():
    # Failide teed, mida töödelda
    file_paths = [
        "/Users/merlynmey/PycharmProjects/PythonEE23/Intermediate/Class 4/Tasks/Multithreading/file1.txt",
        "/Users/merlynmey/PycharmProjects/PythonEE23/Intermediate/Class 4/Tasks/Multithreading/file2.txt",
        "/Users/merlynmey/PycharmProjects/PythonEE23/Intermediate/Class 4/Tasks/Multithreading/file3.txt",
        # Lisa rohkem failiteid vajadusel
    ]

    # Loo protsesside bassein
    pool = multiprocessing.Pool()

    # Rakenda iga failitee kohta process_file funktsiooni
    pool.map(process_file, file_paths)

    # Sulge protsesside bassein
    pool.close()
    # Oota kõikide protsesside lõpetamist
    pool.join()

if __name__ == "__main__":
    main()
