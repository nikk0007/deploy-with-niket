# demo_04_when_not_to_use_oop.py
# ============================================================
# VIDEO DEMO — Part 7
# Show: "When OOP is the WRONG choice"
# Most instructors skip this — it builds real engineering judgment
# ============================================================


# -------------------------------------------------------
# SCENARIO: Simple one-time scripts
# This is perfectly fine WITHOUT any class
# -------------------------------------------------------

import os
import shutil
from datetime import datetime


def compress_old_logs(log_folder):
    """Archives logs older than 7 days."""
    print(f"Compressing old logs in: {log_folder}")
    # Real logic would go here


def backup_folder(source, destination):
    """Copies a folder to a backup location."""
    print(f"Backing up {source} → {destination}")
    # Real logic would go here


def rename_files_by_date(folder):
    """Renames files with today's date prefix."""
    today = datetime.today().strftime("%Y-%m-%d")
    print(f"Renaming files in {folder} with prefix: {today}")
    # Real logic would go here


# Just call the functions — clean, simple, done
compress_old_logs("/var/log/app")
backup_folder("/home/user/projects", "/mnt/backups")
rename_files_by_date("/home/user/downloads")


# -------------------------------------------------------
# WRONG: Over-engineering with unnecessary classes
# Do NOT do this for simple utility scripts
# -------------------------------------------------------

# class LogCompressor:
#     def __init__(self, log_folder):
#         self.log_folder = log_folder
#
#     def compress(self):
#         print(f"Compressing logs in: {self.log_folder}")
#
#
# class FolderBackup:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination
#
#     def run(self):
#         print(f"Backing up {self.source} → {self.destination}")
#
#
# class FileRenamer:
#     def __init__(self, folder):
#         self.folder = folder
#
#     def rename_by_date(self):
#         today = datetime.today().strftime("%Y-%m-%d")
#         print(f"Renaming files in {self.folder} with prefix: {today}")
#
#
# compressor = LogCompressor("/var/log/app")
# compressor.compress()
#
# backup = FolderBackup("/home/user/projects", "/mnt/backups")
# backup.run()
#
# renamer = FileRenamer("/home/user/downloads")
# renamer.rename_by_date()


# -------------------------------------------------------
# TEACH:
# The class version is MORE code.
# It is HARDER to read.
# It adds ZERO value for a one-time utility script.
# This is called over-engineering.
# Good engineers avoid it.
# -------------------------------------------------------


# -------------------------------------------------------
# THE DECISION RULE — show this as a diagram on slides
# -------------------------------------------------------

def show_decision_rule():
    rule = """
    ┌──────────────────────────────────────────────────────────────────┐
    │                   WHEN TO USE WHAT                               │
    ├──────────────────────────────────────────────────────────────────┤
    │                                                                  │
    │  Small Script (< 50 lines, runs once, one purpose)              │
    │       → Functions are enough. Keep it simple.                   │
    │       Example: rename_files(), backup_folder()                  │
    │                                                                  │
    │  Medium Project (multi-file, reused, team uses it)              │
    │       → Mix of Functions + Classes                              │
    │       Example: A Terraform helper with EC2Manager class         │
    │                                                                  │
    │  Large Software / SDK / Framework / Shared Library              │
    │       → Classes, Objects, Composition, Modules, Packages        │
    │       Example: boto3, LangChain, your team's internal SDK       │
    │                                                                  │
    └──────────────────────────────────────────────────────────────────┘

    RULE: Match the tool to the SIZE of the problem.
          Not every problem needs a class.
          Not every project needs functions only.
          Good engineering judgment = knowing which is which.
    """
    print(rule)


show_decision_rule()
