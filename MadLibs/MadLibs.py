import random

def getAdjective(adjective):
    return random.choice(adjective.split())

def getNoun(nouns):
    return random.choice(nouns.split())

def getVerb(verbs):
    return random.choice(verbs.split())

if __name__ == "__main__":

    # print(madlib)

    openNoun = open("english-nouns.txt", "r+")
    openAdjective = open("english-adjectives.txt", "r+")
    openVerb = open("english-verbs.txt", "r+")
    adjectives = openAdjective.read()
    noun = openNoun.read()
    verb = openVerb.read()

    madlib = f"Hello, This is {getAdjective(adjectives)}, I am here to {getVerb(verb)} " \
             f"this Project and be like {getNoun(noun)} "\
             f"and become {getVerb(verb)} or also maybe a {getVerb(verb)}\n" \
             f"this is not to {getVerb(verb)} since that's {getAdjective(adjectives)} what can i say this is {getAdjective(adjectives)} {getNoun(noun)}"

    print(madlib)

    openAdjective.close()
    openNoun.close()
    openVerb.close()