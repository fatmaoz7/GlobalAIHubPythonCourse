# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:51:48 2021

@author: fatma oz
"""
from Question import Question

print("Welcome to the Knowledge Competetion program")
print("Each question worth 10 points")
print("Answers were adjusted according to case sensitivity")
print("Please be ready!")
questions=["1st question:What is the capital city of Turkey? ",
           "2nd question:Who created Python? ",
           "3rd question:Who was the instructor of Python course? ",
           "4th question:When was Python created? ",
           "5th question:When first laser was built? ",
           "6th question:World Human Rights Day is celebrated every year on December... ",
           "7th question:He is known as the ‘Builder of Modern Turkey’ ",
           "8th question:What is the result? 2**3%3+15//5+24 ",
           "9th question:What is the result? 18%4*3-5+24 ",
           "10th question:Who will be one of the top learners? ",
    
    ]

q=[Question(questions[0],"Ankara"),
   Question(questions[1],"Guido van rossum"),
   Question(questions[2],"Ömer Cengiz"),
   Question(questions[3],"1991"),
   Question(questions[4],"1960"),
   Question(questions[5],"10"),
   Question(questions[6],"Mustafa Kemal Atatürk"),
   Question(questions[7],"29"),
   Question(questions[8],"25"),
   Question(questions[9],"Fatma ÖZ"),

   ]
def run_test(q):
    score=0;
    for a in q:
        answer=input(a.prompt)
        if answer==a.answer:
            score+=10;
    print("You got", score, "points")
run_test(q)