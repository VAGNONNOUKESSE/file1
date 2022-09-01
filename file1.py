from operator import length_hint


1+1
 4*7
 a=5
 a*2
 8
 1.5
 B =[1,2.4,3,"ali"]
 C={"Ali":12,"Bio":13}
 D=(1,2,3,4,5,8)
 D
 E='Bonjour monde '
 E
 8%2
 9%2
 129%5
 X="Je m'appelle "
 Y="VAGNONNOUKESSE Coovi Christophe"
 X + Y
 3 >= 1
 3<=1
 print("Hello world")
 type(B)
 float('12')
 f, e,g,h='bon ','apres','midi','a vous'
 f + e
 

 A=[1,2,3,4,5,6,7,8,9,10,11,12]
 for n in A:
    print(n*2 % 4)

 s = 5
 while s < 100:
  s += 2
  print(s)
   
    

 A=[1,2,3,4,5,6,7,8,9,10]
 for n in A:
     if n% 2==0:
            print("This number is even")
     else:
        print("the number what you enter is odd ")


        n=10
        while True :
            print(n)
            n+=5

            B=[5,6,7,8,18,20,25,30,45,50,60,70,80,90,100]
            for n in B:
               if n<=7:
                  print("The age of this person is",n," yeaars , so it is CHILD")
               elif 7<n and n<18:
                     print("The age of this person is",n," yeaars , so it is TEENAGER")
               elif 18<=n and n<=45:
                  print("The age of this person is",n," yeaars , so it is YOUNG")
               else:
                  print(" The age of this person is",n," yeaars , so it is OLD")
            
for  n in  range(1,21):
   if n<10:
      print(n,"BAD GRADE")
   elif 10<=n and n<16:
      print(n,"CONGRATULATION")
   else:
      print(n,"EXCELLENT")
# question 1
for n in range(230):
   if n%2==0:
      print(n,"is even")
   else:
       print(n,"is odd")
   if n%5==0:
      print(n,"is divided by 5")
   elif n%3==0:
     print(10*n,"because ",n,"is divided by 3")
   
      
for n in range(21):
   if n==11:
      break
   print(n)



for n in range(21):
   if n==11:
    continue
   print(n)



A=["Ali","Bio","Baké"]
B=["Student","Pupil","Farmer"]
for a in A:
   for b in B:
      print(a,b)

      #24/08/2022
 A=[1,2,3,4]
mylist= [n for n in A]
mylist2= [n*4 for n in mylist]
mylist2
mylist3 =[n*4 for n in A] 
mylist3

fruits=["apple","banana","cherry","kiwi","mango"]
newlist1=[]
for x in fruits:
   if "a" in x:
      newlist1.append(x)
newlist1
newlist4=[n for n in fruits if "a" in n ]
print(newlist4)

newlist5=[n for n in fruits if n!="apple" ]
newlist5
liste=[n for n in range(len(fruits))]
liste
liste1=[x for x in range (10) if x<5]
liste1

liste2 =[x.upper() for x in fruits]
liste2

liste3=[x if x!="banana" else "orange" for x in fruits]
liste3

# using of the function: input()
myname=input("Enter your name :")
myname

myage=input("Enter your age :")
myage

myprofession=input("Enter your profession :")
myprofession

print(myname,myage,myprofession)

# another way to go directly with these three statements
print(input("Enter your name"),input("Enter your age"),input("Enter your profession"))
#définition de sa propre fonction
def somme(a,b):
   return a+b
   somme(5,25)

# definition d'une fonction avec zero argument ,genre fonction constante
   def salut():
      print("Bonjour! Comment Ca va?")

      salut()


# definition d'une fonction avec un seul  argument 
def exposant(a):
   return a**a
      exposant(3)

      ######################################
      #              ASSIGNMENT -1          #
      ######################################

# fonction pour calculer l'aire du carré
def  aireducarré(a):
   if a>0:
      return a*a
   else:
      print("impossible")
    
   aireducarré(5)


# fonction pour calculer l'aire de la surface du rectangle
def airedurectangle(a,b):
   if a>0 and b>0:
      return a*b
   else:
      print('impossible') 

airedurectangle(0.5,6)

#fonction pour calculer le périmètre d'un rectangle
def périmètre(L,l):
   if L>0 and l>0:
      return (L+l)*2
   else:
      print("Impossible")
périmètre(3,6)

# fonction pour calculer l'aire de la surface d'un trapèze
def airedutrapèze(b,B,h):
   if B>0 and b>0 and h>0:
      return (b+B)*h/2
   else:
      print('impossible') 

airedutrapèze(3,4,5)

# fonction pour calculer du volume d'un pavé droit!
def volume(L,l,H):
   if L>0 and l>0 and H>0:
      return L*l*H
   else:
      print('impossible') 

volume(2,3,5)

#fonction pour calculer le périmètre d'un trapèze
def périmètredutrapèze(a,b,c,d):
   if a>0 and b>0 and c>0 and d>0:
      return a+b+c+d
   else:
      print("Impossible")
périmètredutrapèze(1,3,4,0)



  ######################################
  #              ASSIGNMENT -2         #
  ######################################

 # fonction déterminant la parité d'un nombre
def nombre(a):
   if a%2==0:
      print('The number', a,"is even")
   else:
      print('The number',a,"is odd")

nombre(6)


  # fonction déterminant le groupe d'un verbe
def verbe(a):
   if a.endswith("er"):
      print(a,"est un verbe du premier groupe")
   elif  a.endswith("ir") and not a.endswith("oir"):
      print(a," est un verbe du deuxième groupe")
   else:
      print(a,"est un verbe du troisième groupe")

verbe("voir")

#definition d'une fonction prenant un nombre infini d'arguments
def moyenne(*x):
   return sum(x)/len(x)

   moyenne(3,7,11,3,6)


# fonction calculant la moyenne des éléments d'une liste
def moyenne1(*liste):
   for a in liste:
      print(sum(a)/len(*liste))

      D=[6,3,12]
      moyenne1(D)

# fonction définitie par défaut
def somme1(a,b=5):
   return a+b

somme1(8)
somme1(1,6)


###############################
#           HOME WORK         #
###############################

def longueur(texte):
   return len(texte)

longueur("mot")

V=["a","e","i","o","u","y"]
def nbrevoyelle(texte):

   for n in V and n in texte:
      return len(n)

nbrevoyelle(mot)

moyenne(3,7)



#Cours du 26/08/2022
 #using of the anonymous function 
 q=lambda a,b:a+b
 print(q(6,5))
