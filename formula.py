
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
     

périmètredutrapèze(1,6,2,0)