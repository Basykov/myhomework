# Task 1 Files

with open("homework10txt.txt", "w") as bbs:
    bbs.write("Hello file world!\n")

with open("homework10txt.txt", "r") as bbs:
    g = bbs.read()
    print(g)

# Task 2

import json

print("\n")

while True:
        
        b = input("What do you want to do?(F)ind or (C)ange or (E)nd session\n")

        if b.upper() == "F":
             
             ff = input("Who?(enter person info or state)\n")
             with open("homework10t2.json", "r") as ggf:
                 gg = json.load(ggf)
                 if ff in gg.keys():
                      print(gg[ff])
                 else:
                    for i in gg.values():
                        for d in i:
                            hf = d[0] + " " + d[1]
                            if ff == hf:
                                print (d)
                            elif ff in str(d):
                                print(d)
                                                
        if b.upper() == "C":
             
             jj = input("(A)dd, (C)hange or (D)elete?\n")

             jja = {}

             with open("homework10t2.json", "r") as ddf:
                dd = json.load(ddf)
                for i in dd:
                     jja[i] = dd[i]

             if jj.upper() == "A":
                jjst = input("What state?\n")
                jjn = input("Name?\n")
                jjs = input("Surname?\n")
                jjp = input("Phone?\n")
                if jjst in jja:
                    jjj = [jjn,jjs,jjp]
                    jb = jja[jjst]
                    jb.append(jjj)
                    jja[jjst] = jb 
                if jjst not in jja:
                    jjjj = [[jjn,jjs,jjp]]
                    jja[jjst] = jjjj
                with open("homework10t2.json", "w") as ttf:
                        json.dump(jja,ttf, indent=4)

             if jj.upper() == "D":
                jjd = input("Who do you wish to delete? Enter Name and surname(Example: Rosa Park)\n")
                for i in jja.values():
                    for b in i:
                        hh = b[0]+ " "+ b[1]
                        if jjd == hh:
                             i.remove(b)
                             print("Phone deleted.")

                with open("homework10t2.json", "w") as ttf:
                    json.dump(jja,ttf, indent=4)
                       
             if jj.upper() == "C":
                  found = False
                  jjv = input("Who do you wish to change? Enter Name and surname(Example: Rosa Park) remember that old info will be deleted\n")
                  for i in jja.values():
                    for b in i:
                        hh = b[0]+ " "+ b[1]
                        if jjv == hh:
                             i.remove(b)
                             print("Old info deleted. Now enter new one")
                             jjst = input("What state?\n")
                             jjn = input("Name?\n")
                             jjs = input("Surname?\n")
                             jjp = input("Phone?\n")
                             if jjst in jja:
                                jjj = [jjn,jjs,jjp]
                                jb = jja[jjst]
                                jb.append(jjj)
                                jja[jjst] = jb 
                             if jjst not in jja:
                                jjjj = [[jjn,jjs,jjp]]
                                jja[jjst] = jjjj
                             found = True
                             with open("homework10t2.json", "w") as ttf:
                                 json.dump(jja,ttf, indent=4)
                             break
                        if found == True:
                            break
                             
        elif b.upper() == "E":
            break 