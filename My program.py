#IIEC_RISE My program

import cv2
import os
import pyttsx3

print('Manual of this program :')
pyttsx3.speak('Manual of this program')
print('you can talk with this program and ask some questions which is given in manual')
print('hi, hello, how are you, your creater name, why created you, what kind of operations you can do \n')
print('you can open or run these program')
print('click picture,  my computer,  c drive,  google chrome,  notepad,  windows media player,  command prompt,  document folder,   calculator,  jupyter notbook,  system setting,  close any program,  open notepad file,  exit \n')

print('Please wirte task in undersoodable and easy english')

def seepic() :
	print('you want to see your picture? ')
	pyttsx3.speak('you want to see your picture')
	print('yes or no ?  : ', end='')
	e = input()

	if ('yes' in e.lower()) :
		print('how much time you want to see you picture')
		pyttsx3.speak('how much time you want to see you picture ')
		print('enter time in second  : ')
		pyttsx3.speak('enter time in second ')
		t = input()
		T = (int(t))*1000
				
		cv2.imshow('mypicture', photo)
		cv2.waitKey(T)
		cv2.destroyAllWindows()

	elif ('no' in e.lower()) :
		print('ok , but your picture seved in storage')
		pyttsx3.speak('ok , but your picture seved in storage')
						
	else :
		print("sorry! I can't understand your answer")
		pyttsx3.speak("sorry! I can't understand your answer")
		print('try again')
		pyttsx3.speak('try again')
		seepic()

def takepic() :
	print('when you want to click picture , fisrtly click on camera window and then press c button')
	pyttsx3.speak('when you want to click picture , fisrtly click on camera window and then press c button')
			
	cap = cv2.VideoCapture(0)
		
	while True :
		status, photo = cap.read()
		
		cv2.imshow('your picture', photo)
		
		if cv2.waitKey(1) == ord('c')	:
			cv2.imwrite('{}.png' . format(n) ,photo)
			cv2.destroyAllWindows()
			cap.release()

			print('do you wanna see your picture? \n yes or no')
			pyttsx3.speak('do you wanna see your picture?,  yes or no')
			q = input()
			if ('yes' in q.lower()) or ('yup' in q.lower()) or ('sure' in q.lower()) or ('why not' in q.lower()) :
				print('how much time you want to see you picture')
				pyttsx3.speak('how much time you want to see you picture')
				print('enter time in second : ')
				pyttsx3.speak('enter time in second')
				t = input()
				T = (int(t))*1000
				
				cv2.imshow('mypicture', photo)
				cv2.waitKey(T)
				cv2.destroyAllWindows()
			
				print('want to retake \n type yes or not')
				pyttsx3.speak('want to retake,  type yes or not')
				a = input()
				if ('yes' in a) or ('yup' in a) or ('sure' in a) or ('why not' in a) or ('take' in a) or ('retake' in a) :
					takepic()
				elif ('no' in a) or ('nope' in a) :
					print('ok')
			elif ('no' in q.lower()) or ('nope' in q.lower()) :
				print('ok , but your picture seved in storage')
				pyttsx3.speak('ok , but your picture seved in storage')
				break
		
			break



def pic() :
	print('enter name for your picture')
	pyttsx3.speak('enter name for your picture')
	n = input()
	while True :
		status , photo = cap.read()
		cv2.imwrite('{}.png' . format(n),photo)
		cv2.imshow('hi',photo)
		cv2.waitKey(1)
		print('press c if you want to click your picture')
		pyttsx3.speak('click on CMD window and then press c if you want to click your picture')
		a = input()
		if 'c' in a :
			print('want to retake your pic or not')
			pyttsx3.speak('want to retake your pic or not')
			x = input()
			if 'yes' in x :
				pic()
			elif 'no' in x:
				break
		break  
	  
	pic()
            
	cv2.destroyAllWindows()
	cap.release()
	
#Program start from here

print('hi ,  nice to meet you')
pyttsx3.speak('hi,  nice to meet you')

while True:
	
	print('how I can help you : ' , end='')
	pyttsx3.speak('how I can help you')
	y = input()
	x = y.lower()

