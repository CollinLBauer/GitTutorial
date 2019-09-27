## Welcome to the ACM and WIC GitHub workshop!

Prerequesites: Make a GitHub account and install git to your computer.

Windows and Mac users can download git **[here](https://git-scm.com/)**  
Linux users can install git with `sudo apt-get install git`

### Instructions for Workshop

#### 1. Fork this repository to your own GitHub account

#### 2. Clone it!

```
git clone https://github.com/my_name/GitTutorial.git
```

#### 3. Create a new file and add it to your fork

Powershell users: `New-Item myFile.txt`  
Bash users: `touch myFile.txt`

Now Edit the file by typing in their name and some fun fact about yourself

```
git status
git add myFile.txt
git commit -m “my first commit”
git push
```

Great! You just made your first push with git! Now, let's talk about branching.

#### 4. Make a new branch of your repository

```
git checkout -b mybranch
```
You can see what branches your repo has by typing `git branch`.  
Now change something in your file from earlier and push it to the new branch.

```
git commit -m “new branch”
git push --set-upstream origin mybranch
```

Great! If you look at your GitHub repository, you should now have *two* branches: **master** and **mybranch**

#### 5. Merge the new branch to master

```
git checkout master 
git merge mybranch
git commit -m “merge to master”
git push
```

The changes you made should now be in the master branch.

#### 6. Make a pull request to upstream

Since your repository is a fork of someone else's repository, you can ask to merge your changes with their master!  
You can do this on GitGub by clicking **New pull request**. Add a message and click **submit**, then I can accept and merge it!

Congratulations! You know git!

---

[Helpful git tutorial](https://github.com/Rafase282/MyFCCWiki/blob/master/Back-End-Development-Certification/Git/Lesson-Save-your-Code-Revisions-Forever-with-Git.md)  
[git 101 presentation](https://drive.google.com/open?id=1tyiOKLQVVEwVtHhDUOF-Wli4dZYBR7r5GwrPSvAy8BE)
