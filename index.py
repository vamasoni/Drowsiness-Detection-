from tkinter import *
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "floral white")

	def function(): 
		os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()
		
	root.title("DROWSINESS DETECTION")
	Label(root, text="DROWSINESS DETECTION",font=("times new roman",20),fg="black",bg="DeepSkyBlue2",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)
	Button(root,text="Run using web cam",font=("times new roman",20),bg="sky blue",fg='white',command=function).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	Button(root,text="Exit",font=("times new roman",20),bg="sky blue",fg='white',command=root.destroy).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

	root.mainloop() 