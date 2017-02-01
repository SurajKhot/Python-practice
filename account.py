
class InsufficientBalError(Exception):
	pass
	
	def __init__(self,msg):
		super().__init__(msg)

class Account:
	def __init__(self,acc_no,balance,min_bal):
		self.acc_no=acc_no
		self.balance=balance
		self.min_bal=min_bal
		
	def withdraw(self,amnt):
		if self.balance-amnt<self.min_bal:
			raise InsufficientBalError()
		self.balance=self.balance-amnt
		return self.balance
