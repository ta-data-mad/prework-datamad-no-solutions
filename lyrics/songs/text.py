def babyshark(): 

  animal='shark'
  doo='doo '
  family=['Baby ','Mommy ','Daddy ','Grandma ','Grandpa ',"Let's go hunt"]
  paragraph=0
  complete_song=[]
  result=0

  for e in family:
    i=family.index(e)
    if paragraph<(len(family)-1):
      complete_song.append((3*(family[i]+animal+', '+(doo*6)+'\n'))+ (family[i]+animal+'!\n'))
      paragraph+=1
    else:
      complete_song.append((3*(family[i]+', '+(doo*6)+'\n'))+ (family[i]+'!\nRun away,…'))

  result=''.join(complete_song)
  #print (result)

  #print(len(babyshark))
  #print(len(result))

  return (result)

#print(babyshark() == babyshark)


text = open('baby_shark_song.txt','w')
text.write(babyshark()) 
text.close() 
print (text==babyshark)
print(babyshark() == text)
