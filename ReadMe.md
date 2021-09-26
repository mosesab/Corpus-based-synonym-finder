
# Corpus-based-synonym-finder ReadMe

[![Repo visits](https://github-visit-counter.herokuapp.com/mosesab/Corpus-based-synonym-finder/visits.svg)](#)

### 👩‍💻 Project BreakDown
The Corpus-based Synonym Finder illustrates a principle of Natural Language Processing, it shows that a computer can estimate the meaning
of words in a language without an inherent understanding of that language. 



### 🔦 How the Code Works

* The code works by searching for how the target word is used in a sentence,
* The code finds other words (synonyms) that were used in similar context, 
* The accuracy and speed of execution of the synonym finder code is dependent on the size of the corpus file.  




### 🧪 How to Run the Code

 The synonym*finder.py is the python file that should be run when testing the code. 
 For the code to run ensure that the corpus text file is in the same folder as the code.
 
 

### 📝 How To change the Corpus-based Synonym Finder's language: 
1. Move a corpus text file of the language of choice into the Synonym Finder Folder 
2. Feed the corpus_words_txt (around line 235) variable the name of the corpus(must include .txt) 
3. Note that the larger the corpus word count,the higher the accuracy and the slower the speed of execution



### 📔 Note
 <ul>
	<li> The create_sentence_list function splits the whole corpus into sentences ,it is computationally expensive especially for very large
corpus. Using a database to index the sentences in a corpus could speed up code execution.
 </ul>



### 💡 Language Requirements  
The language used for this project was Yoruba but the code supports any language at all as long as a few conditions are met
    * The characters of the language exists in python's character map.
    * The language uses . (dot / full stop) to denote the end of a sentence.
    


### 👓 Author
Moses Bankole

