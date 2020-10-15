import time
import random
#---
def main():
  words = open("words.txt", 'r')
  words = words.readlines()
  for x in range(0, len(words)):
    temp = str(words[x])
    temp = temp.replace("\n", "")
    words[x] = temp
  print("Simple Type racer using time.time()")
  input("Type the word(s) shown on screen as fast as possible. \n Press ENTER to start.")
  start = time.time()
  word = str(random.choice(words))+" "+str(random.choice(words))
  print(word)
  inp = input("\n>>>: ")
  while inp != word:
    inp = input("\nIncorrect try again\n"+str(word)+"\n>>>: ")
  end = time.time()
  total = end - start
  print(str(round(total, 2))+" seconds.")

while 1:
  try:
    main()
  except Exception as error:
    print("There was an error.\n"+str(error))