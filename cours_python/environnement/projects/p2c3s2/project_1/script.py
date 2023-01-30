from dateutil import parser


parsed_date = parser.parse('3rd January 2014')
print('The type of the parsed date is {}'.format(type(parsed_date)))
