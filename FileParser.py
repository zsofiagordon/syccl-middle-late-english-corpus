#0: 1300 - chaucer
#1: 1500 - shakespeare
#2: 1600 - milton
#3: 1700 - austen
#4: 1800 - dickens


import re

def extract_sents(text, out, label):
        sents = re.findall(r".+?[\.?!]", text.strip())
        for sent in sents:
            if(len(sent)>=10):
                out.write(label+" "+sent.strip()+"\n")
        return sents;

 
def main():
    out = open("dataset.txt", "w")
    for i in range(0,4):
        f = open("century"+str(i)+".txt", "r")
        text = f.read()
        extract_sents(text, out, i);
    print("done");




        


