# All cards available in a standard deck.
from classes import *

#TAs
cooper = TACard('Cooper, Owner of Jellybean', 1999, 1000)
tim = TACard('Tim Tu, Tyrant TA of Twos', 2222, 222)
anthony = TACard('Anthony, Defender of Ed', 1888, 1600)
ben = TACard('Ben, Maker of Games', 1300, 1000)
grace = TACard('Grace, Grading Grace', 2100, 1100)
gurkaran = TACard('Gurkaran, Prepper of Exams', 2000, 1000)
joanna = TACard('Joanna, Defender of Eighty Eights', 2888, 888)
jordan = TACard('Jordan, Bullet Journal Expert', 1200, 2200)
julie = TACard('Julie, Consumer of Spicy Ramen', 1717, 1717)
kevin_y = TACard('Kevin, Recoverer of Homework', 1080, 2250)
marie = TACard('Marie, Fan of Dodgers', 1234, 1534)
melody = TACard('Melody, Singer of Melodies', 1112, 1932)
patrick = TACard('Patrick, Writer of Software', 1000, 2300)
rajamani = TACard('Rajamani, Creator of this Lab', 1100, 2200)
roy = TACard('Roy, Crosser of Words', 2400, 1000)
serena = TACard('Serena, Watcher of Movies', 1200, 2100)
shaun = TACard('Shaun, Responder to Discord', 2100, 1200)


#Tutors
amit = TutorCard('Amit, Watcher of Sports', 1357, 1853)
amritansh = TutorCard('Amritansh, Listener of Western Classical music', 1024, 2048)
araav = TutorCard('Araav, Player of Chess', 1500, 2200)
ashwin = TutorCard('Ashwin, Player of Golf', 1920, 1080)
caitlin = TutorCard('Caitlin, Defender of Trader Joes', 1920, 1080)
cindy = TutorCard('Cindy, Photographer of Food', 2000, 1000)
kevin_m = TutorCard('Kevin ,Loading..', 1000, 2300)
klaire = TutorCard('Klaire, Collector of All', 2200, 1500)
laryn = TutorCard('Laryn, Lord of Lambdas', 2300, 1300)
peter = TutorCard('Peter, Writer of Blogs', 1100, 2300)
rohan = TutorCard('Rohan, Tech Writer of Mentors', 1500, 2200)
rohit = TutorCard('Rohit, Learner of Languages', 1100, 2100)
shivana = TutorCard('Shivana, Wielder of Two Majors', 2800, 900)



# Professors
alex = ProfessorCard('Alex, Little Schemer', 2400, 100)
albert = ProfessorCard('Albert, Lethargy Incarnate', 100, 2400)
catherine = ProfessorCard('Catherine, Referencer of Self', 1800, 1600)

# A standard deck contains all standard cards.
standard_cards = [cooper, tim, anthony, ben, grace, gurkaran, joanna, jordan, julie, kevin_y, marie, melody, patrick, rajamani, roy, serena, shaun, amit, amritansh, araav,
                    ashwin, caitlin, cindy, kevin_m, klaire, laryn, peter, rohan, rohit, shivana, alex, albert, catherine]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()