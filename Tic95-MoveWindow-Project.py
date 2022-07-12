import win32gui
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    def winEnumHandler( hwnd, ctx ):
        global lhwnd
        if win32gui.IsWindowVisible( hwnd ):
            lhwnd[hwnd] = win32gui.GetWindowText( hwnd )

    lhwnd = dict()
    win32gui.EnumWindows( winEnumHandler, None )



    valist = list(lhwnd.values())
    keylist = list(lhwnd.keys())
    def moveWindow(NameOfTheWindow,CoordX,CoordY,SizeX,SizeY):
        for valnum in valist:
            if (NameOfTheWindow in valnum):

                index = valist.index(valnum)
        win32gui.MoveWindow(keylist[index], CoordX,CoordY,SizeX,SizeY,True)
        win32gui.MoveWindow(keylist[index], CoordX,CoordY,SizeX,SizeY,True)

    #(nameOfTheWindow,CoordX,CoordY,SizeX,SizeY)     #PUT THE WINDOW TO MOVE IN THIS FUNCTION 
    moveWindow("Discord",-1920,0,1290,825)           #PUT THE WINDOW TO MOVE IN THIS FUNCTION 
    moveWindow("Task Manager",-630,330,130,350)      #PUT THE WINDOW TO MOVE IN THIS FUNCTION 
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
