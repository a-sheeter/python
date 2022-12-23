import random

user_name = "Amy";
user_question = "Will I win the lottery?";

rand_num = random.randrange(0,8);
eight_answer = "";

print(user_name + " asks: " + user_question)

if rand_num == 0:
  eight_answer = "Yes - definitely.";
elif rand_num == 1:
  eight_answer = "It is decidedly so.";
elif rand_num == 2:
  eight_answer = "Without a doubt";
elif rand_num == 3:
  eight_answer = "Reply hazy, try again.";
elif rand_num == 4:
  eight_answer = "Ask again later.";
elif rand_num == 5:
  eight_answer = "Better not tell you now.";
elif rand_num == 6:
  eight_answer = "My sources say no.";
elif rand_num == 7:
  eight_answer = "Outlook not so good.";
elif rand_num == 8:
  eight_answer = "Very doubtful.";
else:
  eight_answer = "Error";

print("Magic 8-Ball's answer: " + eight_answer);
