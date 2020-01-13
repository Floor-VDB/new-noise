import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))
import pyperclip
from random import randrange
import random
import string

sentences = ["electric, energy nodes, attractors, transmitters, conductors",
             "What would it mean to step outside of this carefully structured system?",
             "a tasteful assertion of ownership",
             "a model that encourages contamination, borrowing, stealing, and horizontal blur.",
             "conceive of a work positioned within the material and discursive technologies of distributed media.",
             "social information circulating in theoretically unlimited quantities ",
             "New strategies are needed to keep up with commercial distribution, decentralization, and dispersion.",
             "You must fight something in order to understand it.",
             "circulation, distribution, and dissemination become a crucial part of the work",
             "with a twist of the kaleidoscope things resolve themselves",
             "it tended to shun social communication, excommunicating itself through incomprehensibility",
             "Embodied in their embrace of the codes of the culture industry",
             "resist easy assimilation into a market-driven art system",
             "preference for distribution-oriented modes",
             "situating the work at a singular point in space and time turns it, a priori, into a monument",
             "mass-market artistic production is usually consumed privately",
             "art grounded in distributed media can be seen as a political art",
             "a person, no matter how passive a component of the capitalist consciousness industry, must be considered a producer",
             "The art world stinks; it is made of people who collectively dig the shit",
             "having ingested art information and raw material from the shared world, pissing his time away",
             "The art world is a collection of people who dig the dirt, or pay the artist to dig it for him, to get a “piece” of the action—the  games  people  play—for  personal  fun  and  profit ",
             "often he is more calculating; he wants things to be as interesting as possible; to give and have return pleasure; to contribute to the life-enhancing social covenant.",
             "The Industrial Revolution and its consequences have been a disaster for the human race.",
             "an erratic component that consists of unpredictable events that follow no discernible pattern, and a regular component that consists of long-term historical trends.",
             "It is not possible to make a LASTING compromise between technology and freedom, because technology is by far the more powerful social force",
             "there are the methods of propaganda, for which the mass communication media provide effective vehicles.",
             "ostensibly designed to benefit individuals, but in practice they usually serve as methods for inducing individuals to think and behave as the system requires. ",
             "Each new step in the assertion of control over the human mind will be taken as a rational response to a problem that faces society",
             "Thus control over human behavior will be introduced not by a calculated decision of the authorities but through a process of social evolution",
             "Did you ever wonder what made him tick, what forces shaped him, what may have molded him?",
             "Damn kid.  Probably copied it.  They're all alike.",
             "we've been spoon-fed baby food at school when we hungered for steak... the bits of meat that you did let slip through were pre-chewed and tasteless.",
             "This is our world now... the world of the electron and the switch, the beauty of the baud. ",
             "My crime is that of curiosity.  My crime is that of judging people by what they say and think, not what they look like.",
             "My crime is that of outsmarting you, something that you will never forgive me for",
             "Here and now we offer you a taste of our liberation frequency, provided by us for your satisfaction and excitement.",
             "Stuck by the deadly rhythm of the production line.",
             "Ideals corrupted and echoes from the past about ideas once held true are shining like untouchable constellations.",
             "why not try and live for a change and turn that glimmering into bright shining creation",
             "We are not stupid, but if we are treated like ingrates we will start to act like children. ",
             "why not try and live for a change and turn that glimmering into bright shining creation",
             "new noise and new voices and new canvases to become something more",
             "Strict in our style but with a touch of elegance and freedom",
             "It’s never been safe to live in a world that teaches us to respect property and disregard human life.",
             "Tonight we can be as mighty as tannhäuser and we can tumble excited down the labyrinths and the turns knowing that derive` is potent.",
             "Fight fire with fire and everything will burn. Yeah.",
             "you can't stop us all... after all, we're all alike."
             ]

recent_value = pyperclip.paste()

def change_char(s, p, r):
    return s[:p]+r+s[p+1:]

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        if int(randrange(0,10))<7:
            recent_value = tmp_value
            pony = change_char(str(recent_value), randrange(len(str(recent_value))), random.choice(string.ascii_letters))
            pyperclip.copy(str(pony))
            recent_value = str(pony)
        else:
            recent_value = tmp_value
            pony = change_char(str(recent_value), randrange(len(str(recent_value))), random.choice(sentences))
            pyperclip.copy(str(pony))
            recent_value = str(pony)
    time.sleep(0.1)





