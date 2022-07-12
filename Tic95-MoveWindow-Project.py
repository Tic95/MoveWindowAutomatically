import win32gui






def winEnumHandler( hwnd, ctx ):
    global lhwnd
    if win32gui.IsWindowVisible( hwnd ):
        lhwnd[hwnd] = win32gui.GetWindowText( hwnd )

lhwnd = dict()
win32gui.EnumWindows( winEnumHandler, None )



valist = list(lhwnd.values())
keylist = list(lhwnd.keys())

for valnum in valist:
    if ("Discord" in valnum):

        index = valist.index(valnum)



print(keylist[index])
print(lhwnd)

win32gui.MoveWindow(keylist[index], -1920,0,1290,825,True)
win32gui.MoveWindow(keylist[index], -1920,0,1290,825,True)