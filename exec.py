import random


def is_terminal(token):
    return token[0] != "_"


def expand(grammar, tokens):
    for i, token in enumerate(tokens):

        # ignore terminals
        if is_terminal(token):
            continue

        # choose a replacement at random
        replacement = random.choice(grammar[token])

        if is_terminal(replacement):
            tokens[i] = replacement
        else:
            tokens = tokens[:i] + replacement.split() + tokens[(i+1):]
        return expand(grammar, tokens)

    # if we get here we had all terminals and are done
    return tokens


def generate_sentence(grammar):
    return expand(grammar, ["_S"])


grammar = {
    "_S": ["_NP _VP"],
    "_NP": ["_N", "_A _NP _P _A _N", "_A _N"],
    "_VP": ["_VN _N", "_VN _NP", "_V"],
    "_N": ["data science", "Python", "apple", "desk", "chair", "bed", "room", "box", "glass", "bottle"],
    "_A": ["big", "linear", "logistic", "smart", "fast", "slow", "rapid", "bright", "dark", "hot", "cold", "high", "low"],
    "_P": ["about", "near", "of", "from", 'after', 'along', 'at', 'beside', 'in', 'on', 'over', 'round'],
    "_VN": ["learns", "trains", "tests", "is", "kills", "types", "chooses", "reverts", "opens", "delets", "stacks"],
    "_V": ["runs", "dies", "sleeps", "falls", "rises"]
}

words = generate_sentence(grammar)
for word in words:
    print(word, '', end='')
