import logging
logging.basicConfig(filename='myprogram.log', level=logging.DEBUG)

data=[]

class Info:
		def __init__(self):
			self.add()
		def add(self):
			try:
				x=int(input("Enter Data"))
				data.append(x)
				print(data)
				logging.debug(data)
			except Exception as e:
				logging.exception(e)
				raise e
obj=Info()
