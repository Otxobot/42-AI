import re
import sys

def text_analyzer(txt=None):
    if txt == None:
            txt= input("Where is the text I have to analyze?\n>>")
    length = len(txt)
    print(f"The text contains {length} characters")
    lengt_of_caps = len(re.findall(r'[A-Z]', txt))
    print(f"There are {lengt_of_caps} capital letters")
    lengt_of_min = len(re.findall(r'[a-z]', txt))
    print(f"There are {lengt_of_min} lowercase letters")
    amount_of_puncs = len(re.findall(r'[.,\'"!%&?¿]', txt))
    print(f"There are {amount_of_puncs} punctuation marks")
    amount_of_spaces = len(re.findall(r'[ ]', txt))
    print(f"There are {amount_of_spaces} spaces")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        txt = ""
        while len(txt) == 0:
            txt = input("Where is the text I have to analyze?\n>>")
        text_analyzer(txt)
    text_analyzer(sys.argv[1])