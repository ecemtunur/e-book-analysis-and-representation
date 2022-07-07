import requests   # In here, I called the modules and libraries that I will use here (by using "import" command)
import operator
from bs4 import BeautifulSoup   

print("   Hello, I want to give you some informations \n     about the words of the books you want.\n        You can choose one or two books.")

while True:
    howmanybooks = int(input("\nHow many books do you want to see? \n"))  # I asked the user how many books they want to see. I gave the user a chance to rewrite, 
    if howmanybooks == 1:                                                 # if user enters something different from the format of the project.
        break
    elif howmanybooks == 2 :
        break
    else :
        print("You have one more chance O_o")
        
while True:
    chooseword = input("Would you like to enter the number of words? Press 'Y' for yes, 'N' for no = \n") # I asked the user if he/she wanted to set the number of words that would appear.  
    if chooseword == "Y" or chooseword == "y":                                                            # I made letters more sensitive (upper and lower case)
        wordwanted = int(input("Please, enter how many words do you want to see? \n"))                    # If a value is entered, that value will be displayed, if not, twenty words will be displayed.
        break
    elif chooseword == "N" or chooseword == "n":
        wordwanted = 20
        break
    else:
        print("I think you pressed wrong key, I give you one more chance ^-^")

def deletesymbols(lists):       
    withoutsymbol = []          
    symbols =["'m", "'s", "'t", "'ll", "'ve", "'re", "'", '—', '=', '==', '\t', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '.' , ',', '!','?','(',')' ,';', '[', ']', '\n', '"', ':', '  ', '~', '@', '^' , '#' , '%' , '$' , '&', '*', '_', "-", '`', '{', '}', '|', '>', '<', '←', '→' ]
    
    for word in lists:                                 
        for symbol in symbols:               
            if symbol in word:
                word = word.replace(symbol, " ").strip()   # This function is for removing symbols. If the word in the book is the same as this symbol, or if it contains this symbol, I put a space in its place.
        
        if word != '' and len(word) > 0:     # If the resulting word is not a space and does not consist of a single character, I added it to the cleared words.
            piece = word.split()             # If it is a group of words, I splitted the words according to the space and added it to the clean words.
            for Word_2 in piece : 
                Word_2 = Word_2.strip()
                if Word_2 != '' and len(Word_2) > 0:
                    withoutsymbol.append(Word_2) 
    return withoutsymbol

