lenguajes = ["python", "kotlin", "java", "go", "ruby"]

for l in lenguajes:
    if l == "kotlin":
        print(l.upper())
    elif l == "java":
        lenguajes.remove("java")
    else:
        print(l)









