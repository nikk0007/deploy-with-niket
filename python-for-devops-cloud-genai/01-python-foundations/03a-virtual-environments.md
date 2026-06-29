# 🐍 Python Virtual Environments — venv, requirements.txt, and uv

> *"Shared resources cause conflicts. In real life, in offices, and in Python."*

This guide explains why virtual environments exist, how to use them correctly, how to share Python projects professionally using `requirements.txt`, and how the modern tool `uv` is changing the way developers work.

📺 **Video Tutorial:** [Python Virtual Environments Explained — venv, requirements.txt and uv | Complete Guide in Hindi](#)
📂 **Part of:** Python Foundation Series — Video #5

---

## 📋 Table of Contents

- [The Problem — Why Global Installations Break Things](#the-problem--why-global-installations-break-things)
- [The Solution — Virtual Environments](#the-solution--virtual-environments)
- [Creating a Virtual Environment — venv](#creating-a-virtual-environment--venv)
- [Activating and Deactivating](#activating-and-deactivating)
- [Installing Libraries Inside a Virtual Environment](#installing-libraries-inside-a-virtual-environment)
- [The requirements.txt File](#the-requirementstxt-file)
- [What Goes in .gitignore](#what-goes-in-gitignore)
- [The Modern Way — uv](#the-modern-way--uv)
- [venv vs uv — When to Use What](#venv-vs-uv--when-to-use-what)
- [Quick Reference Summary](#quick-reference-summary)

---

## The Problem — Why Global Installations Break Things

When you install Python on your computer, it sits **globally** — one copy used by everything on that machine. Third-party libraries you install via `pip` also go into that same global space.

This works fine when you have one project. The problem starts when you have multiple.

### The conflict scenario

| Situation | Result |
|-----------|--------|
| Project A uses Library X **version 1.0** | Working fine |
| Project B needs Library X **version 2.0** | You upgrade globally |
| After upgrade — Project A | **Breaks** — version 2.0 has breaking changes |
| You downgrade back to 1.0 | Project B **stops working** |
| You're stuck | Both projects cannot coexist globally |

This is not a rare edge case. This is the everyday reality of any developer working on more than one Python project.

**Root cause:** One shared space. Multiple projects with different, conflicting needs. No isolation.

---

## The Solution — Virtual Environments

A **virtual environment** is an isolated, self-contained Python setup created specifically for one project.

- It has its own Python copy and its own separate library folder
- What you install inside one virtual environment stays inside it
- Completely invisible to other projects and to the global system

### The mental model

Think of it like this:

```
Global Python  =  The main water supply line of a building
Virtual Env    =  Each flat has its own independent water tank

One flat's tank gets contaminated → other flats are completely unaffected
Each flat manages its own supply independently
```

### What this gives you

```
Project A  →  Library X version 1.0  ✅  (untouched forever)
Project B  →  Library X version 2.0  ✅  (no conflict)
Project C  →  Library X version 3.0  ✅  (no problem)

All three on the same machine. Perfectly coexisting.
```

> 🏭 **Industry Rule:** Always work inside a virtual environment. No exceptions. Every professional Python project — from a small script to a large production system — uses one.

---

## Creating a Virtual Environment — venv

`venv` is Python's **built-in tool** — no installation needed, it comes with Python itself. This is the standard, traditional approach used in most codebases, tutorials, and open-source projects.

### Step 1 — Open your terminal inside your project folder

In VS Code: right-click your project folder → **Open in Integrated Terminal**

### Step 2 — Create the virtual environment

**On Mac / Linux:**
```bash
python3 -m venv .venv
```

**On Windows:**
```bash
python -m venv .venv
```

### What is `.venv`?

- `.venv` is the folder name where your virtual environment will be stored
- The dot prefix makes it a **hidden folder** — keeps your project directory clean
- You can name it anything (`env`, `venv`, `myenv`) — `.venv` is the modern convention

### What happens after running this command?

Python creates a new folder `.venv` inside your project directory containing a complete isolated Python setup. That is your virtual environment — **created, but not yet active.**

---

## Activating and Deactivating

Creating a virtual environment is not enough. You must **activate** it before using it.

Activating means: *"From now on, use this project's private Python — not the global one."*

### Activate

**On Mac / Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

### How to confirm it is active

Your terminal prompt changes — you will see the environment name in parentheses:

```
(.venv) your-folder-name $
```

That `(.venv)` prefix is your confirmation. You are now inside the virtual environment. Any library you install goes into this isolated space only.

### Deactivate when done

```bash
deactivate
```

Your terminal prompt returns to normal — you are back on the global system.

> ⚠️ **Important habit:** Every time you open a project in a new terminal session, activate the virtual environment first. It does **not** stay active automatically across sessions.

---

## Installing Libraries Inside a Virtual Environment

Once your virtual environment is active, install libraries normally using `pip`:

```bash
pip install requests
pip install flask
pip install numpy
```

These install **only inside `.venv`** — your global Python and all other projects remain completely unaffected.

### Version pinning — important for production

```bash
pip install requests==2.31.0
pip install flask==3.0.3
pip install numpy==1.26.4
```

**Why pin versions?**

When you write `pip install requests`, it always installs the **latest** version. That version can change tomorrow. If your code depends on specific behavior of `requests 2.31.0`, and a teammate installs `3.0.0`, your code may break on their machine.

Pinning with `==` ensures your project behaves **identically on every machine, every time.**

**Where to find version numbers?**

👉 [pypi.org](https://pypi.org) — the official Python Package Index. Search any library, find all available versions, copy the exact version number you need.

---

## The requirements.txt File

You cannot share your `.venv` folder with others — it is large (hundreds of MB), machine-specific, and completely unnecessary to share.

Instead, you record all your project's dependencies in a single text file called **`requirements.txt`**.

### What it looks like

```
requests==2.31.0
flask==3.0.3
numpy==1.26.4
pandas==2.2.0
```

### Generate it automatically from your active environment

```bash
pip freeze > requirements.txt
```

This captures every currently installed library and its exact version into the file automatically.

### Install all dependencies from the file

```bash
pip install -r requirements.txt
```

`-r` = read from file. One command. All dependencies. Exact versions. Done.

### The complete sharing workflow

```
Developer side:
──────────────
Create project folder
→ Create .venv
→ Activate
→ pip install libraries (with pinned versions)
→ Write code
→ pip freeze > requirements.txt
→ Share: .py files + requirements.txt  ✅
→ Do NOT share: .venv folder  ❌

Teammate side:
─────────────
Receive project files
→ Create fresh .venv
→ Activate
→ pip install -r requirements.txt
→ Exact same environment — ready to run  ✅
```

> 💡 **The golden rule:** Code travels. Environments stay local. `requirements.txt` is the bridge between them.

---

## What Goes in .gitignore

When using Git, the `.venv` folder must **never** be committed to the repository. It is large, machine-specific, and completely reproducible from `requirements.txt`.

Create a `.gitignore` file in your project root and add:

```
.venv/
__pycache__/
*.pyc
```

| Entry | What it is | Why exclude |
|-------|------------|-------------|
| `.venv/` | Virtual environment folder | Large, machine-specific, reproducible |
| `__pycache__/` | Python's compiled cache folder | Auto-generated, not needed |
| `*.pyc` | Compiled Python bytecode files | Auto-generated, not needed |

### What you DO commit

```
✅  All .py source files
✅  requirements.txt
✅  .gitignore itself
✅  Any config files your project needs
```

---

## The Modern Way — uv

`venv` works well but is slow and has limitations. The Python ecosystem now has a newer, significantly faster tool: **`uv`**.

- Built in **Rust** — blazing fast
- Maintained by **Astral** — the same team behind the popular `ruff` linter
- Rapidly becoming the industry standard for Python environment and package management

### Why uv is better

| Feature | venv + pip | uv |
|---------|------------|----|
| Speed | Baseline | 10x–100x faster |
| Python version management | Needs pyenv separately | Built-in |
| Lock file | requirements.txt | uv.lock (more precise) |
| Replaces | — | pip + venv + pyenv + pipenv + poetry |
| Manual venv activation | Required | Handled automatically |

### Install uv

**Mac / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Start a new project with uv

```bash
uv init my-project
cd my-project
uv add requests flask numpy
```

That is it. No manual `.venv` creation. No manual activation for most workflows. `uv` handles it all automatically.

A `uv.lock` file is created automatically — more precise than `requirements.txt`, ensuring exact reproducible installs across Mac, Windows, and Linux.

---

## venv vs uv — When to Use What

### Use `venv` when:

- Working on an **existing project** that already uses it
- Following a **tutorial or course** that uses venv
- **Contributing to open-source** projects using the traditional setup
- You want **zero additional installations** — venv is built into Python

### Use `uv` when:

- Starting a **brand new project**
- You want **significantly faster installs** — especially with large dependency trees
- Managing **multiple Python versions** on the same machine
- Building **production-grade modern applications**

> Both tools are worth knowing. A large amount of existing code, tutorials, and open-source projects use `venv`. But for new projects — `uv` is clearly the better choice.

---

## Quick Reference Summary

### venv Workflow

```bash
# Create virtual environment
python3 -m venv .venv          # Mac/Linux
python -m venv .venv           # Windows

# Activate
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows

# Install libraries (with pinned versions)
pip install requests==2.31.0

# Capture environment to file
pip freeze > requirements.txt

# Recreate environment from file (on any machine)
pip install -r requirements.txt

# Deactivate
deactivate
```

### uv Workflow

```bash
# Install uv (one time)
curl -LsSf https://astral.sh/uv/install.sh | sh   # Mac/Linux
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Start new project
uv init my-project
cd my-project

# Add dependencies
uv add requests flask numpy
```

### .gitignore — Always Add This

```
.venv/
__pycache__/
*.pyc
```

### The Professional Sequence — Never Skip This

```
1. Create project folder
2. Create virtual environment
3. Activate it
4. THEN start installing libraries and writing code
```
---

*Happy Coding! 🚀*