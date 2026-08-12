Subject=["Python ", "Dbms", "networking", "java", "c++"]

print("Subject List:", Subject)

print("first Subject:", Subject[0])
print("third Subject:", Subject[2])

Subject[1] = "C"
print("\n---- After Modification ----")
print(" After Modification :", Subject)

Subject.append("python")
print("\n---- After Adding ----")
print(" After Adding:", Subject)

Subject.remove("networking")
print("\n---- After Removing ----")
print(" After Removing:", Subject)

Subject.insert(2, "html")
print("\n---- After Inserting ----")
print(" After Inserting:", Subject)

Subject.sort()
print("\n---- After Sorting ----")      
print(" After Sorting:", Subject)