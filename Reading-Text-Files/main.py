# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    #read file
    with open(filename) as file:
        data = file.read().replace(',','').replace('.','').replace('?','')

        return data
        
 
def count_words(filename):
    text = read_file_content(filename).split()
    # [assignment] Add your code here
    count = {}
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
filename = "./story.txt"
#print(text)
print(count_words(filename))