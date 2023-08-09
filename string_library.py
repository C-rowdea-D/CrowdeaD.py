
write = "Hi ash"
gholam = write.replace("a", "da")
print(gholam)


greet = "  hello Bob  "
gy = greet.rstrip()      #lstrip for left strip for be in the middle
print(gy)
rez = greet.startswith("  hello")
print(rez)
zer = greet.startswith("s")
print(zer)



has = "ashkan today is the day that you should find your self"
to = has.find("should")
print(to)
tu = has.find("is")
print(tu)
khey = has [tu : to]   #but not included should
print(khey)
