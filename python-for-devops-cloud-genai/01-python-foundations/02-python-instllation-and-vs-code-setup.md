# 🐍 Python Installation & Setup — Windows, WSL Ubuntu, and VS Code

This guide covers a complete Python development environment setup from scratch — for beginners and anyone who wants a professional-grade local setup on Windows.

📺 **Video Tutorial:** [Python Installation on Windows and WSL Ubuntu | VS Code Setup for Beginners](#)
📂 **Part of:** Python Foundation Series — Video #2

---

## 📋 Table of Contents

- [What You Will Set Up](#what-you-will-set-up)
- [Path 1 — Python on Windows](#path-1--python-on-windows)
- [Path 2 — WSL Ubuntu Setup](#path-2--wsl-ubuntu-setup)
  - [What is WSL and Why Use It?](#what-is-wsl-and-why-use-it)
  - [Installing WSL and Ubuntu](#installing-wsl-and-ubuntu)
  - [Installing Python Inside WSL Ubuntu](#installing-python-inside-wsl-ubuntu)
- [VS Code Installation and Extensions](#vs-code-installation-and-extensions)
- [Connecting VS Code to WSL](#connecting-vs-code-to-wsl)
- [Running Your First Python File](#running-your-first-python-file)
- [Recommended Project Folder Structure](#recommended-project-folder-structure)
- [Common Errors and Fixes](#common-errors-and-fixes)
- [Quick Reference Summary](#quick-reference-summary)

---

## What You Will Set Up

Before writing a single line of Python, you need three things in place:

| Component | Purpose | Analogy |
|-----------|---------|---------|
| **Python** | The language engine that reads and runs your code | Engine under the hood |
| **VS Code** | The editor where you write your code | Cockpit |
| **WSL Ubuntu** | A Linux environment inside your Windows machine | Professional kitchen inside your apartment |



---

## Path 1 — Python on Windows

### Step 1 — Download Python

Go to: **https://www.python.org/downloads/**

Click the yellow **"Download Python 3.x.x"** button. Always download the latest stable version.

### Step 2 — Run the Installer

Open the downloaded `.exe` file.

> ⚠️ **CRITICAL STEP — Do not skip this:**
> At the bottom of the installer screen, check the box that says **"Add Python to PATH"**
> This checkbox is **unchecked by default**. If you miss it, Python will not work from the terminal.

After checking that box, click **"Install Now"**.

**Why does PATH matter?**
When you type `python` in the terminal, Windows needs to know *where* Python is installed. PATH is that address. Without it, Windows simply says *"python? I don't know what that is"* — and nothing runs.

### Step 3 — Verify Installation

Open **Command Prompt** (`cmd` in Start menu) and run:

```bash
python --version
```

Expected output:
```
Python 3.x.x
```

Also verify pip (Python's package installer):

```bash
pip --version
```

If both show version numbers — **installation successful.**

If you see `'python' is not recognized` — PATH was not added. Reinstall Python and make sure to check that box.

> 💡 **Homework:** PATH can also be set manually through Windows Environment Variables. Try finding that setting yourself — search online for "how to add Python to PATH manually on Windows".

---

## Path 2 — WSL Ubuntu Setup

### What is WSL and Why Use It?

**WSL = Windows Subsystem for Linux**

WSL is a Linux environment that runs directly inside your Windows machine — no dual boot, no virtual machine, no separate hardware needed. It is built into Windows 10 and Windows 11.

**Why use WSL over plain Windows for Python?**

- Most production servers run **Linux** — AWS, Google Cloud, Azure all run Linux
- Your code will run the same way locally and on the server — no environment mismatch surprises
- Python tools, libraries, and scripts behave more predictably on Linux
- No Windows-specific path issues or permission errors
- **If you plan to work with data science, machine learning, DevOps, cloud, or web backend — WSL is the professional standard**

> 💬 *Windows is like a furnished apartment — comfortable and easy. WSL is like adding a professional kitchen inside that apartment. You still live in the same place, but now you can cook at a restaurant level.*

---

### Installing WSL and Ubuntu

**Requirements:**
- Windows 10 version 2004 or later, OR Windows 11
- Administrator access on your machine

#### Step 1 — Open PowerShell as Administrator

Right-click the Start button → select **"Windows PowerShell (Admin)"** or **"Terminal (Admin)"**

Run this single command:

```powershell
wsl --install
```

This one command installs **WSL 2** and **Ubuntu** automatically. Internet connection required — it will take a few minutes.

#### Step 2 — Restart Your Computer

Required after WSL installation. Do not skip this step.

#### Step 3 — First Ubuntu Launch

After restart, search **"Ubuntu"** in the Start menu and open it.

The first launch will take a few minutes — it is setting up a mini Linux system inside your Windows machine.

It will then ask you to create a **username and password**. This is your Linux user account — remember these credentials.

#### Step 4 — Verify Ubuntu is Running

```bash
cat /etc/os-release
```

You should see Ubuntu version details. WSL is ready.

---

### Installing Python Inside WSL Ubuntu

Ubuntu comes with Python pre-installed, but it may not be the latest version. Here is the proper way to set it up.

#### Step 1 — Update Ubuntu packages first

```bash
sudo apt update && sudo apt upgrade -y
```

> `sudo` means "run as administrator" in Linux. Always run this before installing anything new.

#### Step 2 — Install Python, pip, and venv

```bash
sudo apt install python3 python3-pip python3-venv -y
```

This installs three things:
- `python3` — the Python interpreter
- `python3-pip` — pip package manager
- `python3-venv` — virtual environment support (useful later)

#### Step 3 — Verify

```bash
python3 --version
pip3 --version
```

> ⚠️ **Important difference — Windows vs WSL:**
>
> | Environment | Command |
> |-------------|---------|
> | Windows | `python` |
> | WSL Ubuntu | `python3` |
>
> This is one of the most common confusion points for beginners. Both environments are separate — commands differ slightly.

---

## VS Code Installation and Extensions

VS Code is where you write your code. Download it once — it works for both Windows files and WSL files.

### Download and Install

Go to: **https://code.visualstudio.com/**

Download for Windows and run the installer.

During installation, make sure to check:
- ✅ **"Add to PATH"**
- ✅ **"Open with Code"** *(adds VS Code to the right-click context menu)*

---

### Must-Have Extensions

Install these two extensions before anything else.

#### Extension 1 — Python (by Microsoft)

`Ctrl+Shift+X` → Search **"Python"** → Install the one by Microsoft

**What it does:**
- Syntax highlighting — different parts of your code appear in different colors
- Variables, strings, and functions are visually distinct
- Makes reading and writing code significantly easier

#### Extension 2 — Pylance (by Microsoft)

Usually installs automatically alongside the Python extension. If not, search for it manually.

**What it does:**
- Acts as a real-time coding assistant
- Flags errors *as you type* — before you even run the code
- Auto-completes variable names, function names, and import paths
- Saves significant debugging time

---

### Optional — Color Themes

A good dark theme reduces eye strain during long coding sessions.

`Ctrl+K` → `Ctrl+T` to open theme picker

Popular options: **One Dark Pro**, **Dracula**, **Tokyo Night**

---

### Python File Extension

Every Python file **must** end in `.py`

```
main.py
calculator.py
data_analysis.py
```

Without `.py`, VS Code will not treat the file as Python.

---

## Connecting VS Code to WSL

VS Code has built-in WSL support. You can write code in VS Code and run it inside Linux — without leaving Windows.

### Step 1 — Install the WSL Extension

`Extensions` tab → Search **"WSL"** → Install **"WSL" by Microsoft**

### Step 2 — Connect VS Code to WSL

**Option A — From the Ubuntu terminal (recommended):**

Navigate to your project folder and type:

```bash
code .
```

The `.` means "open current folder." VS Code will launch automatically, connected to WSL.

**Option B — From inside VS Code:**

`Ctrl+Shift+P` → type `WSL` → select **"Connect to WSL"**

### How to Confirm You Are Connected

Look at the **bottom-left corner** of VS Code.

You should see a green badge that says: **`WSL: Ubuntu`**

When you see this — you are writing code in VS Code on Windows, but your code runs inside the Linux environment. Best of both worlds.

---

## Running Your First Python File

### On Windows

1. Open VS Code
2. `File → New File` → Save as `hello.py`
3. Write this code:

```python
print("Python is ready on Windows!")
name = input("Enter your name: ")
print("Hello,", name)
```

4. Open the terminal in VS Code: `Ctrl + `` ` (backtick key, near the top-left of your keyboard)
5. Run:

```bash
python hello.py
```

---

### On WSL Ubuntu

1. Open Ubuntu terminal and create a project folder:

```bash
mkdir python_projects
cd python_projects
code .
```

2. VS Code opens connected to WSL. Create a new file `hello.py` with the same code above.
3. Run in the VS Code terminal:

```bash
python3 hello.py
```

---

## Recommended Project Folder Structure

Start organizing your projects correctly from day one. Open the **parent folder** in VS Code — not individual files. This gives you the full project tree in the sidebar.

```
PythonLearning/
│
├── basics/
│   ├── variables.py
│   ├── datatypes.py
│   └── operators.py
│
├── projects/
│   ├── calculator.py
│   └── number_guessing.py
│
└── practice/
    └── day1.py
```

---

## Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `'python' is not recognized` | PATH not set during Windows installation | Reinstall Python, check the **"Add Python to PATH"** box |
| `python3: command not found` on WSL | Python not installed in WSL | Run `sudo apt install python3` |
| File not running | Missing `.py` extension | Save the file with `.py` extension |
| Wrong Python version shown | Multiple Python versions installed | Check with `python --version` or `python3 --version` |
| `pip` not found on WSL | pip not installed | Run `sudo apt install python3-pip` |
| VS Code not connected to WSL | WSL extension missing or not connected | Install WSL extension, then use `code .` from Ubuntu terminal |

---

## Quick Reference Summary

### Windows Setup

```bash
# 1. Download from python.org — check "Add Python to PATH" during install
# 2. Verify
python --version
pip --version
```

### WSL Setup

```powershell
# In PowerShell as Administrator
wsl --install
# Restart your machine
```

```bash
# Inside Ubuntu terminal
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv -y
python3 --version
pip3 --version
```

### VS Code Setup

```
1. Download from code.visualstudio.com
2. Install extensions: Python + Pylance (both by Microsoft)
3. Install WSL extension (if using WSL)
4. Connect to WSL: type  code .  from Ubuntu terminal
5. Confirm: green "WSL: Ubuntu" badge in bottom-left corner
```

### Key Rule

> **Every Python file must end in `.py` — no exceptions.**

---

*Happy Coding! 🚀*