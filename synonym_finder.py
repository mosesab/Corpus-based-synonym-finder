
'''
synonym_finder.py
version : 1.0
Author : Bankole Moses

requirements.txt : None
CrossPlatform Support : True
Date: June 29, 2021.
Tested on Android, Windows, Linux using python 3.8.3
All libraries used are part of the standard python library of python 3.8.3
'''


import re
import unicodedata
import os 
from sentence_tokenizer import find_sentences

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
    
def strip_digitsAndSpecialChars(text):
    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = re.sub('[ ]+', ' ', text)
    #substitute values that aren't letters,numbers,underscore or dot
    text = re.sub('[^0-9a-zA-Z_.]', ' ', text)
    # seperate dot from text by adding whitespace to it
    text =  re.sub('[.]', ' . ', text)
    #substitute digits with whitespace
    text =  re.sub('[0-9]', ' ', text)
    #substitute single letter words with white_space
    text = re.sub(r'(?:^| )\w(?:$| )', ' ', text)

    return text
    

def clean_text(text):
    """
    Applies all the filters to input text.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :return type: String.
    """
    text = text.lower()
    text = strip_accents(text)
    text = strip_digitsAndSpecialChars(text)
      
    return text

def create_sentence_list(file_path, count = 0):
	"""
    cleans text and tokenizes the text into 
    a list of sentences(string)

    :param text: The filepath to the corpus.
    :type text: String.

    :returns: A list of sentences(strings)
    that have been cleaned
    :return type: list.
	"""
	my_word_list = []	
	# Read text File
	with open(file_path, 'r',encoding = 'utf-8') as fd: 
		input_str = str(fd.read())
		fd.close()		
	#removes diacritics and cleans text data
	string = clean_text(input_str)	
	return find_sentences(string)
	
		
def get_target_sentences(target_word,corpus_sentence_list):
	#sentence_index is used to know the original sentence equivalent of a corpus_sentence_list element
	target_word = target_word.lower()
	sentence_index = 0
	target_sentences_list = []
	# score each sentence in corpus_sentence_list and 
	#write it's original corpus sentence equivalent to a text file based on its score.		
	for sentence in corpus_sentence_list:
		word_exists = 0
		sentence_length = 0
		
		for word in sentence.split():
			sentence_length += 1
			if word == target_word:
				word_exists += 1
				target_sentences_list.append(corpus_sentence_list[sentence_index])
		sentence_index += 1
	return target_sentences_list
	
def get_words_surronding_target_word(target_word,target_sentences_list):
	before_target_word_list = []
	after_target_word_list = []
	
	for sentence in target_sentences_list:
		#split sentence string into  substrings before_keyword, keyword, after_keyword 	
		before_keyword, temp_keyword, after_keyword = sentence.partition(target_word)
		
		#pick the first two words b4 keyword
		b_list = before_keyword.split()
		if len(b_list) > 1:
			b_string = '' + b_list[-2]+' '+b_list[-1]
		elif len(b_list) == 1:
			b_string = '' + b_list[-1]
		else:
			print("Null Error: A sentence in before_target_word_list is empty")
				
		before_target_word_list.append(b_string)
		
		#pick the first two words after keyword
		a_list = before_keyword.split()
		if len(a_list) > 1:
			a_string = '' + a_list[-2]+' '+a_list[-1]
		elif len(b_list) == 1:
			a_string = '' + a_list[-1]
		else:
			print("Null Error: A phrase in after_target_word_list is empty")
		
		after_target_word_list.append(a_string)		
		break
		
	return before_target_word_list , after_target_word_list
	
def search_for_synonyms(before_target_word_list, after_target_word_list, corpus_sentence_list):
	synonym_word_list = []
	surronding_words_list = []
	#get all the words in the corpus that are in the same sentence with surronding words  
	
	for sentence in corpus_sentence_list:
		word_list = sentence.split()		
		for phrase in before_target_word_list:				
			#get word after phrase
			#append word to synonym_word_list				
			if phrase in sentence:
					before_phrase, temp_phrase, after_phrase = sentence.partition(phrase)
					#pick the first word after phrase
					s_list = after_phrase.split()
					if len(s_list) > 1:
						possible_synonym = '' + s_list[-1]
						synonym_word_list.append(possible_synonym)
					#else:
						#print("Null Warning: after_phrase in sentence is empty")
							
					
		for phrase_ in after_target_word_list:				
			#get word before phrase
			#append word to synonym_word_list				
			if phrase_ in sentence:
					before_phrase, temp_phrase, after_phrase = sentence.partition(phrase_)
					#pick the first word before phrase
					s_list2 = before_phrase.split()
					if len(s_list2) > 1:
						possible_synonym2 = '' + s_list2[-1]
						synonym_word_list.append(possible_synonym2)
					#else:
						#print("Null Warning: before_phrase in sentence is empty")
							
					
					surronding_words_list.extend(s_list)
					surronding_words_list.extend(s_list2)				
	
	#remove duplicates from surronding_words_list
	surronding_words_list = list(set(surronding_words_list))

	temp_synonym_word_list = []
	temp_synonym_word_list.extend(synonym_word_list)		
	
	#remove surronding words from the synonym list
	temp_synonym_word_list = [i for i in temp_synonym_word_list if i not in surronding_words_list]
	#if after removing surronding words temp_synonym_word_list is empty, return synonym_word_list with surronding words
	if len(temp_synonym_word_list) < 1:
		print("\n Info: Larger corpus files provide more Accuracy but less speed\n")
		return synonym_word_list
	else:
		print("\n Info: Synonym search completed successfully\n")
		
	return temp_synonym_word_list
 
def start_work(corpus_word_list):	
	
		#Enter the target word without diacritics
		target_word = input("Enter the target word: ")
		
		target_sentences = get_target_sentences(target_word,corpus_word_list)
		before_target_word_list , after_target_word_list = get_words_surronding_target_word(target_word,target_sentences)
		
		synonym_word_list = search_for_synonyms(before_target_word_list, after_target_word_list, corpus_word_list)

		print("Available Words: \n", synonym_word_list)
		print("\n \n ")
		
		quit = input("Do you want to quit, Y, N: ")
		quit = quit.lower()
		if quit == 'n':
			start_work(corpus_word_list)
		elif quit == 'y':
			pass
		else:
			print("ERROR: Invalid Selection")
		

	
print("Corpus-Based Synonym Finder \n")

#filenames must include .txt
corpus_words_txt = "Yoruba_corpus.txt"	# corpus word count = 41398


# Check whether file is in text format or not
if corpus_words_txt.endswith(".txt"):
	print("Loading: Pre-processing the  Corpus... Please Wait \n")
	filepath = os.path.join(os.getcwd(), corpus_words_txt)		
	 
	corpus_word_list = create_sentence_list(filepath)
else:
		print("ERROR: .txt is missing from the corpus file name")
		
	
if corpus_words_txt == "Yoruba_corpus.txt":
	print('''You can try yoruba words like: "owo", "iku", "gba"  ''')

start_work(corpus_word_list)