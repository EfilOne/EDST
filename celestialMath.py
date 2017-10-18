class cm():

	import math

	def __INIT__(self):

		# Astronomical Constants
		self.c 	   = 299792458				# Speed of Light             - in m/s
		self.h 	   = 6.62607004081e-34		# Planck Constant            - in J.s
		self.hbar  = self.h/(2*math.pi())	# Inverse of h               - in J.s
		self.G 	   = 6.6725985e-11			# Gravitational Constant     - in m^3(Kg*s^2)
		self.k 	   = 1.380626e-23			# Boltzmann Constant         - in J k^-1
		self.sigma = 5.6705119e-8			# Stephan-Boltzmann Const.   - in W/(m^2*K^4)
		self.Ks    = 1.361					# Solar Constant             - in W/m^2
		self.g 	   = 9.80665				# Gravitational Acceleration - in m/s^2
		self.b 	   = 2.897772917e-3			# Wien's Displacement Const. - in m K

		# Astronomical Units and Physical Constants
		self.AU 	   = 149600000000 		# Astronomical Unit        - in meters
		self.parsec    = 3.08567758074e16 	# Parsec                   - in meters
		self.ly 	   = 9463000000000000 	# Light Year               - in meters
		self.solM 	   = 1.9889e30			# Solar Mass               - in kilograms
		self.solRad    = 695700000			# Solar Radius             - in meters
		self.solLum    = 3.828e26			# Solar Luminosity         - in watts
		self.solTemp   = 5780				# Solar Temperature        - in kelvins
		self.solMinCHZ = 0.77				# Sol Inner habitable rad. - in AU
		self.solMaxCHZ = 1.18				# Sol Outer Habitable rad. - in AU
		self.solAbsMag = 4.77				# Solar Absolute Magnitude - in magnitudes
		self.eMass 	   = 5.9722e24			# Earth's Mass             - in kilograms
		self.eAtmoP    = 101325				# Earth's Atmos. Pressure  - in pascals

		# Payment Coefficients for Stars
		self.Scoef  = 2880
		self.Dcoef  = 33737
		self.HNcoef = 54309

		# Payment Coefficients for Planets
		self.planets 	 = 720
		self.ClassI  	 = 3974
		self.ClassII_HMC = 23168
		self.MRich 		 = 52292
		self.WW_Earth	 = 155581
		self.ammonia 	 = 232619
		self.TCRock 	 = 223971
		self.TCHMC 		 = 241607
		self.TCWW 		 = 279088

	def starPay(self,k,m):
		return k+(m*k/66.25)

	def worldPay(self,k,m):
		return k+(3*k*m**0.1999977/5.3)

	def meanDensity(self,m,r):
		return ((self.solM*m)/((4/3)*math.pi()*pow(self.solRad*r,3)))/1000

	def peakWL(self,temp):
		return (self.b/temp)*(10**9)

	def luminosity(self,r,temp):
		return (4*math.pi()*(self.solRad*r)**2*self.sigma*temp**4)*1000

	def fluxDensity(self,r,temp):
		lum = self.luminosity(r,temp)
		return lum/(4*math.pi()*(self.solRad*r)**2)

	def absMag(self,r,temp):
		lum = self.luminosity(r,temp)
		return self.solAbsMag-2.5*math.log((lum/self.solLum)*1000)

	def innerCHZ(self,r,temp):
		return (self.solMinCHZ*r)*(temp/self.solTemp)**2 # Not sure here, may need to convert radius into meters then toward AU

	def outerCHZ(self,r,temp):
		return (self.solMaxCHZ*r)*(temp/self.solTemp)**2 # Not sure here, may need to convert radius into meters then toward AU

	def galactocentric(self,x,y,z):
		R 		= math.sqrt((x-25)**2+(y-25900)**2)
		rho 	= math.degrees(math.atan2((y-25900),x-25))
		Z 		= z+21
		return [R,rho,Z]

class match():
	def __INIT__(self):

		# Stars Classification list
		self.StarClasses 	= 	['O','B','A','F','G','K','M','L','T','Y','TTS','AeBe','W','WN','WNC','WC','WO',
								 'CS','C','CN','CJ','CH','CHd','MS','S','D','DA','DAB','DAO','DAZ','DAV','DB','DBZ',
								 'DBV','DO','DOV','DQ','DC','DCV','DX','N','H','X','SupermassiveBlackHole',
								 'A_BlueWhiteSuperGiant','F_WhiteSuperGiant','M_RedSuperGiant','M_RedGiant',
								 'K_OrangeGiant','RoguePlanet','Nebula','StellarRemnantNebula']

		#Planets Classification list
		self.planetClasses  =  ['Icy body','Rocky ice body','Rocky body','Metal rich body','High metal content body',
								'Water world','Earthlike body','Ammonia world','Sudarsky class I gas giant',
								'Sudarsky class II gas giant','Sudarsky class III gas giant','Sudarsky class IV gas giant',
								'Sudarsky class V gas giant','Water giant','Water giant with life', 'Gas giant with water based life',
								'Gas giant with ammonia based life','Helium gas giant','Helium rich gas giant']

	def starMatch(self,stype):
		if stype in self.StarClasses:
			return True
		else:
			return False

	def planetMatch(self,ptype):
		if ptype in self.planetClasses:
			return True
		else:
			return False
