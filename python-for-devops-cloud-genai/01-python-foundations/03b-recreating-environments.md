# 🔁 Recreating Python Virtual Environments — venv & uv

When you clone a project from GitHub, or receive code from a teammate, the `.venv`
folder is never included (it is in `.gitignore`). This guide shows you exactly how
to recreate the full environment from scratch — using both the traditional `venv`
approach and the modern `uv` approach.

---

## 📋 Table of Contents

- [What Files Are Shared With You](#what-files-are-shared-with-you)
- [Method 1 — Recreate Using venv + requirements.txt](#method-1--recreate-using-venv--requirementstxt)
- [Method 2 — Recreate Using uv sync](#method-2--recreate-using-uv-sync)
  - [What Files Does uv Need?](#what-files-does-uv-need)
  - [pyproject.toml — What It Is](#pyprojecttoml--what-it-is)
  - [uv.lock — What It Is](#uvlock--what-it-is)
  - [Which Combination of Files Will You Have?](#which-combination-of-files-will-you-have)
  - [uv sync Commands by Scenario](#uv-sync-commands-by-scenario)
- [Side-by-Side Comparison](#side-by-side-comparison)
- [Quick Reference — All Commands](#quick-reference--all-commands)

---

## What Files Are Shared With You

When a project is shared via GitHub or as a zip, you will typically receive:

```
my-project/
│
├── main.py                  ← source code
├── requirements.txt         ← if project uses venv/pip workflow
├── pyproject.toml           ← if project uses uv workflow
├── uv.lock                  ← if project uses uv workflow
├── .gitignore
└── README.md

❌ .venv/                    ← NEVER included — you recreate this locally
```

The `.venv` folder is always absent. Your job is to recreate it using whichever
file the project provides.

---

## Method 1 — Recreate Using venv + requirements.txt

Use this method when the project contains a `requirements.txt` file.

### Step 1 — Navigate into the project folder

```bash
cd my-project
```

### Step 2 — Create a fresh virtual environment

**Mac / Linux:**
```bash
python3 -m venv .venv
```

**Windows:**
```bash
python -m venv .venv
```

### Step 3 — Activate the virtual environment

**Mac / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

Confirm activation — your terminal prompt should show:
```
(.venv) my-project $
```

### Step 4 — Install all dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

`-r` = read from this file and install everything listed in it, with exact pinned versions.

### Step 5 — Verify installation

```bash
pip list
```

You should see all libraries from `requirements.txt` listed as installed.

### Full flow in one block

```bash
cd my-project
python3 -m venv .venv                  # Mac/Linux
source .venv/bin/activate              # Mac/Linux

python -m venv .venv                   # Windows
.venv\Scripts\activate                 # Windows

pip install -r requirements.txt
pip list
```

> ⚠️ Every time you open a new terminal session, you must activate the virtual
> environment again before running your code. It does not persist across sessions.

---

## Method 2 — Recreate Using uv sync

Use this method when the project was created using `uv`.

`uv sync` is the single command that recreates the entire environment. It reads the
project's dependency files, creates the virtual environment automatically, and
installs everything — in one step.

```bash
cd my-project
uv sync
```

That is the complete command. But what makes it work is the files present in the
project. Understanding those files is important.

---

### What Files Does uv Need?

`uv` uses two files to recreate an environment:

| File | Role | Required? |
|------|------|-----------|
| `pyproject.toml` | Declares what the project needs | ✅ Always required |
| `uv.lock` | Records the exact resolved versions | ✅ Required for exact reproduction |

Both files are committed to Git and travel with the project.
You never create them manually — `uv` generates and maintains them for you.

---

### pyproject.toml — What It Is

`pyproject.toml` is the **project configuration file**. It is the modern Python
standard (defined in PEP 518 and PEP 621) for declaring project metadata and
dependencies.

When you run `uv init` and `uv add`, this file is created and updated automatically.

A typical `pyproject.toml` looks like this:

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31.0",
    "flask>=3.0.3",
    "numpy>=1.26.4",
]
```

**What it declares:**
- Project name and version
- Minimum Python version required
- List of dependencies with acceptable version ranges

Think of `pyproject.toml` as the **menu** — it says what the project wants,
with some flexibility on exact versions.

---

### uv.lock — What It Is

`uv.lock` is the **lock file**. It records the exact, fully resolved version of
every single package — including all indirect dependencies (dependencies of your
dependencies).

A snippet of what `uv.lock` contains:

```
version = 1
requires-python = ">=3.11"

[[package]]
name = "requests"
version = "2.31.0"
source = { registry = "https://pypi.org/simple" }

[[package]]
name = "certifi"
version = "2024.2.2"
source = { registry = "https://pypi.org/simple" }
```

**What it guarantees:**
- Exact same versions installed on every machine — Mac, Windows, Linux
- No version drift — even if a newer version of a library is released tomorrow,
  `uv sync` will still install exactly what the lock file specifies
- Reproducible builds across your entire team and in CI/CD pipelines

Think of `uv.lock` as the **actual order receipt** — exactly what was delivered,
down to every item, precisely recorded.

> 💡 `uv.lock` is far more precise than `requirements.txt` because it also captures
> the full dependency tree — not just your direct dependencies.

---

### Which Combination of Files Will You Have?

Depending on how the project was set up and shared, you may encounter one of these
three scenarios:

---

#### Scenario A — Both pyproject.toml AND uv.lock are present ✅ (ideal)

```
my-project/
├── pyproject.toml
├── uv.lock
└── main.py
```

This is the standard, correct state for a `uv` project.

```bash
uv sync
```

`uv sync` reads `uv.lock` and installs the **exact pinned versions** — guaranteed
identical environment to whoever originally set up the project. This is the most
reliable scenario.

---

#### Scenario B — Only pyproject.toml, no uv.lock

```
my-project/
├── pyproject.toml
└── main.py
```

This happens when someone initialized the project but never ran `uv lock`, or
forgot to commit the lock file.

```bash
uv sync
```

`uv` will read `pyproject.toml`, **resolve the best compatible versions**,
install them, and **generate a new `uv.lock` file** automatically.

> ⚠️ Without the lock file, `uv` installs the latest compatible versions at the
> time you run `sync`. This may differ slightly from what the original developer had.
> Commit the generated `uv.lock` immediately so future runs are pinned.

---

#### Scenario C — Project has requirements.txt but you want to use uv

```
my-project/
├── requirements.txt
└── main.py
```

The project was originally set up with `venv/pip`, but you prefer `uv`.

```bash
# Import dependencies from requirements.txt into uv
uv add $(cat requirements.txt)
```

Or more reliably, initialize uv in the existing project and import:

```bash
uv init --no-workspace          # sets up pyproject.toml in existing project
uv add -r requirements.txt      # imports all deps from requirements.txt into uv
uv sync                         # installs everything and generates uv.lock
```

After this, the project is fully migrated to `uv` with both `pyproject.toml`
and `uv.lock` generated.

---

### uv sync Commands by Scenario

```bash
# Standard sync — install all dependencies (default)
uv sync

# Sync and also install optional dev dependencies
uv sync --all-extras

# Sync without dev dependencies (for production deployment)
uv sync --no-dev

# Force re-resolve all versions even if lock file exists
uv sync --upgrade

# Upgrade a specific package only
uv sync --upgrade-package requests

# Check what would be installed without actually installing
uv sync --dry-run
```

---

## Side-by-Side Comparison

| | venv + requirements.txt | uv sync |
|--|------------------------|---------|
| **Command to recreate** | `pip install -r requirements.txt` | `uv sync` |
| **Files needed** | `requirements.txt` | `pyproject.toml` + `uv.lock` |
| **Creates .venv automatically** | ❌ You create it manually first | ✅ uv creates it for you |
| **Activation needed** | ✅ Must activate manually | ✅ Activate for running scripts |
| **Captures indirect deps** | ❌ Only direct deps | ✅ Full dependency tree |
| **Cross-platform reproducibility** | Partial | ✅ Exact same on all platforms |
| **Speed** | Slower | 10x–100x faster |
| **Works without internet** | ❌ | ✅ If uv cache is warm |

---

## Quick Reference — All Commands

### venv + requirements.txt

```bash
# Step 1 — Create virtual environment
python3 -m venv .venv          # Mac/Linux
python -m venv .venv           # Windows

# Step 2 — Activate
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows

# Step 3 — Install from requirements.txt
pip install -r requirements.txt

# Step 4 — Verify
pip list

# When done
deactivate
```

### uv sync

```bash
# Scenario A: Both pyproject.toml and uv.lock present (ideal)
uv sync

# Scenario B: Only pyproject.toml, no lock file
uv sync                        # auto-generates uv.lock

# Scenario C: Migrating from requirements.txt to uv
uv init --no-workspace
uv add -r requirements.txt
uv sync

# Additional sync options
uv sync --all-extras           # include optional dependencies
uv sync --no-dev               # exclude dev dependencies
uv sync --upgrade              # re-resolve all to latest compatible
uv sync --upgrade-package flask  # upgrade one specific package
uv sync --dry-run              # preview without installing

# After sync — activate the environment uv created
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

### Files to always commit to Git

```
✅ requirements.txt            (venv workflow)
✅ pyproject.toml              (uv workflow)
✅ uv.lock                     (uv workflow)
✅ .gitignore

❌ .venv/                      (never commit)
❌ __pycache__/                (never commit)
```

---
