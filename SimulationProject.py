import sys, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit
from PyQt5.QtCore import QSize    
import numpy as np

#Snake Class
class Snake:
    
    animal = 'Snake'
    BirthYear = 0
    DeathYear = -1
    nextBirth = -1

    # Parameterized constructor
    def __init__(self, time): 
        self.BirthYear = time
        
    # Determines randomly the time of death by natural causes for this snake
    def calcDeathYear(self): 
        value = self.BirthYear + random.randint(5, 7) 
        self.DeathYear = value
        return value
    
    # 1-3 years for a snake to fully develope and have offspring every year
    def calcNextBirth(self, time): 
        value = time + random.uniform(1, 3)
        self.nextBirth = value
        return value
    
    #Print function
    def __str__(self):
        myString = 'A {:s} was born on year: {:d},\n'.format(self.animal,\
                            self.BirthYear)
        return myString
    
    #print function for snake object
    def __repr__(self):
        SnakeStr = self.__str__()
        return SnakeStr

    #deletes the object
    def __del__(self):
        myString = ("A Snake has died after {:d} years.\n".format(self.DeathYear - self.BirthYear))
        return myString

#Hawk Class
class Hawk:
    
    animal = 'Hawk'
    BirthYear = 0
    DeathYear = -1
    nextBirth = -1

    # Parameterized constructor
    def __init__(self, time): 
        self.BirthYear = time
        
    # Determines randomly the time of death by natural causes for this snake
    def calcDeathYear(self): 
        value = self.BirthYear + random.randint(7, 9) 
        self.DeathYear = value
        return value
    
    # Calculates when the next snake gets born
    def calcNextBirth(self, time): 
        value = time + random.uniform(5, 6)
        self.nextBirth = value
        return value
    
    #Print function for error checking
    def __str__(self):
        myString = 'A {:s} was born on year: {:d},\n'.format(self.animal,\
                            self.BirthYear)
        return myString
    
    #print function for snake object
    def __repr__(self):
        HawkStr = self.__str__()
        return HawkStr

    #deletes the object
    def __del__(self):
        myString = ("A Hawk has died after {:d} years.\n".format(self.DeathYear - self.BirthYear))
        return myString

#Snake Class
class Rabbit:
    
    animal = 'Rabbit'
    BirthYear = 0
    DeathYear = -1
    nextBirth = -1
    
    # Parameterized constructor
    def __init__(self, time): 
        self.BirthYear = time
        
    # Determines randomly the time of death by natural causes for this snake
    def calcDeathYear(self): 
        value = self.BirthYear + random.randint(3, 5) 
        self.DeathYear = value
        return value
    
    # Calulates year of maturity to have next offspring. Rabbits can mature in 7 months to 1 year
    def calcNextBirth(self, time): 
        value = time + random.uniform(.7, 1)
        nextBirth = value
        return value
    
    #Print function for error checking
    def __str__(self):
        myString = 'A {:s} was born on year: {:d},\n'.format(self.animal,\
                            self.BirthYear)
        return myString
    
    #print function for snake object
    def __repr__(self):
        RabbitStr = self.__str__()
        return RabbitStr

    #deletes the object
    def __del__(self):
        myString = ("A Rabbit has died after {:d} years.\n".format(self.DeathYear - self.BirthYear))
        return myString

#Simulation Class
class Simulation:
    snakePop = 0
    hawkPop = 0
    rabbitPop = 0
    time = 0

    #Constructor
    def __init__(self, window):
        self.Events = []
        self.window = window
    
    #Starts the simulation
    def Start(self):
        self.snakePop = 0
        self.hawkPop = 0
        self.rabbitPop = 0
        self.time = 0
        self.Events = []
        
        count = 0
        while count != 4:
            hawk1 = Hawk(self.time)
            self.hawkPop += 1
            
            snake1 = Snake(self.time)
            snake2 = Snake(self.time)
            self.snakePop += 2
            
            rabbit = Rabbit(self.time)
            self.rabbitPop += 1
            self.Events.append(rabbit)

            self.Events.append(hawk1)
            self.Events.append(snake1)
            self.Events.append(snake2)
            count +=1

        
        self.window.eventsField.clear()
        for e in self.Events:
            self.window.eventsField.insertPlainText(e.__str__())
            self.calcEvent(e)
    
    #Calculates death year and nextbirth for the animal
    def calcEvent(self, event):
        event.calcDeathYear()
        event.calcNextBirth(self.time)

    #Advances time by x years
    def advanceTime(self, years):
        for i in range (years):
            self.time +=1
            print(self.time)
            self.window.eventsField.clear()
            for e in self.Events:
                #Snake or rabbit dies to their predator
                if e.animal != 'Hawk' and e.BirthYear != self.time and self.time != 1:
                    if e.animal == 'Snake':
                        randOdds = random.random()
                        odds = randOdds
                        #50% chance of dying in a year from a predator
                        if (odds < .50):
                            #snake dies to hawk
                            self.snakePop -=1
                            self.window.eventsField.insertPlainText('A snake was killed by a hawk\n')
                            self.Events.remove(e)
                            del e
                            continue

                    elif e.animal == 'Rabbit':
                        randOdds = random.random()
                        odds = randOdds
                        #65% chance of dying in a year from a predator
                        if (odds < .65):
                            #rabbit dies to hawk/snake
                            self.rabbitPop -=1
                            self.window.eventsField.insertPlainText('A rabbit was killed by a hawk/snake\n')
                            self.Events.remove(e)
                            del e
                            continue

                    
                #Animal Dies of natural causes
                if e.DeathYear < self.time:
                    if e.animal == 'Hawk':
                        self.hawkPop -= 1
                        self.Events.remove(e)
                        self.window.eventsField.insertPlainText('A hawk has died after {:d} years.\n'.format(self.time - e.BirthYear))
                        del e
                        continue
                    elif e.animal == 'Rabbit':
                        self.rabbitPop -= 1
                        self.Events.remove(e)
                        self.window.eventsField.insertPlainText('A Rabbit has died after {:d} years.\n'.format(self.time - e.BirthYear))
                        del e
                        continue
                    elif e.animal == 'Snake':
                        self.snakePop -= 1
                        self.Events.remove(e)
                        self.window.eventsField.insertPlainText('A Snake has died after {:d} years.\n'.format(self.time - e.BirthYear))
                        del e
                        continue

                if e.nextBirth < self.time and e.BirthYear != self.time:
                    self.birthAnimal(e)




    def birthAnimal(self,event):

        #1-2 hawks per hawk per year
        if event.animal == 'Hawk':
            count = random.randint(1,2)
            for i in range(count):
                hawk = Hawk(self.time)
                self.calcEvent(hawk)
                self.hawkPop += 1
                self.Events.append(hawk)
                self.window.eventsField.insertPlainText(hawk.__str__())

        #1-5 rabbits per rabbit per year
        elif event.animal == 'Rabbit':
            count = random.randint(1,5)
            for i in range(count):
                rabbit = Rabbit(self.time)
                self.calcEvent(rabbit)
                self.rabbitPop += 1
                self.Events.append(rabbit)
                self.window.eventsField.insertPlainText(rabbit.__str__())

        #3-5 snakes per snake per year.
        elif event.animal == 'Snake':
            count = random.randint(3,5)
            for i in range(count):
                snake = Snake(self.time)
                self.calcEvent(snake)
                self.snakePop += 1
                self.Events.append(snake)
                self.window.eventsField.insertPlainText(snake.__str__())

    
        
    
