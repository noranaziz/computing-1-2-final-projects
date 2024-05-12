# to run this on replit, go to https://replit.com/@noranaziz/GCC-App?v=1


from tkinter import *
import requests
import json


# global variables:
location = ["Pick a location", "Montgomery, Alabama", "Juneau, Alaska", "Phoenix, Arizona", "Little Rock, Arkansas", "Sacramento, California", "Denver, Colorado", "Hartford, Connecticut", "Dover, Delaware", "Honolulu, Hawaii", "Tallahassee, Florida", "Atlanta, Georgia", "Boise, Idaho", "Springfield, Illinois", "Indianapolis, Indiana", "Des Moines, Iowa", "Topeka, Kansas", "Frankfort, Kentucky", "Baton Rouge, Louisiana", "Augusta, Maine", "Annapolis, Maryland", "Boston, Massachusetts", "Lansing, Michigan", "St. Paul, Minnesota", "Jackson, Mississippi", "Jefferson City, Missouri", "Helena, Montana", "Lincoln, Nebraska", "Carson City, Nevada", "Concord, New Hampshire", "Trenton, New Jersey", "Santa Fe, New Mexico", "Raleigh, North Carolina", "Bismarck, North Dakota", "Albany, New York", "Columbus, Ohio", "Oklahoma City, Oklahoma", "Salem, Oregon", "Harrisburg, Pennsylvania", "Providence, Rhode Island", "Columbia, South Carolina", "Pierre, South Dakota", "Nashville, Tennessee", "Austin, Texas", "Salt Lake City, Utah", "Montpelier, Vermont", "Richmond, Virginia", "Olympia, Washington", "Charleston, West Virginia", "Madison, Wisconsin", "Cheyenne, Wyoming"]
city = ""
state = ""
choice = ""
chosen = ""
fajr = ""
thuhr = ""
asr = ""
maghreb = ""
isha = ""

