import re

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print ('Searching the phrase using the re check: %r' %pattern)
        print (re.findall(pattern,phrase))
        print ('\n')




test_phrase = "This is a string! But it has 321314442. How can we remove it?"
test_patterns = [r'\D+']

multi_re_find(test_patterns,test_phrase)


# test_patterns = [ 'sd*',     # s followed by zero or more d's
#                 'sd+',          # s followed by one or more d's
#                 'sd?',          # s followed by zero or one d's
#                 'sd{3}',        # s followed by three d's
#                 'sd{2,3}',      # s followed by two to three d's
#                 ]
