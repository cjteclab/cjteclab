# Blog by cjteclab

## 2022-11-28

### Moving towards **VS Code**
After consideration, I decided to move from Vim as the main IDE to VS Code.

In the past few months, I decided to use vim as my main IDE in combination with tmux. I liked the terminal-based approach, the slim and fast working environment and of course was hyped by using just my keyboard for fast navigation and coding. Vim gave me the feeling of getting really into programming and being a technical nerd who is a convinced Linux user. So I learned the key bindings, configured my .vimrc file and installed different plug-ins. But at any time I missed something which I couldn't describe. Vim couldn't give me the feeling of overlooking my projects and files. Also, the use of all those plug-ins was ok but never fully convinced me. Furthermore, the fact that I have to use a different IDE on my windows laptop and for data science projects (jupyter notebook) doesn't make me happy.  
In this context, I watched some video snippets [1](https://www.youtube.com/watch?v=G5mtQhWNezQ) and [2](https://www.youtube.com/watch?v=tzr7hRXcwkw) and they convinced me to switch to VS Code and give it a try.  

#### Installed Extensions
- VIM : Vim emulation for Visual Studio Code
- Better Comments
- Python : IntelliSense
- Python Indent
- Python Test Explorer
- autoDocstring (you can change formatting style)
- AREPL for python

#### Settings
- Activate relative line numbers.

### Update 2022-12-02
So far, I am very happy with VS Code. But I missed Vim so much, that I made the decision to use both. I will use VS Code for large projects and when I need a overview of a project. And I will use Vim for daily tasks and coding sessions.

---

## 2022-12-09

### Ubuntu and its problems with the fan configuration
Some Ubuntu users maybe are familiar with the following issue. After you have booted your computer, you have to find out that the fan is running at full speed. You have no idea what happened? The last time you worked on your computer, everything was fine. The fan was quiet and run at normal speed. You didn't change any settings.
I can't tell you what's the problem behind this issue. But I can tell you that this issue occurs once in a while ([Source](https://askubuntu.com/a/1034036)).  
The last time I had to handle this issue, I couldn't fix it. Trying different fan settings in the BIOS didn't fix the issue. Erasing the hard disk and reinstalling Ubuntu didn't work either. In the end, I installed Windows. I don't know why, but after installing Windows, the fan was running at normal speed again.  

This time I tried to fix this issue by using **lm-sensor** and **fancontrol**, as it is described in many forums. I highly recommend the blog article at [iandw.com](https://iandw.net/2014/10/12/fancontrol-under-ubuntu-14-04-resolving-usrsbinpwmconfig-there-are-no-pwm-capable-sensor-modules-installed/), because the article describes some common errors while using **fancontrol**. The blog article handles the fan problem at Ubuntu 14.10, but it is still working at Ubuntu 22.04.

After I fixed the issue by using **lm-sensor** and **fancontrol**, my cpu fan is running at normal speed and without annoying noises again.

---
