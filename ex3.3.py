Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def right_justify(string):
	a = ''
	l = len(string)
	for i in range(0,70-l):
		a = a+' '
	a = a + string
	print a

	
>>> right_justify('hello this string is justified to right')
                               hello this string is justified to right
>>> 
>>> 
>>> 
>>> ex 3.4
SyntaxError: invalid syntax
>>> "---> ex 3.4 <---"
'---> ex 3.4 <---'
>>> def do_twice(func)
SyntaxError: invalid syntax
>>> def do_twice(func):
	func()
	func()

	
>>> def print_spam():
	print 'spam'

	
>>> do_twice(print_spam)
spam
spam
>>> do_twice(right_justify('Hello World...!!!'))
                                                     Hello World...!!!

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    do_twice(right_justify('Hello World...!!!'))
  File "<pyshell#12>", line 2, in do_twice
    func()
TypeError: 'NoneType' object is not callable
>>> 
KeyboardInterrupt
>>> 
