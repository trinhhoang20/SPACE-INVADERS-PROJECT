CPSC 386: Introduction to Game Design - Fall 2022
Project One, Space Invaders, due Sunday, 2 Oct 2022 (by 2359)
In this assignment, you will create the Space Invaders game, based on the Alien Invasions! code 
from Project One. The image resources you will need (ship, ship animation destruction, bunker, 
different types of aliens, alien animation destruction, and ufo destruction) will all have to be created 
using an Image editing tool such as Inkscape or Gimp. The audio resources you will need can be 
captured using an audio editor such as Audacity from an online version of Space Invaders.
Online versions can be found on Youtube, or by searching on Google.
Classic Space Invaders has several differences from the Alien Invasions! Game. You will need to 
complete the following:
1. You will need PyCharm, Pygame, and Python 3 installed on your computer.
2. Using classic Space Invaders as a guide, and using an Image editor such
as Inkscape or Gimp, create the four types of aliens shown above, the
traditional Space Invaders ship, and the bunkers to hide behind.
3. The aliens must include a simple, slow, two-state animation while they are
moving (it looks better if alternating aliens are synchronized). Aliens must have a different
image when they explode (could show a simple, fast animation as well).
4. A UFO should move across the screen at random intervals. It makes a continuous oscillating
sound as it moves. If it is destroyed, it shows its (random) value instead of an explosion.
CPSC 386 – SPACE INVADERS -- project one – page 1 of 3
5. The ship must have a fast. animated explosion (8-12 frames) when it is destroyed. Be sure to
move the pixels of the exploding parts around from frame to frame. (Note: the ship we used in
Alien Invasions! Is not the same as that used in Classic Space Invaders.)
6. Create a LAUNCH screen, that shows the name of the game (in white and green), the aliens 
and their values, and the menus for Play Game and High Scores. The start screen should 
show at the beginning of each game, including if you have just lost a game.
7. Add lasers to the aliens, so they can shoot back at the ship. Use a random number generator
and a timer (pygame.time.get_ticks()) so they don’t shoot too often.
8. Add bunkers to the game that the ship can hide behind. The bunker can be damaged by both
the ship’s and aliens’ lasers. Use a random number generator to set the bunker’s pixels to
transparent when a laser strikes a part of the bunker to avoid a bite-out-of-a-sandwich look.
Use the Python Imaging Library to set the pixels.
9. Submit the zipped contents to Canvas AND submit to Canvas a GIF file showing your program 
running. Do not put the GIF file inside the zip file. Convert mov, mp4 etc files to GIF before 
submitting.
Submission
Turn in the code for this homework by uploading all of the Python source files you created, the 
images directory, and the sounds directory as a zip file to Canvas. You must also take a screen 
recording of your game playing, convert it to a GIF format, AND submit the GIF file to Canvas.
You may work as a team of up to TWO team members; be sure to submit the names of all team 
members. Both team members should understand all aspects of the implementation.
Individuals submitting assignments on their own may discuss this homework assignment with other 
students, however the work you submit must have been completed on your own.
To complete your submission, print the following sheet, fill out the spaces below, and submit it to the 
professor in class by the deadline. Failure to follow the instructions exactly will incur a 10% penalty 
on the grade for this assignment.
CPSC 386 – SPACE INVADERS --- project one – page 2 of 3
CPSC 386: Introduction to Game Design - Fall 2022
Project One, Space Invaders, due Sunday, 2 Oct 2022 (by 2359)
Your names (up to two members if submitting as a team)
_________________________________________________________________
Verify each of the following items and place a checkmark in the correct column. Each item incorrectly marked 
will incur a 5% penalty on the grade for this assignment. There is a 10% per day late penalty -- projects 
submitted after 72 hours will receive no credit.
Completed Not
Completed SPACE INVADERS
 
The game has a startup screen that shows the name of the game, the values and 
images of the aliens, and has a Play Game and High Scores menu. 
  The high scores are stored on disk, and are displayed when the menu is selected.
  Aside from the UFO, the game has 3 types of aliens, created using a pixel editor. 
 
A UFO alien moves across the screen at random, infrequent intervals. It was 
created using a pixel editor, and it shows its value when it is destroyed.
 
The ship was created using a pixel editor. It also has an animated (8-12 pixel 
frame) for destruction. 
 
The aliens have simple, two-frame animations for movement. They also have a 
simple (3-4 frame) animation for destruction. 
 
The aliens can shoot lasers back at the ship at infrequent, random intervals. 
Alien lasers can destroy the bunkers, and can collide with ship lasers.
 
Bunkers allow the ship to hide from the aliens’ lasers, but they are damaged by 
aliens’ or ship’s lasers. Use the Python Imaging Library for pixel manipulation.
  Ominous background music becomes faster as the number of aliens decrease.
  Pycharm IDE shows green checkmarks for every Python source file.
  Project directory pushed to new GitHub repository listed above
 
Project directory has been pushed using a GitHub client, not by manually 
dragging-and-dropping files onto the GitHub web page.
Comments on your submission
CPSC 386 – project one – page 3 of 
