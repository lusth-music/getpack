import os

def main():
  fp = open("index.html", "r")
  instruments = fp.read().split()

    
  os.mkdir("./temp")
  os.chdir("./temp")
  #for i in range(0, len(instruments), 1):
    #os.system("sudo getpack \'"+instruments[i]+"\'")
    #os.system("sudo rm *")
  os.chdir("..")
  os.rmdir("./temp")

main()
