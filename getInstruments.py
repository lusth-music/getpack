import os
import urllib.request
from html.parser import HTMLParser

class parseClass(HTMLParser):
  def handle_starttag(self, tag, attrs):
    if(tag == "a"):
      instrument = attrs[0][1].split('.')[0]
      
      print("Preparing getpack workspace")
      if not os.path.exists("./tempGetpackWorkspace"):
        os.mkdir("./tempGetpackWorkspace")
      os.chdir("./tempGetpackWorkspace")
      os.system("rm -f *")

      print("Downloading instrument sample pack: " + instrument)
      os.system("getpack \'"+instrument+"\'")
      print(instrument)

      print("Cleaning up getpack workspace")
      os.system("rm -f *")
      os.chdir("..")
      os.rmdir("./tempGetpackWorkspace")
      print("Finished downloading instument sample pack: " + instrument + '\n')


def main():
  url = "http://beastie.cs.ua.edu/songlib/samples/"
  try:
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
  except:
    print("Error: could not reach songlib sample library")

  parser = parseClass()
  parser.feed(text.strip())

main()
