import re

# Base for cheatsheet
play_string = '''abcdefghijklmnopqurtuvwxyz
abcDefghijklmNopqurtuvwxyZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] '\' | ( )
lietuva.com
ac
+37060482010
}37060482010
+370.604.82.010
+370-604-82-010
+aaa-604-82-010
+ddd-604-82-010
-37060482010
111.999.6699
eima.blaz@gmail.com_'''

patternText = re.compile(r'ac')                 # To find exact text
patternAnyText = re.compile(r'.')               # To find any text
patternDigits = re.compile(r'\d')               # Find all digits
patternNotDigits = re.compile(r'\D')            # Find all not digits
patternCharacters = re.compile(r'\w')           # Find all characters and _
patternNotCharacters = re.compile(r'\W')        # Find all not characters and not _
patternWhitespace = re.compile(r'\s')           # Whitespace and newline
patternNotWhitespace = re.compile(r'\S')        # Not Whitespace and newline

patternWordBoundary = re.compile(r'\bHa')       # Occurrence of Ha even if it is star of another work
patternNotWordBoundary = re.compile(r'\BHa')    # Individual occurrence of Ha
patternStarString = re.compile(r'^ab?c')        # Starts with string
patternEndWithString = re.compile(r'.com')      # Ends with string

patternListOfOptions = re.compile(r'[-+]37060482010')       # List of options
patternNotListOfOptions = re.compile(r'[^-+]37060482010')   # Not list of options
patternGrouping = re.compile(r'\+(\d\d\d).(\d\d\d).(\d\d.\d\d)')    # Grouping

patternZeroOrMore = re.compile(r'\+370*')  # Zero or more
patternOneOrMore = re.compile(r'\+370+')  # One or more
patternOptionalCharacter = re.compile(r'ab?c')  # Optional Character
patternExactNumber = re.compile(r'\+(\d{3}).(\d{3}).(\d{2}.\d{2})')
patternRangeOfNumbers = re.compile(r'(\d{3}).(\d{3}).(\d{2,4})')

# result = re.findall(patternExactNumber, play_string)
# print(result)

#  Find first occurrence of the pattern in the text
resultSearch = patternText.search(play_string)
print(resultSearch.group(0))

#  Match the start of the text
resultMatch = patternText.match(play_string)
print(resultMatch)

#  Find all occurrences
resultFindAll = patternText.findall(play_string)
print(resultFindAll)

# Same as find all but returns an iterator
resultFindAllIter = patternText.finditer(play_string)
print(resultFindAllIter)

# Split functionality
resultSplit = patternWhitespace.split(play_string)
print(resultSplit)

# Substitute with another
resultSub = patternWhitespace.sub('Potato', play_string)
print(resultSub)

# Substitute with another but shows how many substitutes done
resultSubN = patternWhitespace.subn('Potato', play_string)
print(resultSubN)