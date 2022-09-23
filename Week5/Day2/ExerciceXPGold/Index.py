
class BankAccount():
	def __init__(self,balance,username,password,authenticated=False):
		self.password=password
		self.balance=balance
		self.username=username
		self.authenticated=False
	
	def deposit(self,val,name,passw):
		v=self.authenticate(passw,name)
		if v==True:
			print('\n')
			print(f' \tAccount Balance: {self.balance} ')
			try:
				val=int(val)
				if val>0:
					print(f' \t depot of {val} in your Account')
					self.balance=self.balance+val
					print(f' \t your new balance is {self.balance}')
				else:
					raise Exception('Your depot value is negative')
			except:
				print('\t Something is going wrong deposit of {val} is not done')
		else:
			print('\t Authentificate Failed , Authentificate yourself first')
		
	def withdraw(self,val,name,passw):
		v=self.authenticate(passw,name)
		if v==True:
			print('\n')
			print(f' \t Account Balance: {self.balance}')
			try:
				val=int(val)
				if val>0:
					print(f' \t withdraw of {val} in your Account')
					self.balance=self.balance-val
					print(f' \t  your new balance is {self.balance}')
				else:
					raise Exception('Your withdraw value is negative')
			except:
				print(f'\t Something is going wrong withdraw of {val} is not done')
		else:
			print('\t Authentificate Failed , Authentificate yourself first')

	def  authenticate(self,passw,name):
		print('\n')
		print(' Authenticate ')
		if passw==self.password and name==self.username:
			print(f'\t authenticate of {name} Success')
			return True
		else:
			print(f'\t authenticate of {name} Failed')
			return False
			

class MinimumBalanceAccount(BankAccount):
	def __init__(self,balance,username,password,authenticated=False,mini=0):
		super().__init__(balance,username,password,authenticated=False)
		self.minimum_balance=mini
	
	def withdraw(self,val,name,passw):
		v=self.authenticate(passw,name)
		if v==True:
			print('\n')
			print('withdraw')
			print(f' \t Account Balance: {self.balance}')
			try:
				val=int(val)
				if val>0 and self.balance>self.minimum_balance:
					print(f' \t withdraw of {val} in your Account')
					self.balance=self.balance-val
					print(f' \t your new balance is {self.balance}')
				else:
					raise Exception('Your withdraw value is negative')
			except:
				print(f'\t Something is going wrong withdraw of {val} is not done')
		else:
			print('\t Authentificate Failed , Authentificate yourself first')

	
	

coris=MinimumBalanceAccount(-65000,'sheldon','sheldonlee')
coris.deposit(400,'sheldon','sheldonlee')
coris.withdraw(200,'dd','gg')



