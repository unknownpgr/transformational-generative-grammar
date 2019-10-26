import random

NONE_TERMINAL_SIGNAL = '@'

grammar = {
    '@start': ['@vars @newline_t @functions @newline_t int @space_t main ( ) { @newline_t @codes } @newline_t'],

    '@functions': ['@function', '@function @newline_t @functions'],
    '@function': ['void @space_t @name ( ) { @newline_t @codes } @newline_t '],

    '@vars': ['@var', '@var @vars'],
    '@var': ['@type_t @space_t @name ; @newline_t', '@type_t @space_t @name = @value ; @newline_t'],

    '@codes': ['@none_t', '@code ; @newline_t', '@code ;  @newline_t @codes', '@codes @brances @codes'],
    '@code': ['@name @space_t = @space_t @term', '@name ( )'],
    '@brances': ['@if', '@for','@while'],

    '@term': ['@name', '@name ( )', '@code', '@comparation', '@operation', '@value'],
    '@comparation': ['@term @space_t > @space_t @term', '@term @space_t < @space_t @term', '@term @space_t == @space_t @term'],
    '@operator2' :['+','-','*','/','^','&','&&','|','||','%','==','+=','-=','*=','/='],
    '@operator1L' : ['!','-','+'],
    '@operator1R' : ['++','--'],
    '@operation': ['@term @space_t @operator2 @space_t @term','@operator1L @term',' @name @operator1R'],

    '@if': ['if( @term ){ @newline_t @codes } @newline_t', 'if( @name ){ @newline_t @codes }else{ @newline_t @codes } @newline_t'],
    '@for': ['for ( @code ; @term ; @space_t  @code ) { @newline_t @codes } @newline_t'],
    '@while': ['while ( @term ) { @newline_t @codes } @newline_t'],

    '@type_t': ['int', 'float', 'double', 'char', 'long'],
    '@name': ['@character_t', '@name @character_t', '@name @number'],
    '@value': ['@number', '\' @character_t \'', '0x @number'],

    '@character_t': ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'L', 'm', 'n', 'O', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    '@number': ['@number_t', '@number_t @number'],
    '@number_t': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

    '@none_t': [''],
    '@space_t': [' '],
    '@newline_t': ['\n']
}


def generate(token, grammar, depth):
    print(depth, token)

    if token[0] is not NONE_TERMINAL_SIGNAL:
        return [token]

    else:
        if token[-2] == '_' and token[-1] == 't':
            terminal = random.choice(grammar[token])
            return [terminal]
        else:
            if depth<30:
                sentence_structure = random.choice(grammar[token])
            else:
                # If depth is too deep, do not recursivly generate code.
                copy = []
                for gram in grammar:
                    if not token in gram:
                        copy.append(gram)
                sentence_structure = random.choice(copy)
            print(sentence_structure)
            parsed_tokens = sentence_structure.split(' ')
            sentence = []
            for token in parsed_tokens:
                if(len(token) == 0):
                    continue
                sentence += generate(token, grammar, depth+1)
            return sentence


sniffets = generate('@start', grammar, 0)

code = ''
for piece in sniffets:
    code += piece

print(code)
