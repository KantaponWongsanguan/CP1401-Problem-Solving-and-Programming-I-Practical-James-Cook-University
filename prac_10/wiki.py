import wikipedia

keyword = str(input("Insert title or phrase >> "))
while keyword != "":
    print(wikipedia.search(keyword))
    print(wikipedia.summary(keyword))
    print(wikipedia.page(keyword))
    keyword = str(input("Insert title or phrase >> "))
print("Existing")