#GUI Class
class Window(QMainWindow):
    #Fonts
    timeFont = QtGui.QFont("Times", 24, QtGui.QFont.Bold)
    btnFont = QtGui.QFont("Times", 18, QtGui.QFont.Bold)
    eventsFont = QtGui.QFont("Times", 18)
    statsFont = QtGui.QFont("Times", 18)
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        #Simulation
        self.sim = Simulation(self)
        #Set the boundaries for our Window
        self.setGeometry(500,500,1000,600)
        self.setMinimumSize(QSize(1000, 600))
        self.setMaximumSize(QSize(1000, 600))
        
        #Set title for Window
        self.setWindowTitle("Simulation World") 
        
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   
        
        #Set Layout
        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  
        gridLayout.setRowStretch(1,2)
        
        #Make Label
        self.timeLabel = QLabel() 
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setFont(self.timeFont)
        self.timeLabel.setText('Press Start to Begin')
       
        #Add Label to layout
        gridLayout.addWidget(self.timeLabel, 1, 1)
        
        
        # Add text fields
        self.eventsField = QPlainTextEdit(self)
        self.eventsField.insertPlainText("Events.\n")
        self.eventsField.setFixedHeight(400)
        self.eventsField.setFixedWidth(325)
        self.eventsField.setFont(self.eventsFont)
        
        self.statsField = QPlainTextEdit(self)
        self.statsField.insertPlainText("Stats.\n")
        self.statsField.setFixedHeight(400)
        self.statsField.setFixedWidth(325)
        self.statsField.setFont(self.statsFont)
        
        #Add Fields to GUI
        gridLayout.addWidget(self.eventsField,1,0)
        gridLayout.addWidget(self.statsField,1,2)
        
        #Create buttons
        exitBtn = QPushButton('Exit', self)
        timeBtn = QPushButton('Advance Time', self)
        startBtn = QPushButton('Start', self)
        
        #Button Font
        exitBtn.setFont(self.btnFont)
        startBtn.setFont(self.btnFont)
        timeBtn.setFont(self.btnFont)
        
        #Add ActionListeners to Butttons
        exitBtn.clicked.connect(self.exit_click)
        timeBtn.clicked.connect(self.time_click)
        startBtn.clicked.connect(self.start_click)
        
        #Add Buttons to the gridLayout
        gridLayout.addWidget(exitBtn, 2, 2)
        gridLayout.addWidget(timeBtn, 2, 1)
        gridLayout.addWidget(startBtn, 2, 0)

        self.show()
        
    #Exit Button Clicked
    def exit_click(self):
        sys.exit()
    
    #Start Simulation Was Clicked
    def start_click(self):
        self.timeLabel.setText('Starting')
        self.sim.Start()
        self.display_stats()
        
    #Advance time button Clicked
    def time_click(self):
        self.timeLabel.setText('Loading')
        self.sim.advanceTime(30)
        self.timeLabel.setText('Year: {:d}'.format(self.sim.time))
        self.display_stats()
    
    #Displays stats of the animals 
    def display_stats(self):
        myString = "Time in Year(s): {:d}\n\n".format(self.sim.time)
        myString +="Snake Population : {:d}\n".format(self.sim.snakePop)
        myString +="Hawk Population  : {:d}\n".format(self.sim.hawkPop)
        myString +="Rabbit Population :{:d}\n".format(self.sim.rabbitPop)
                    
        self.statsField.setPlainText(myString)
        
            
#End of Window Class

app = QtWidgets.QApplication(sys.argv)
mainWin = Window()
mainWin.show()
sys.exit(app.exec_())
