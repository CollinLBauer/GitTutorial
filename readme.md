## Welcome to the GitHub workshop!

**Prerequesites**: Make a GitHub account and install git to your computer.

Windows and Mac users can download git **[here](https://git-scm.com/)**  
Linux users can install git with `sudo apt-get install git`

**Note**: We will be running git from the command line terminal. If you are new to terminal, feel free to ask for help.

---

### Instructions for Workshop

<br/>

1. Fork this repository to your own GitHub account with the "Fork" button on the top right of the GitHub page

   - This should take you to a brand new copy of this repository under your GitHub account.

<br/>

2. Clone your new fork!

   - `git clone https://github.com/my_name/GitTutorial.git`  

     *Replace `my_name` with your GitHub account name*

   - This will download the repository and place it in a folder called GitTutorial.

   - Now, type `cd GitTutorial` to move into that folder.

<br/>

3. Create a new file and add it to your fork

   - Make a new file, `first_last.txt`, replacing first and last with your name.

     - Bash users: `touch first_last.txt`
     - Powershell users: `New-Item first_last.txt`  
     
     *Note: using a unique name for this file is important, or it will cause issues later.*


   - Edit the file by typing in their name and some fun fact about yourself!  

   - Once you're done, add it to your branch by typing in the following commands.

     ```
     git status
     git add my_name.txt
     git commit -m “my first commit”
     git push
     ```

   - Git will ask you to log in with your GitHub account. For some, it may ask this every time, which gets annoying. There's a way around this, which you can read about **[here](https://stackoverflow.com/questions/35942754/how-to-save-username-and-password-in-git-gitextension)**.  
     Just be aware that using that trick  will let anyone else with access to your computer computer make git changes in your name.
   
   You've now made your first push with git! You should be able to see your changes on GitHub. Now, let's talk about branching.

<br/>

4. Make a new branch of your repository

   Branches are an important aspect of git, but not an easy one to wrap your head around. These steps may seem silly right now, but this skill will be immensely helpful in the future!
   
   - Type `git checkout -b mybranch`  
     This creates a new branch that may have separate changes from the default `master` branch.
   
     - *Tip: You can see what branches your repo has by typing* `git branch`
   
   - Now change something in your file from earlier and push it to the new branch.
   
     ```
     git commit -m “new branch”
     git push --set-upstream origin mybranch
     ```

     *Note:* `-m` *in the commit lets you set what is called a commit message. This can be whatever you want, but if you do* **not** *include this, it might take you to a strange text editor. Ask for help if this happens!*


    Great! If you look at your GitHub repository, you should now have *two* branches: **master** and **mybranch**

<br/>

5. Merge the new branch to master

   - Type in the following commands:  
     
     ```
     git checkout master 
     git merge mybranch
     git commit -m “merge to master”
     git push
     ```

   The changes you made should now be in the master branch!

   When working with git for real, you may run into something called a ***merge conflict***. This happens when two branches have different changes on the same file. You can read more about resolving these conflicts **[here](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line)**.

<br/>

6. Make a pull request to upstream

   Since your repository is a fork of someone else's repository, you can ask to merge your changes with their master!  
   You can do this on GitGub by clicking **New pull request**. Add a message and click **submit**, then we can accept and merge it!

<br/>

7. *Congratulations!* You now know git!

---

### Further reading
- [Helpful git tutorial](https://github.com/Rafase282/MyFCCWiki/blob/master/Back-End-Development-Certification/Git/Lesson-Save-your-Code-Revisions-Forever-with-Git.md)  
- [git 101 presentation](https://drive.google.com/open?id=1tyiOKLQVVEwVtHhDUOF-Wli4dZYBR7r5GwrPSvAy8BE)
