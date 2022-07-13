def weclome () :
  print("*********************************")
  print("**                             **")
  print("** Welcome to the Command Line **")
  print("**                             **")
  print("*********************************\n")

def merge(parsed, adj, fname,verb,pNoun,lAnimal,sAnimal,gName,fNo,fName,sNo):
  newText=parsed.format(Adjective= adj, A_First_Name=fname, Past_Tense_Verb=verb, Plural_Noun=pNoun, Large_Animal=lAnimal, Small_Animal=sAnimal, A_Girl_Name=gName, OneToFifty_Number= fNo, First_Name=fName, Number=sNo)

  print("\nResulted outcome...\n")
  print("**********************************")
  print(newText)
  print("**********************************")
  print("That was funny, TQ")

  reFile = open("../assets/results.txt", "w")
  reFile.write(newText)
  reFile.close()

def getInput(text):
  print("\nPlease enter an adjective")
  adjective = input()

  print("\nPlease enter a first name")
  fname = input()

  print("\nPlease enter a past-tense verb")
  verb = input()

  print("\nPlease enter a plural noun")
  pNoun = input()

  print("\nPlease enter a large animal name")
  lAnimal = input()

  print("\nPlease enter a small animal name")
  sAnimal = input()

  print("\nPlease enter a girl name")
  gName = input()

  print("\nPlease enter a number between 1 and 50")
  fNo = input()

  print("\nPlease enter another first name")
  fName = input()

  print("\nPlease enter any number")
  sNo = input()

  merge(text,adjective,fname,verb,pNoun,lAnimal,sAnimal,gName,fNo,fName,sNo)

def parse_template(text):
  getInput(text)

def read_template(link):
  try:
    file = open(link)
  except FileNotFoundError:
    print("Error: Sorry the file does not exist!")
  else:
    content = file.read()
    parse_template(content)
  finally:
    file.close()

weclome()
read_template("../assets/dark_and_stormy_night_template.txt")  
