sentence=input('enter a sentence:\t')
width=int(input('enter a width:\t'))
def make_paragraph(sentencee,widthh):
    counter=0
    update=''
    for element in sentencee:
        counter+=1
        update+=element
        if counter%widthh==0:
            update+='\n'
           # counter=0
    print(update,end=' ')
make_paragraph(sentence,width )