#Talking Program From Here
	
	if ('hi' in x) or ('hello' in x) :
		print(x)
		pyttsx3.speak(x)
	
	elif ('how' in x) and ('are' in x) and ('you' in x) :
		print("couldn't be better")
		pyttsx3.speak("couldn't be better")
		print('and what about you : ' , end='')
		pyttsx3.speak('and what about you ')
		p = input()
		q = p.lower()

		if (('i am' in q) and (('fine' in q) or('well' in q) or ('good' in x))) or ((('could not' in q) or ("couldn't" in q)) and ('be' in q) and (('better' in q) or ('good' in q))) :
			print('Good')
			pyttsx3.speak('Good')

		elif ('not' in q) and (("i'm" in q) or ('i am' in q)) and (('not good' in q) or('not better' in q) or ('bad' in q) or ('not well' in q) or ('not fine' in q)) :
			print('why!')
			pyttsx3.speak('why!')
			print('what happend with you....')
			pyttsx3.speak('what happend with you....')
			print("tell me")
			pyttsx3.speak('tell me')
			print("I'm your friend, right.... so tell me : " , end='')
			pyttsx3.speak("I'm your friend , right.... so tell me")
			w = input()
			how = w.lower()
			
			if ('nothing' in how) or ('leave it' in how) or ('forget it' in how) or (('forget' in how) and ('it' in how)):
				print('no problem, if you cannot tell me')
				pyttsx3.speak('no problem, if you cannot tell me')

			else :
				print('this is very bad, but forget about it, this is nothing, just a bad moment, so foget this')
				pyttsx3.speak('this is very bad, but forget about it, this nothing, just a bad moment, so foget this')
				print("keep smile on your face, like this :) ")
				pyttsx3.speak('keep smile on your face, like this')
				print('now Is everything ok?')
				pyttsx3.speak('now Is everything ok?')
				b = input()
				a = b.lower()
				
				if ('yes' in a) or ('ok' in a) or ('yup' in a) or ('fine' in a) or ('something' in a) :
					print("that's good")
					pyttsx3.speak("that's good")
					
							

		else :
			print("i cannot understand you reply")
			pyttsx3.speak('i cannot understand you reply')
			
	elif (('you' in x) or ('your' in x)) and (('creater' in x) or ('created' in x)) and ('name' in x) :
		print('Sunil Sirvi created me')
		pyttsx3.speak('Sunil Sirvi created me')

	elif ('why' in x) and ('created' in x) and ('you' in x) :
		print('to easy your work.')
		pyttsx3.speak('to easy your work.')
	
	elif ('what' in x) and ('you' in x) and ('do' in x) :
		print('I can do many things, like talk to you and run some program for you etc.')
		pyttsx3.speak('I can do many things, like talk to you and run some program for you etc.')



#Run System's Program Form Here

	if (('take' in x) or ('click' in x) or ('capture' in x)) and (('picture' in x) or ('image' in x) or ('photo' in x) or ('pic' in x)) :
		
		print('I am giving your picture name is your name ')
		pyttsx3.speak('I am giving your picture name is your name ')
		print('enter your name : ')
		pyttsx3.speak('enter your name')
		n = input()
		print('when you want to click picture , fisrtly click on camera window and then press c button')
		pyttsx3.speak('when you want to click picture , fisrtly click on camera window and then press c button')
			
		cap = cv2.VideoCapture(0)
			
		while True :
			status, photo = cap.read()
			
			cv2.imshow('your picture', photo)
			
			if cv2.waitKey(1) == ord('c')	:
				cv2.imwrite('{}.png' . format(n) ,photo)
				cv2.destroyAllWindows()
				cap.release()

				print('do you wanna see your picture? \n yes or no')
				pyttsx3.speak('do you wanna see your picture?,  yes or no')
				q = input()
				if ('yes' in q.lower()) or ('yup' in q.lower()) or ('sure' in q.lower()) or ('why not' in q.lower()) :
					print('how much time you want to see you picture')
					pyttsx3.speak('how much time you want to see you picture')
					print('enter time in second : ')
					pyttsx3.speak('enter time in second')
					t = input()
					T = (int(t))*1000
				
					cv2.imshow('mypicture', photo)
					cv2.waitKey(T)
					cv2.destroyAllWindows()
			
					print('want to retake \n type yes or not')
					pyttsx3.speak('want to retake,  type yes or not')
					a = input()
					if ('yes' in a) or ('yup' in a) or ('sure' in a) or ('why not' in a) or ('take' in a) or ('retake' in a) :
						takepic()
					elif ('no' in a) or ('nope' in a) :
						print('ok')
				elif ('no' in q.lower()) or ('nope' in q.lower()) :
					print('ok , but your picture seved in storage')
					pyttsx3.speak('ok , but your picture seved in storage')
					break
			
				break

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('this pc' in x) or ('my computer' in x)) :
		os.system('explorer')

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('c drive' in x) or ('C drive' in x) or ('C Drive' in x)) :
		os.system('explorer c:')

	elif (('run' in x ) or ('open' in x) or ('execute' in x) or ('play' in x)) and (('media' in x) or ('player' in x) or ('media player' in x)) :
		os.system('wmplayer')

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('google' in x) or ('chrome' in x)) :
		os.system('chrome')

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('notepad' in x) or ('editor' in x) or ('text editor' in x)) :
		os.system('notepad')

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('cmd' in x) or ('command' in x) or ('command line' in x) or ('command prompt' in x)) :
		os.system('start cmd.exe')

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('document' in x) or ('document list' in x) or ('Document' in x) or ('Document list' in x) or ('Document List' in x) or ('document List' in x)) :
		os.system('explorer :')

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('calc' in x) or ('calculator' in x) or ('Calculator' in x)) :
		os.system('calc')

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('jupyter' in x) or ('jupyter notebook' in x)) :
		os.system('jupyter notebook')

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('setting' in x) or ('settings' in x) or ('system' in x) or ('systems' in x)) :
		os.system('start ms-settings:')

	elif (('close' in x) or ('destroy' in x) or ('kill' in x)) and (('program' in x) or ('notepad' in x) or ('text file' in x) or ('editor' in x)) :
		print('enter program name : ')
		pyttsx3.speak('enter program name')
		f = input()
		os.system('taskkill/im {}.exe' . format(f))	

	elif (('run' in x) or ('open' in x) or ('execute' in x)) and (('notepad file' in x) or ('text file' in x) or ('editor file' in x)) :
		f = input('enter your file name : ')
		pyttsx3.speak('enter your file name' , end='')
		os.system(f)

	elif ('exit' in x) or ('stop' in x) :
		print('ok')
		pyttsx3.speak('ok')
		print('bye, see you soon')
		pyttsx3.speak('bye, see you soon')
		break
