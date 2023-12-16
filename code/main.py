import os
import time

# import the functions from the utils file
from utils import read_grammar_from_file,generate_sentence,append_to_file

if __name__ == '__main__':
  # To calculate execution time of program
	start_time = time.perf_counter()

	# specifying the pathname for parsing grammer file
	file_name = 'grammar.gr'
	# managing the path for gr file using os module 
	file_path = os.path.join(os.getcwd(),file_name)
	# calling function to get the grammer in python dictionary 
	grammar = read_grammar_from_file(file_path)

	# specifying filename for saving the generated sentences
	save_file_name = 'gen_sentences.txt'
	# loop to generate 10,000 students  
	for i in range(10000):
		append_to_file(save_file_name, generate_sentence(grammar))
		

	end_time = time.perf_counter()
	# calculation and display of total execution time
	execution_time = end_time - start_time
	print(f"Time taken : {execution_time:.4f} seconds")