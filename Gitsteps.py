# Start jupiter notebook
# /Applications/anaconda3/bin/jupyter_mac.command ; exit;


# Steps to onnect my python spyder with github
# WD set to repository 
import os
print(os.getcwd())  
path="/Users/Blanca/ironhack/prework-datamad-no-solutions"
os.chdir(path)

# Commit 
!git add .
!git add gitsteps.py
!git add bus.py
# Commit all files 
!git commit -am "Bus 100% done!"


# Comit only selected files 
# !git commit -m "Snail and well 100% done!"
!git push origin master

# pull existing repository to merge with files you want to push
# !git remote add origin https://github.com/bfmilan/prework-datamad-no-solutions.git

# Add the file to local git
# !git add temp.py
# Push the file to github.com
# !git push -u origin master


# If you want to remove the file from the Git repository and the filesystem, use:
# !git rm example.txt
# !git commit -m "remove example.txt"

# But if you want to remove the file only from the Git repository and not remove it from the filesystem, use:
# git rm --cached file1.txt
# git commit -m "remove file1.txt"

# And to push changes to remote repo
