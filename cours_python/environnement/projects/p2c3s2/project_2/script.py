from fuzzywuzzy import fuzz


ratio = fuzz.ratio('Open Classrooms', 'Openclassrooms')
print('The two strings have a similarity match of {}'.format(ratio))
