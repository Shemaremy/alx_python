def multiple_returns(sentence):
    if not sentence:
        return (None)
    else:
        return(len(sentence), sentence[0])


#sentence = "Holberton"
#length, first = multiple_returns(sentence)
#print("Length: {:d} - First character: {}".format(length, first))