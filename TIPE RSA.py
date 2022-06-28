import numpy as np

#retourne True si n est premier, False dans le cas contraire, n doit etre un entier

def estprem(n):

		if n == 1 or n == 2:
		  return True
		if n%2 == 0:
		  return False
		r = n**0.5
		if r == int(r):
		  return False
		for x in range(3, int(r), 2):
		  if n % x == 0:
		    return False
		return True


#découpe des blocs de longueur long dans une chaine de caractères k et retourne une liste des blocs

def decoupeblocs(k, long):
	d , f = 0 , long
	l = []

	while f <= len(k):

		l.append(k[d:f])

		d , f = f , f + long


	m = len(k)%long

	if m != 0:

		l.append(k[len(k)-m:])

	return l


#retourne le plus grand dénominateur commun de a et b

def pgcd(a,b):
	while (b>0):

		r=a%b

		a,b=b,r

	return a


#pgcd étendu avec les 2 coefficients de bézout u et v. Entrées : a, b entiers. Sorties : r = pgcd(a,b) et u, v entiers tels que a*u + b*v = r

def pgcde(a, b):


	r, u, v = a, 1, 0
	rp, up, vp = b, 0, 1

	while rp != 0:
		q = r//rp
		rs, us, vs = r, u, v
		r, u, v = rp, up, vp
		rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)

	return (r, u, v)


#retourne un dictionnaire contenant la clé privée et la clé publique sous forme de tuples: {priv:(clé privée),pub:(clé publique)}

def cle():
	#choix au hasard de deux entiers premiers (n et q)
	p = np.random.choice(1000,1)
	q = np.random.choice(1000,1)

	while estprem(p) is False:
		p = np.random.choice(1000,1)

	while estprem(q) is False:
		q = np.random.choice(1000,1)

	#calcul de n et m
	n = p*q
	m = (p-1)*(q-1)

	#recherche de e premier de m (c'est a dire tel que pgcd(m,c)=1 ) et de d = pgcde(m,c) tel que 2 < d < m
	r = 10
	d = 0
	while r != 1 or d <= 2 or d >= m:
		e = np.random.choice(1000,1)
		r, d, v = pgcde(e,m)

	n, e, d = int(n), int(e), int(d)


	return {"priv":(n,e), "pub":(n,d)}



def chiffre(n, e, msg):

	#conversion du message en codes ascii
	asc = [str(ord(j)) for j in msg]

	#ajout de 0 pour avoir une longueur fixe (3) de chaque code asccii
	for i, k in enumerate(asc):

		if len(k) < 3:

			while len(k) < 3:

				k = '0' + k

			asc[i] = k

	#formation de blocs de taille inferieure à n (ici blocs de 4)
	ascg = ''.join(asc)

	d , f = 0 , 4

	#on rajoute eventuellement des 0 a la fin de ascg de maniere a ce que len(ascg) soit un multiple de f
	while len(ascg)%f != 0:

		ascg = ascg + '0'

	l = []

	while f <= len(ascg):

		l.append(ascg[d:f])

		d , f = f , f + 4

	#chiffrement des groupes
	crypt = [str(((int(i))**e)%n) for i in l]

	return crypt



#m est une liste des blocs à déchiffrer

def dechiffre(n, d, m):
	#dechiffrage des blocs
	resultat = [str((int(i)**d)%n) for i in m]

	#on rajoute les 0 en debut de blocs pour refaire des blocs de 4
	for i, s in enumerate(resultat):

		if len(s) < 4:

			while len(s) < 4:

				s = '0' + s

			resultat[i] = s


	#on refait des groupes de 3 et on les convertie directement en ascii
	g = ''.join(resultat)

	asci = ''

	d , f = 0 , 3

	while f < len(g):

		asci = asci + chr(int(g[d:f])) #conversion ascii

		d , f = f , f + 3

	return asci


#facteurs(n): décomposition d'un nombre entier n en facteurs premiers

def facteurs(n):
	F = []
	if n==1:
		return F
# recherche de tous les facteurs 2 s'il y en a
	while n>=2:
		x,r = divmod(n,2)
		if r!=0:
			break
		F.append(2)
		n = x
# recherche des facteurs 1er >2
	i=3
	rn = np.sqrt(n)+1
	while i<=n:
		if i>rn:
			F.append(n)
			break
		x,r = divmod(n,i)
		if r==0:
			F.append(i)
			n=x
			rn = np.sqrt(n)+1
		else:
			i += 2
	return F