str=input()
if str.find('h') != -1:
  str=str[str.find('h')+1:]
  if str.find('e') != -1:
   str=str[str.find('e')+1:]
   if str.find('l') != -1:
     str=str[str.find('l')+1:]
     if str.find('l') != -1:
       str=str[str.find('l')+1:]
       if str.find('o') != -1:
         print('YES')
       else:
         print('NO')
     else:
       print('NO')
   else:
     print('NO')
  else:
    print('NO')
else:
  print('NO')