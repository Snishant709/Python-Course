i=0
with open("marks.txt",'r') as f:
    while True:
        i=i+1
        lines=f.readline()
        if not lines:
            break
        m1=int(lines.split(",")[0])
        m2=int(lines.split(",")[1])
        m3=int(lines.split(",")[2])
        print(f"Marks of Student{i} in English is {m1+1}")
        print(f"Marks of Student{i} in Math is {m2}")
        print(f"Marks of Student{i} in Science is {m3}")
        print(lines)

f=open("marks.txt",'r') 
while True:
        line=f.readline()#will put '/n' after printing the line 
        if not line:
                print(type(line))
                break
        else:
            print(line)

with open("Lines.txt",'w') as f:
    lines=['line1\n','line2\n''line3\n','line4']
    f.writelines(lines)#it does not add the new line

'''
| Method        | Reads              | Returns         | Best For                                    |
| ------------- | ------------------ | --------------- | ------------------------------------------- |
| `readline()`  | One line at a time | String          | Processing large files line by line         |
| `readlines()` | All lines at once  | List of strings | Small/medium files where you need all lines |

writelines()
📌 File object method — writes multiple strings to a file.
Purpose: Writes a list/iterable of strings directly to a file.
Important: Does not add \n automatically — you must include it.


'''