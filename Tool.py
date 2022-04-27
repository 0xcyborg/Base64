# 2022-04-27

from base64 import b64decode,b64encode

Option = int(input("1- Encrypt\n2- Decrypt\n-> "))

def Process(Value):
  Key = int(input("Key -> "))
  with open("Data.txt","r") as File:
    Data = bytes(File.read().encode("utf-8"))
  for Num in range(Key):
    if(Value == 1):
      Data = b64encode(Data)
    elif(Value == 2):
      Data = b64decode(Data)
  else:
    print("<Done>")
    with open("Data.txt","w") as File:
      File.write(Data.decode("utf-8"))

if(__name__ == "__main__"):
  if(Option == 1):
    Process(Option)
  elif(Option == 2):
    Process(Option)
  else:
    print("?")