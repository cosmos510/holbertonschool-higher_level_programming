#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        return len(sentence)
    return len(sentence), sentence[:1]
