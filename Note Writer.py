import time
import pickle

try:
	note=open('notebook.dat','rb').read().split('\n')
except Exception:
	print('No default notebook was found, created one.')
	writenote=open('notebook.dat','wb')

notelist=[]
	
while True:
	selection=int(input('(1) Read the notebook \n(2) Add note\n(3)Edit a note\n(4)Delete a note\n(5)Save and quit\n\nPlease select one:'))
	if selection==1:
		writenote=open('notebook.dat','wb')
		for i in notelist:
			print(i)
		pickle.dump([],writenote)
		writenote.close()
			
	elif selection==2:
		newnote=input('Write a new note:')
		addnote=notelist.append(newnote+':::'+time.strftime('%X %X'))
		
	elif selection==3:
		print('The list has '+str(len(notelist))+' notes.')
		indexchange=input('Which of them will be changed?:')
		print(notelist[int(indexchange)])
		change=input('Give the new note:')
		notelist.pop(int(indexchange))
		notelist.insert(int(indexchange),change+':::'+time.strftime('%X %X'))
		
	elif selection==4:
		print('The list has '+str(len(notelist))+' notes.')
		indexremove=input('Which of them will be deleted?:')
		print('Deleted note ',notelist[int(indexremove)-1])
		notelist.pop(int(indexremove)-1)
			
	elif selection==5:
		note=open('notebook.dat','rb')
		note.close()
		print('Notebook shutting down, thank you.')
		break
