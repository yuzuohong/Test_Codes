
class PythonDemo:
  #To create a new GUID use the commands:
  #>>> import pythoncom
  #>>> print(pythoncom.CreateGuid())
  _reg_clsid_ = "{D1B0A23F-0B6E-46D6-8880-744DBFFB86CD}"
  _reg_progid_ = "Python.Demo"
  _reg_desc_ = "Python Demo COM Server"
  _public_methods_ = ["HelloWorld", "HelloYou", "SplitString"]

  #-Function HelloWorld-------------------------------------------------
  def HelloWorld(self):
    import platform, struct
    return "Hello World from Python " + platform.python_version() + \
      " on " + platform.system() + " (" + platform.architecture()[0] + \
      ")"

  #-Function HelloYou---------------------------------------------------
  def HelloYou(self, name="Anybody"):
    return "Hello " + str(name) + " from Python"

  #-Function SplitString------------------------------------------------
  def SplitString(self, val, item=None):
    import string
    if item != None:
      item = str(item)
    return val.split(item)

#-Sub Main--------------------------------------------------------------
def main():
  import sys, win32com.server.register
  if sys.argv[1].lower() == "--register":
    print("Registering COM server...")
  if sys.argv[1].lower() == "--unregister":
    print("Unregistering COM server...")
  win32com.server.register.UseCommandLine(PythonDemo)

#-Main------------------------------------------------------------------
if __name__=="__main__":
  main()
