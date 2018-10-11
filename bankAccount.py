''' 
Bank account that has two attributes:
1. Owner
2. Balance

and two methods:
1. deposit
2. withdraw (may not exceed available balance)
'''

class Account:
	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance

	def __repr__(self):
		return f"Hi {self.owner}, your balance is ${self.balance}."

	def deposit(self,dep_amt):
		self.balance = self.balance + dep_amt
		print("\nDeposit of $%s was successful! Your new balance is $%s." % (dep_amt,self.balance))

	def withdraw(self,wd_amt):
		if self.balance >= wd_amt:
			self.balance = self.balance - wd_amt
			print("\nWithdraw successful! Your new balance is $%s." % self.balance)
		elif self.balance == 0:
			print("Cannot complete request! You don't have jack shit!")
		else:
			print("\nFunds not available. Withdraw amount exceeds balance!")

acct1 = Account('Mike',500)
print(acct1)

input1 = input("Press D to deposit or W to withdraw: ").lower()
if input1 == 'd':
	deposit1 = int(input("How much would you like to deposit? $"))
	acct1.deposit(deposit1)
elif input1 =='w':
	wd1 = int(input("How much would you like to withdraw? $"))
	acct1.withdraw(wd1)
else:
	print('Please press D or W only.')