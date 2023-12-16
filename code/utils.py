import random

# function to check whether the string is terminal,preterminals, or non terminals
# - we need to stop the recursion if we reach to terminal words
# - terminal words have each first letter of word lowercase Eg. chief of staff
def check_terminals(str):
  word_list = str.split(' ')
  # logic to check if first letter of words is lowercase or not
  # if all not upper => it is terminal words
  return not all(word[0].isupper() for word in word_list)



# function to read 
def read_grammar_from_file(file_path):
    # empty dictionary to store formatted result
    grammar_dict = {}
    with open(file_path, 'r') as file:
        # opening file and iterating through each line
        for line in file:
            list = line.strip().split("\t")
            # split the line by tab and only check ones with length 3 (3 words)
            if len(list) ==3:
                # destructure symbol and its respective values
                _, symbol, *productions = list
                
                if symbol != 'ROOT':
                    # skip symbool ROOT
                    # check if values are terminal words or not
                    # if terminal words like chief of staff we insert data as it is.
                    # else we split them into list like NP VP 
                    productions = productions[0] if check_terminals(productions[0]) else productions[0].split(" ")
                    # store result in list even for string
                    productions = productions if len(productions) == 1 else [productions]
                    # condition check if symbol is already in dictionary or not
                    if symbol in grammar_dict:
                        grammar_dict[symbol] += productions 
                    else:
                        grammar_dict[symbol] = productions 
    return grammar_dict


# function to remove nested nested non terminal words,to avoid long sentences.
def remove_nested_list(input_dict):
  # empty dictionary to store result
	result_dict = {}

	for key, value in input_dict.items():
		arr = []
    # iterate through each value to find nested values
		for i in value:
				if not isinstance(i, list):
						arr.append(i)
				else:
            # insert list into dictionary only if there is no nested value
            # nested value check => if key exists in list
						isNested = any(item == key for item in i)
						if not isNested:
								arr.append(i)

		result_dict[key] = arr
	return result_dict


# recusive function to generate sentence
# concept of depth used to avoid long sentences. 
def generate_sentence(grammar, symbol='S', depth=0, max_depth=4):
    # base condition to return word if it is terminal
    if check_terminals(symbol):
        return symbol   
    else:
        # filter out terminal words
        filtered_symbols = [item for item in grammar[symbol] if not isinstance(item, list)]
        if depth >= max_depth: 
            # if max depth achieved go for terminal words
            if len(filtered_symbols) != 0:
                return random.choice(filtered_symbols) + ' '
            # else call the function to generate sentence without nested grammer.
            else:
                return gen_from_grammar(remove_nested_list(grammar),symbol,depth,max_depth)
        else:
            # call the function to get into terminal words
            return gen_from_grammar(grammar,symbol,depth,max_depth)


# function to generate function sentence from given grammer
def gen_from_grammar(grammar,symbol,depth,max_depth):
    production = random.choice(grammar[symbol])
    sentence = ''
    # loop through the list of non terminal grammer to get into terminal
    if isinstance(production, list):
        for i in production:
            sentence += generate_sentence(grammar,i, depth + 1, max_depth)
    # get the terminal via current symbol
    else:
        sentence += generate_sentence(grammar,production, depth + 1, max_depth) + " "
    return sentence

# function to write the generated sentence into file.
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')