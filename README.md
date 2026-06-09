# 🚀 Oh-My-Special
![Oh-My-Special Logo](Previews/logo.png)

A lightweight, extensible custom shell built in Python.  
Designed for learning how real terminal environments, command parsing, and system-level interactions work under the hood.

---

## 📌 Overview

**Oh-My-Special** is a Python-based mini shell that replicates core terminal behaviors such as navigation, command execution, and directory listing — with a focus on clarity, customization, and future extensibility.

It is not a replacement for CMD/PowerShell, but a learning-focused shell emulator.

---

## ✨ Features

- 🖥️ Custom CLI prompt system
- 📂 Directory navigation (`cd`)
- 📄 File listing (`ls`)
- 🎨 Colored terminal output (via `colorama`)
- ⚙️ Command parser system
- 🧠 Extensible command architecture (`Commands` class)
- 🔁 Interactive REPL loop (planned/active)

---

## 🧱 Project Structure

```text
oh-my-special/
│
├── main.py           # Entry point (REPL loop)
├── commands.py       # Command logic & execution
├── config.py         # Optional configuration (future)
└── README.md
```

## Installation 

**Start** by copying the repository :
```
git clone https://github.com/sarimgamerop-cloud/oh-my-special.git
cd oh-my-special
```
***Note:*** cloning the repository in the ``C:/Users`` or ``/home`` is recommended.

**Install the required fonts:**
- # For Windows 10/11 :
  
  ```
  powershell
  irm https://github.com/ryanoasis/nerd-fonts/releases/latest/download/IosevkaTerm.zip -OutFile iosevka.zip Expand-Archive iosevka.zip -DestinationPath iosevka
  ```
  after the downloading is complete , you will see a ``iosevka.zip`` in the current-directory , extract the zip
  and select all the fonts and install them by right clicking on the selected files. then hit install.

- # Linux :
- 
  **Linux** user can either install the fonts by using their package manager , or either by downloading them.
  # Arch:

  ```
  sudo pacman -S ttf-iosevka-nerd
  ```
  # Fedora

  ```
  sudo dnf install nerd-fonts-iosevka
  ```
