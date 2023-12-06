def multiple_returns(sentence):
    if not sentence:
        return ("Length: 0 - First character: None")
    else:
        m = (len(sentence), sentence[0])
        return m


#sentence = ""
#length, first, *rest = multiple_returns(sentence)
#print("Length: {} - First character: {}".format(length, first))