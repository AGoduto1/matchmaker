# Angelo Goduto
# Matchmaker-aag

# Constants
INTRODUCTION = '''

      *****************************************
     *               Matchmaker 1.1            *
   *      Helping you find luv since 2019        *
 *                  Cupidsoft, Inc.                *
******************************************************

This program figures out if you and I are meant to be.
You will answer 5 questions. To each question, answer 5
if you strongly agree, 4 if you agree, 3 if you neither
agree nor disagree, 2 if you disagree, and 1 if you
strongly disagree.

Our happiness depends on you. Don't let us down ...
'''

QUESTION = [
    'Hawkeyes Football is the best',
    'European soccer is the greatest sport in the world!',
    'PHP is the best computer language',
    'Computer Science is the best major.',
    'Are you glad this is the last question?'
]

DESIRED_RESPONSE = [
    5, # strongly agree
    2, # disagree
    1, # strongly disagree
    5, # strongly agree
    1  # strongly disafree

]

MAX_SCORE = 5 * len(QUESTION)

print(INTRODUCTION)

response = []
compatibility = []

# Ask all questions.
for i in range(len(QUESTION)):
    userResponse = int(input(QUESTION[i]))
        # Todo: Validate response and ask question again if necessary.
    response.append(userResponse)

    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatibility.append(questionCompatibility)

    # String formatting with parameters and placeholders
    print("Question %d compatability: %d\n" % (i+1, questionCompatibility))

totalCompatiblity = 0
for c in compatibility:
    totalCompatiblity += c

totalCompatiblity *= 100 / MAX_SCORE
print('Total Compatibility: %d\n\n' % (totalCompatiblity))

# Todo: Determine compatibility ranges.