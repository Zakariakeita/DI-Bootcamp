class Phone():
	def __init__(self,phone_number):
		self.phone_number=phone_number	
		self.call_history=[]
		self.messages=[]

	def add(self,string):
		self.call_history.append(string)
	
	def add2(self,string):
		self.messages.append(string)

	def name(self):
		return self.name

	def Call(self,other_phone):
		call1=f'{self.phone_number} have call {other_phone}'
		self.call_history.append(call1)
		
		
	def show_call_history(self):
		for i in self.call_history:
			print(i)

	def send_message(self,other_phone,content):
		dic={'to':other_phone,'from': self.phone_number, 'content':content}
		self.messages.append(dic)
		
	def show_messages(self):
		for i in self.messages:
			print(i)
			
	def show_outgoing_messages(self):
		for i in self.messages:
			for j in i.keys():
				if j=='to':
					print(i)
	def show_incoming_messages(self):
		for i in self.messages:
			for j in i.keys():
				if j=='from':
					print(i)


Keita=Phone('75456790')
Sanou=Phone('70908789')
Keita.Call(Sanou.phone_number,Sanou)
Keita.send_message(Sanou.phone_number,Sanou,' How are u')
Sanou.send_message(Keita.phone_number,Keita,'come here')
Keita.send_message(Sanou.phone_number,Sanou,'How old are you')
Sanou.send_message(Keita.phone_number,Keita,'15 year old')
Keita.send_message(Sanou.phone_number,Sanou,'good aftrenoon')
print('\n')
print("KEITA call history :")
Keita.show_call_history()
print('\n')
print("SANOU call history :")
Sanou.show_call_history()
print('\n')
print("KEITA messages : ")
Keita.show_messages()
print("outgoings : ")
Keita.show_outgoing_messages()
print("incomings : ")
Keita.show_incoming_messages()
print('\n')
print("SANOU messages : ")
Sanou.show_messages()
print("outgoings : ")
Sanou.show_outgoing_messages()
print("incomings : ")
Sanou.show_incoming_messages()











