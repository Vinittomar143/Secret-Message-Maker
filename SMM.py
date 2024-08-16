import string
import random
def ran_char(y):
  return ''.join(random.choice(string.ascii_letters) for x in range(y))
ran1=ran_char(3)
ran2=ran_char(3)

st=input("Enter Message: ")
words=st.split(" ")
coding=input("Press 1 for coding and press 0 for decoding: ")
coding=True if (coding=="1") else False
if(coding):
  nwords=[]
  for word in words:
    if(len(word)>=3):
      stnew=ran1+word[1:]+word[0]+ran2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
else:
  nwords=[]
  for word in words:
    if(len(word)>=3):
      stnew=word[3:-3]
      stnew=stnew[-1]+stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
