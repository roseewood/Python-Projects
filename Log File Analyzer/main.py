
file = open("server.log", "r")
logs = file.readlines()
file.close()

total = 0
info = 0
error = 0
warning = 0
errors = []

for line in logs:
    total += 1

    if line.startswith("INFO"):
        info += 1

    elif line.startswith("ERROR"):
        error += 1
        errors.append(line.strip())

    elif line.startswith("WARNING"):
        warning += 1

print("----- Log Report -----")
print("Total Lines :", total)
print("INFO Count :", info)
print("ERROR Count :", error)
print("WARNING Count :", warning)

print("\nError Messages:")
for msg in errors:
    print(msg)


summary = open("summary.txt", "w")

summary.write("----- Log Report -----\n")
summary.write("Total Lines : " + str(total) + "\n")
summary.write("INFO Count : " + str(info) + "\n")
summary.write("ERROR Count : " + str(error) + "\n")
summary.write("WARNING Count : " + str(warning) + "\n\n")

summary.write("Error Messages:\n")
for msg in errors:
    summary.write(msg + "\n")

summary.close()

print("\nSummary saved in summary.txt")