# beginning of app. scroll down to the prayer timer class to see final project.
class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.title("GCC App")
    self.geometry("500x400")
    # the following code (allows user to advance to different frames/pages) was used from https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
    container = Frame(self)
    container.pack(side = "top", fill = "both", expand = True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    self.frames = {}
    # adds each class to an array of frames, outputting each one and raising them to the user's view (see showFrame) when needed. the default frame that is shown to the user is HomePage
    for F in (HomePage, AboutUs, OurBylaws, PrayerTimer, ContactUs):
      pageName = F.__name__
      frame = F(parent = container, controller = self)
      self.frames[pageName] = frame
      frame.configure(background = "#262f36")
      frame.grid(row = 0, column = 0, sticky = "nsew")
    self.showFrame("HomePage")
  
  # is called whenever the respective button is clicked on the home page. it "shows" a frame (one of the classes) and replaces it with the original one.
  def showFrame(self, pageName):
    # show a frame for the given page name
    frame = self.frames[pageName]
    frame.tkraise()


# this is the home page, the page that is shown when the program is run. it consists of 4 buttons, 3 of which are grayed out as they are not a part of the final project, but are a part of my honors project (which i will not be showcasing). upon clicking on the button labeled "Prayer Timer", the user will be taken to the PrayerTimer class/frame. Respective labels and buttons are initialized and outputted.
class HomePage(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller
    self.titleFont = ("Helvetica", 20, "bold italic")
    self.homeLbl = Label(self, text = "Final Project", font = self.titleFont, background = "#262f36", foreground = "white")
    self.homeLbl.pack(side = "top", fill = "x", pady = 10)
    self.homeBtn1 = Button(self, text = "About Us", foreground = "#262f36", background = "white", command = lambda: controller.showFrame("AboutUs"), state = "disabled")
    self.homeBtn2 = Button(self, text = "Our Bylaws", foreground = "#262f36", background = "white", command = lambda: controller.showFrame("OurBylaws"), state = "disabled")
    self.homeBtn3 = Button(self, text = "Prayer Timer", foreground = "#262f36", background = "white", command = lambda: controller.showFrame("PrayerTimer"))
    self.homeBtn4 = Button(self, text = "Contact Us!", foreground = "#262f36", background = "white", command = lambda: controller.showFrame("ContactUs"), state = "disabled")
    self.homeBtn1.pack()
    self.homeBtn2.pack()
    self.homeBtn3.pack()
    self.homeBtn4.pack()


# THIS CLASS IS NOT PART OF THE FINAL PROJECT
class AboutUs(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)  
    self.titleFont = ("Helvetica", 20, "bold italic")
    self.controller = controller
    self.aboutLbl = Label(self, text = "About Us", font = self.titleFont, background = "#262f36", foreground = "white")
    self.missionLbl = Label(self, text = "Mission Statement", font = ("Helvetica", 15), background = "#262f36", foreground = "white")
    self.statementLbl = Label(self, text = "'Create a diversified Islamic Community\nirrespective of race, age, skin color, \nfinancial status and country of origin. \nConsistent with the principles and teachings of Islam.'", background = "#262f36", foreground = "white")
    self.spaceLbl = Label(self, text = "", background = "#262f36", foreground = "white")
    self.historyLbl = Label(self, text = "History of Geist Community Center", font = ("Helvetica", 15), background = "#262f36", foreground = "white")
    self.datesLbl = Label(self, text = "3/15/2017 – Received confirmation from Fishers planning\n department to build a mosque.\n4/30/2017 – Floor plan was finalized.\n12/6/2017 – First Day of Construction.\n1/4/2018 – Building plan was officially approved \nby City of Fishers. All required permits have been received.\n4/14/2018 – First Adhan at Geist Community Center.", background = "#262f36", foreground = "white")
    self.aboutLbl.pack(side = "top", fill = "x", pady = 10)
    self.missionLbl.pack()
    self.statementLbl.pack()
    self.spaceLbl.pack()
    self.historyLbl.pack()
    self.datesLbl.pack()
    self.homeBtn = Button(self, text = "Go back to home page", foreground = "#262f36", background = "white", command = lambda: controller.showFrame("HomePage"))
    self.homeBtn.pack(side = "bottom")


# THIS CLASS IS NOT PART OF THE FINAL PROJECT
class OurBylaws(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.titleFont = ("Helvetica", 20, "bold italic")
    self.controller = controller
    self.bylawsLbl = Label(self, text = "Our Bylaws", font = self.titleFont, background = "#262f36", foreground = "white")
    self.bylawsLbl.pack(side = "top", fill = "x", pady = 10)
    self.homeBtn = Button(self, text = "Go back to home page", foreground = "#262f36", background = "white", command = lambda: controller.showFrame("HomePage"))
    self.homeBtn.pack()


# FINAL PROJECT STARTS HERE
# this is the prayer timer page, which actually consists of 2 separate parts: the location picker, and the prayer time output. the initial part is the location picker. the necessary widgets (labels, dropdown, and buttons) are created and outputted.
class PrayerTimer(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.titleFont = ("Helvetica", 20, "bold italic")
    self.controller = controller
    self.locLbl = Label(self, text = "Please choose your location:", font = self.titleFont, background = "#262f36", foreground = "white")
    self.submitBtn = Button(self, text = "Submit", foreground = "#262f36", background = "white", command = lambda: [self.getPrayers(), self.getDate(), self.showPrayerTimer()])
    self.homeBtn = Button(self, text = "Go back to home page", foreground = "#262f36", background = "white", command = lambda: controller.showFrame("HomePage"))
    self.locLbl.pack()
    self.dropdownMenu()
    self.submitBtn.pack()
    self.homeBtn.pack()
  
  def showLocMenu(self):
    # since i wanted to use the same variables in the prayer time page *after* they were set to a value, i destroyed all of the widgets and outputted some new ones instead of navigating to a different frame (which would require a new class) altogether, and as a result, complicate the variable settings.
    for widget in self.winfo_children():
      widget.destroy()
    # several labels and 2 buttons (one to navigate to the prayer times and one to go back to the home page) are initialized and outputted (they are the same variables as the ones in the initialization method above)
    self.locLbl = Label(self, text = "Please choose your location:", font = self.titleFont, background = "#262f36", foreground = "white")
    self.submitBtn = Button(self, text = "Submit", foreground = "#262f36", background = "white",command = lambda: [self.getPrayers(), self.getDate(), self.showPrayerTimer()])
    self.homeBtn = Button(self, text = "Go back to home page", foreground = "#262f36", background = "white", command = lambda: self.controller.showFrame("HomePage"))
    self.locLbl.pack()
    self.dropdownMenu()
    self.submitBtn.pack()
    self.homeBtn.pack()
  
  def showPrayerTimer(self):
    # since i wanted to use the same variables *after* they were set to a value, i destroyed all of the widgets and outputted some new ones instead of navigating to a different frame (which would require a new class) altogether.
    for widget in self.winfo_children():
      widget.destroy()
    # initialized lots of labels to output prayer times and button to get back to the home page.
    self.dateLbl = Label(self, text = todaysDate, font = ("Helvetica", 15, "bold italic"), background = "#262f36", foreground = "white")
    self.spacerLbl = Label(self, text = "", background = "#262f36", foreground = "white")
    self.fajrLbl = Label(self, text = "Fajr: " + fajr, font = ("Helvetica", 12), background = "#262f36", foreground = "white")
    self.thuhrLbl = Label(self, text = "Thuhr: " + thuhr, font = ("Helvetica", 12), background = "#262f36", foreground = "white")
    self.asrLbl = Label(self, text = "Asr: " + asr, font = ("Helvetica", 12), background = "#262f36", foreground = "white")
    self.maghrebLbl = Label(self, text = "Maghreb: " + maghreb, font = ("Helvetica", 12), background = "#262f36", foreground = "white")
    self.ishaLbl = Label(self, text = "Isha: " + isha, font = ("Helvetica", 12), background = "#262f36", foreground = "white")
    self.dateLbl.pack()
    self.spacerLbl.pack()
    self.fajrLbl.pack()
    self.thuhrLbl.pack()
    self.asrLbl.pack()
    self.maghrebLbl.pack()
    self.ishaLbl.pack()
    self.spacerLbl.pack()
    self.homeBtn = Button(self, text = "Go back to home page", foreground = "#262f36", background = "white", command = lambda: [self.showLocMenu(), self.controller.showFrame("HomePage")])
    self.homeBtn.pack()
  
  def dropdownMenu(self, *args):
    # create dropdown of locations ("capital, state" format) that the user can choose from. this DOES affect the prayer times.
    global location
    global city
    global state
    global choice
    commaIndex = 0
    choice = StringVar(self)
    choice.set(location[0])
    dropdown = OptionMenu(self, choice, *location)
    dropdown.config(background = "white")
    dropdown["menu"].config(background = "white")
    dropdown.pack()
    choice.trace('w', self.getLocation)

  def getLocation(self, *args):
    # sets city and state variables to the user's choice from the dropdown menu.
    global city
    global state
    global chosen
    global choice
    chosen = choice.get()
    for i in range(len(chosen)):
      if "," == chosen[i]:
        commaIndex = i
    city = chosen[:commaIndex]
    state = chosen[commaIndex + 2:]
    print("City: " + city)
    print("State: " + state)

  def getPrayers(self, *args):
    # receives url of prayer time api, which will be used to output the respective prayer times depending on the city and state that the user picked. 
    global city
    global state
    global fajr
    global thuhr
    global asr
    global maghreb
    global isha
    url = "https://api.aladhan.com/v1/timingsByCity?city={}&state={}&country=US&method=2".format(city, state)
    results = requests.get(url)
    print(results)
    json = results.json()
    print(json)
    print()
    timings = json["data"]["timings"]
    print(timings)
    fajr = timings["Fajr"]
    thuhr = timings["Dhuhr"]
    asr = timings["Asr"]
    maghreb = timings["Maghrib"]
    isha = timings["Isha"]
  
  def getDate(self):
    # receives url of prayer time api, which will be used to outpupt the current date ("weekday, month day year" format)
    global todaysDate
    url = "https://api.aladhan.com/v1/timingsByCity?city={}&state={}&country=US&method=2".format(city, state)
    results = requests.get(url)
    json = results.json()
    apiDate = json["data"]["date"]["gregorian"]
    weekday = apiDate["weekday"]["en"]
    month = apiDate["month"]["en"]
    day = apiDate["day"]
    year = apiDate["year"]
    todaysDate = "Today is: " + weekday + ", " + month + " " + day + " " + year
# FINAL PROJECT ENDS HERE


# THIS CLASS IS NOT PART OF THE FINAL PROJECT
class ContactUs(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.titleFont = ("Helvetica", 20, "bold italic")
    self.controller = controller
    self.contactLbl = Label(self, text = "Contact Us!", font = self.titleFont, background = "#262f36", foreground = "white")
    self.contactLbl.pack(side = "top", fill = "x", pady = 10)
    self.homeBtn = Button(self, text = "Go back to home page", command = lambda: controller.showFrame("HomePage"))
    self.homeBtn.pack()

# run the program
def main():
  app = App()
  app.mainloop()

if __name__ == "__main__":
  main()
