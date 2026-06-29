# Section 3: The pass Keyword
#
# Sometimes you want to write the outer structure of your program
# first, and fill in the actual logic later.
# An empty if/else block is a SyntaxError in Python - "pass" fixes that.

exam_scheduled = True

# WRONG - this would raise: IndentationError: expected an indented block
# if exam_scheduled:
# else:
#     print("Centre is closed.")

# RIGHT - use pass as a placeholder
if exam_scheduled:
    pass  # will fill in the real logic later
else:
    print("Centre is closed.")

print("Program continued without errors.")

# pass tells Python: "something needs to go here, just not right now."
# It's a professional habit - sketch the structure first, then fill
# in the details, without breaking the program in between.
