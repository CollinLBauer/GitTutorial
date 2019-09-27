## Welcome to the ACM and WIC GitHub workshop!

### Instructions for Workshop



#### 1. Fork the reposityory to your own GitHub account.

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

#### 5. Let's merge the new branch to master.

```
git checkout master 
git merge mybranch
git commit -m “merge to master”
git push
```

The changes you made should now be in the master branch.

Congratulations! You know git!

---

[Helpful git tutorial](https://github.com/Rafase282/MyFCCWiki/blob/master/Back-End-Development-Certification/Git/Lesson-Save-your-Code-Revisions-Forever-with-Git.md)  
[git 101 presentation](https://drive.google.com/open?id=1tyiOKLQVVEwVtHhDUOF-Wli4dZYBR7r5GwrPSvAy8BE)
