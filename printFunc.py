
# *objects (Positional values)

# Zero objects (prints an empty line)
print()

# Single object
print("Hello World!")  # Output: Hello World!

# Multiple objects (separated by commas)
print("Alice", 25, ["Python", "Java"])  # Output: Alice 25 ['Python', 'Java']


# sep (Separator)

# Customizing separator with a hyphen
print("2026", "09", "28", sep="-")

# Removing spacing completely
print("Py", "th", "on", sep="")

# end (Ending character)

# Overriding newline to stay on the same line
print("Hello", end=" ")
print("World!")

# Custom ending string
print("Processing complete", end="... SUCCESS\n")
