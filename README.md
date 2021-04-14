# Rickroll-Detector

## What's the purpose of this script?
  This script can detect rickrolls whether it's a YT link or a bit.ly link or a shorturl link
  
## Pre-requisites
  1. Python version >= 3.7 and python added to PATH (Windows)<br />
  2. Git-scm installed and added to PATH (Windows)
  3. Chrome webbrowser
  4. Selenium package for python (Install using: __pip install selenium__)
  5. Requests package for python (Install using: __pip install requests__)
  
## Setting up the detector
  1. Clone the repository to any directory using the command :__git clone https://github.com/TheProgrammingArchive/Rickroll-Detector/__
  2. Once cloned navigate to the directory using cd and run installer.py using: python installer.py (WINDOWS) or python3 installer.py (LINUX/MACOS)
  3. If the os being used is windows then move to step [5].
  4. Navigate to the folder named "driver" and run the command chmod +x chromedriver
  5. Navigate back to the main folder
  
## Arguments available
  1. find_identity.py -c "link" -> Searches for the SME (Suggested video) of the link __(RECOMMENDED TO RUN THIS FIRST)__ and alerts the user if it flags a rickroll SME.
  2. find_identity.py -d "link" -> Prints video details (Title, Date, Views, Likes, Dislikes) as a list object.
  3. find_identity.py -od "link" -> Prints channel details (Channel name, Subscriber count)
  4. find_identity.py -cmt "link" -> Analyses the comments of the video for certain words related to a rick roll. Alerts user if specifications are met, if not prints upto 15 
  comments for the user to read and analyse. The comments are printed in the form of a list object
  5. find_identity.py -t "link" -> Analyses the title of the video and alerts the user if it flags a title with certain keywords.
  6. find_identity.py -chnc "link" -> Analyses channel name and alerts the user if it flags Rick Astley's official channel or other rick-roll related ones
  7. find_identity.py -pl "link" -> Analyses the name of the playlist in which the video may be located and alerts the user if it flags specific keywords. __(NOT RECOMMENDED TO   RUN THIS FIRST AS IF THE VIDEO ISN'T IN A PLAYLIST IT CAN BE VERY SLOW)__
  8. find_identity.py -plv "link" -> Prints all the videos inside the playlist as a list object.
  9. find_identity.py -dsc "link" -> Prints the description of the video

## Effective searching of a link
  It is advised to run the -c method first, if it doesn't flag a rick roll then proceed with -t, followed by -cmt, -chnc, -pl. __(RECOMMENDED TO FOLLOW THIS ORDER)__<br />
  If a rick-roll isn't flagged anywhere here then it is suggested to run -d, -od, -dsc, -plv __(THESE METHODS NEED TO BE MANUALLY ANALYSED)__
  
## Usage
  python3 find_identity.py -opt "link" (LINUX/MACOS) <br />
  find_identity.py -opt "link" (WIN)
  
__CERTAIN VIDEOS MAY PASS THROUGH ALL THE FLAGS IN THE SCRIPT. ONLY USE THIS SCRIPT IF YOU'RE SUSPICIOUS OF A LINK. IF THERE ARE NO SIGNS OF A RICKROLL PROCEED WITH THE LINK.__
