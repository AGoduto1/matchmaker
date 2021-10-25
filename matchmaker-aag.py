# Angelo Goduto
# Matchmaker-aag
# Taken from the code of EnterANumberBetween1And5 by Eric Pogue

# Constants
INTRODUCTION = '''

          *********                **********
        *          *              *           *
      *             *************
    *               Matchmaker 1.0                *
  *      The Most Intresting Man Of The Year       *
 *                  Cupidsoft, Inc.                  *
***************************************************** **
*                       Hello,                           *
*    My name name is Angelo Goduto and I am looking      *
 *   for the one! Below are going to be a few questions  *
  *  that I want to ask and depending on how you answer *
   * these questions will determine how compatable we  *
    * are. You should answer each question with       *
     * a number rating of 1 thru 5. 1 meaning        *
      * you strongly disagree, 3 meaning youre      *
       * neutral, and 5 meaning you strongly       *
        *               agree.                    *
         *                                       *
          *     Everything you put will         *
           *       possibly change your        *
            *            future               *
             *                               *
              *         Forever ...         *    
                *                          *
                  *                      *
                    *                  *
                      *            *
                        *        *
                          *    *
                            **

'''

QUESTION = [
    'The Blackhawks are the best hockey team.',
    'Philosphy is the best subject.',
    'HTML is the best code.',
    'Flying is the best way to travel.',
    'The winter is the best time of year.'
]

DESIRED_RESPONSE = [
    5, # strongly agree
    1, # strongly disagree
    4, # agree
    5, # strongly agree
    2  # disagree

]

MAX_SCORE = 5 * len(QUESTION)

print(INTRODUCTION)

response = []
compatibility = []

# UserResponse2String = str(input(("Enter a number between 1 and 5.\n")))
# print("You entered: " + UserResponse2String)
for i in range(len(QUESTION)):
    userResponse = int(input(QUESTION[i]))
# Here I tried completing the validation and I couldn't seem to figure out what I was doing wrong.
# So I tried putting str instead of int so I could put my if statement below.
# This caused the code to crash multiple times.

    response.append(userResponse)

# if not userResponse.isnumeric():
#    print("This is not a number.")
# else:
#    print("This is a valid number.")


    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatibility.append(questionCompatibility)

    print("Question %d compatability: %d\n" % (i+1, questionCompatibility))

totalCompatiblity = 0
for c in compatibility:
    totalCompatiblity += c

totalCompatiblity *= 100 / MAX_SCORE
print('Total Compatibility: %d\n\n' % (totalCompatiblity))

if totalCompatiblity >= 85:
    print("What's your phone number? We should start talking.")
elif totalCompatiblity >= 65:
    print("Maybe there's a view things we can change to make it better.")
elif totalCompatiblity >= 40:
  print("I guess we should be seeing other people.")
elif totalCompatiblity >= 0:
  print("Please don't talk to me...")

