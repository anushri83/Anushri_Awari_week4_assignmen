
# Write a program that reads a text file, counts the number of lines, words, and characters, and
# writes the results to a new file.

def count_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:   # open and read from file
            content = file.readlines()        #stores text line by line

            num_lines = len(content)
            num_words = sum(len(line.split()) for line in content)
            num_chars = sum(len(line) for line in content)


        with open(output_file, 'w') as file:     #open and write in file
            file.write(f"Number of lines: {num_lines}\n")
            file.write(f"Number of words: {num_words}\n")
            file.write(f"Number of characters: {num_chars}\n")
        print(f"Results have been written to {output_file} successfully.")


    except FileNotFoundError:     #error          
        print(f"The file {input_file} was not found.")


input_file = r"C:\Users\admin\Downloads\python\cogitix\week4\task_1\input_file.txt"   #input file address
output_file = r"C:\Users\admin\Downloads\python\cogitix\week4\task_1\output_file.txt" #output file address

count_file(input_file, output_file)