def deletestopwords(lists):
    withoutstopwords = []  
    stopwords = ["etc", "-", "us", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "u", "v", "y", "z", "w", "x", "q", "I", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", 
                 "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has",
                 "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", 
                 "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", 
                 "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "end", "should", "now", "next", "first"]
    
    for word in lists:              # I made a few additions myself to the stop words, which I received from a source I showed in the references section, and separated them from the words of the book.
        for sword in stopwords:
            if sword == word:
                word = word.replace(sword, " ")                
        if(len(word) > 0) and word != " ":
            withoutstopwords.append(word)    # I added them to the list I created at the beginning of the function.
    return withoutstopwords           

def dictionaries(lists):
    count = {}                  # I created a dictionary
    for word in lists:          # I took the words of the book and passed them through this dictionary. 
        if word in count:       # If there is in this dictionary I increased its value, otherwise I added it to the dictionary as a word.
            count[word] += 1  
        else:
            count[word] =  1
    return count

if howmanybooks == 1:       
    allwords=[]
    bookname = input("Please, write book name \n")       # If one book was requested, I took the title of the book and edited.
    url = bookname.replace(" ", "_").replace("'", "%27")
    r = requests.get("https://en.m.wikibooks.org/wiki/" + url + "/Print_version") 
    soup = BeautifulSoup(r.content, 'html.parser')       # I obtained the link using the request module and made it suitable for the Python language using the BeautifulSoup library.
    
    file1 = open("book1.txt", "w", encoding="utf-8")     # I added (encoding="utf-8") in order to avoid any incompatibilities. (book1.txt) This file is for me to get the words easy
    file3 = open("book.txt", "w", encoding="utf-8")      # The whole book is in this file as text (book.txt)
    for lines in soup.find_all("div", {"class":"mw-parser-output"}):  # I bought this part to be more general (("div", {"class":"mw-parser-output"}))
        cont = lines.text
        file3.write(cont)
        words = cont.lower().split()                    # I converted all words to lowercase letters so that there is no capital letter mismatch. 
        
        for word in words:
            file1.write(word + "\n")
    file1.close()
    file3.close()
            
    file2 = open("book1.txt", "r", encoding="utf-8")    # I opened the file and read from there this time.
    words1 = file2.readlines()
    file2.close()
    
    for word in words1:
        allwords.append(word)         # I added the words to the list and then cleared them through functions.
    
    allwords = deletesymbols(allwords)
    allwords = deletestopwords(allwords)
    wordcount = dictionaries(allwords)  # I created the dictionary from the clean list for comparison purposes.
           
    counter = 1   
    print("\nBOOK NAME : " + bookname + "\nNO   WORD        FREQ_1\n~~   ~~~~        ~~~~~~")   # I printed the table header.                    
    for key,value in sorted(wordcount.items(),reverse=True, key = operator.itemgetter(1)):      # I ordered the words as many as user wants from the most repeated to the least.
        if counter > wordwanted:
           break   
        else:       
            print("{:<4} {:13} {:<4}".format(counter, key, value))  # I used format command to make the table neat.
        counter += 1    
        
elif howmanybooks == 2:       # In this part, I repeat the actions taken when a book was requested. 
    allwords1=[]              # This time, there are three lists (two lists for the words of the books, the other for the words of both books)
    allwords2=[]
    allwords1_2 = []
    bookname = input("Please, write first book name \n")    # I edited and added the links of two books.
    url1 = bookname.replace(" ", "_").replace("'", "%27")
    r = requests.get("https://en.m.wikibooks.org/wiki/" + url1 + "/Print_version")
    soup = BeautifulSoup(r.content, 'html.parser')
    bookname2 = input("Please, write second book name \n")
    url2 = bookname2.replace(" ", "_").replace("'", "%27")
    r2 = requests.get("https://en.m.wikibooks.org/wiki/" + url2 + "/Print_version")
    soup2 = BeautifulSoup(r2.content, 'html.parser')
       
    file1 = open("book1.txt", "w", encoding="utf-8")                    # I did the same file operations this time for two books. (book1.txt) This file is for me to get the words easy
    file5 = open("firstbook.txt", "w", encoding="utf-8")                # The whole book is in this file as text (firstbook.txt)
    for lines in soup.find_all("div", {"class":"mw-parser-output"}):    # For first book.
        content = lines.text
        file5.write(content)
        words = content.lower().split()
        
        for word in words:
            file1.write(word + "\n")
    file1.close()
    file5.close()
    
    file2 = open("book1.txt", "r", encoding="utf-8")
    words1 = file2.readlines()
    file2.close()
    
    for word in words1:                 
        allwords1.append(word)    # I added the words to own list and the common list.
        allwords1_2.append(word)

    file6 = open("secondbook.txt", "w", encoding="utf-8")   # The whole book is in this file as text (secondbook.txt) 
    file3 = open("book2.txt", "w", encoding="utf-8")                    # For second book. (book2.txt) This file is for me to get the words easy
    for line in soup2.find_all("div", {"class":"mw-parser-output"}):
        contents = line.text
        file6.write(contents)
        wordss = contents.lower().split()
        
        for wordd in wordss:
            file3.write(wordd + "\n")  
    file3.close()
    file6.close()
    
    file4 = open("book2.txt", "r", encoding="utf-8")
    word2 = file4.readlines()
    file4.close()
    
    for word in word2:          # I added the words to own list and the common list.
        allwords2.append(word)
        allwords1_2.append(word)
    
    allwords1 = deletesymbols(allwords1)
    allwords1 = deletestopwords(allwords1)
    wordcount1 = dictionaries(allwords1)
    
    allwords2 = deletesymbols(allwords2)
    allwords2 = deletestopwords(allwords2)
    wordcount2 = dictionaries(allwords2)
    
    allwords1_2 = deletesymbols(allwords1_2)
    allwords1_2 = deletestopwords(allwords1_2)
    wordcountcommon = dictionaries(allwords1_2)
        
    counter = 1
    print("\nBOOK 1 : " + bookname + "\nBOOK 2 : " + bookname2 + "\n\nCOMMON WORDS \nNO   WORD        FREQ_1  FREQ_2  FREQ_SUM\n~~   ~~~~        ~~~~~~  ~~~~~~  ~~~~~~~~")
    for key,value in sorted(wordcountcommon.items(),reverse=True, key = operator.itemgetter(1)):
        if key in allwords1 and key in allwords2:   # If both words are in the list, that word is common.           
            if counter <= wordwanted:                
                print("{:<4} {:13} {:<6}  {:<6}  {:<6}".format(counter, key, wordcount1[key], wordcount2[key], value ))  
                counter += 1
            del wordcount1[key]      # To find different words, if the word in the dictionary of common words was in the lists of the books, I deleted this word from the dictionary of the books.
            del wordcount2[key]
                    
    counter = 1
    print("\nBOOK 1 : " + bookname + "\nDISTINCT WORDS \nNO   WORD        FREQ_1\n~~   ~~~~        ~~~~~~") # I listed the words in the dictionary of first book and dictated them.
    for key,value in sorted(wordcount1.items(),reverse=True, key = operator.itemgetter(1)):
        if counter > wordwanted:
           break   
        else:                          
            print("{:<4} {:13} {:<4}".format(counter, key, value))
        counter += 1    
    
    counter = 1
    print("\nBOOK 2 : " + bookname2 + "\nDISTINCT WORDS \nNO   WORD        FREQ_2\n~~   ~~~~        ~~~~~~") # I listed the words in the dictionary of second book and dictated them.
    for key,value in sorted(wordcount2.items(),reverse=True, key = operator.itemgetter(1)):
        if counter > wordwanted:
           break   
        else:                          
            print("{:<4} {:13} {:<4}".format(counter, key, value))
        counter += 1
