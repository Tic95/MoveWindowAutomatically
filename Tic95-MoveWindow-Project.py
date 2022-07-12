import win32gui
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()           #RUN as admin for moving the task manager 
    except:
        return False

if is_admin():
    
    
    def winEnumHandler( hwnd, ctx ):
        global lhwnd
        if win32gui.IsWindowVisible( hwnd ):
            lhwnd[hwnd] = win32gui.GetWindowText( hwnd ) #create a dictionarry with the hwnd and the name of all the Visible Window

    lhwnd = dict()
    win32gui.EnumWindows( winEnumHandler, None )



    valist = list(lhwnd.values())# Create a list with all the names of the visible window
    keylist = list(lhwnd.keys())#create a list with all of their hwnd
    def moveWindow(NameOfTheWindow,CoordX,CoordY,SizeX,SizeY):
        for valnum in valist:
            if (NameOfTheWindow in valnum): #check if the name of the window you wanna move is in the valist 

                index = valist.index(valnum)              #if it is take the position of the object
        win32gui.MoveWindow(keylist[index], CoordX,CoordY,SizeX,SizeY,True)#move the window 
        win32gui.MoveWindow(keylist[index], CoordX,CoordY,SizeX,SizeY,True)#again just for the multi screen users

    #(nameOfTheWindow,CoordX,CoordY,SizeX,SizeY)     #PUT THE WINDOW YOU WANNA MOVE IN THIS FUNCTION 
    moveWindow("Discord",-1920,0,1290,825)           #PUT THE WINDOW YOU WANNA MOVE IN THIS FUNCTION 
    moveWindow("Task Manager",-630,330,130,350)      #PUT THE WINDOW YOU WANNA MOVE IN THIS FUNCTION 
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
