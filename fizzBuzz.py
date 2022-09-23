# Lucia Sanchez
# Oct 28 2021
# Fizz Buzz

x=0
while x<100:
    fizz= ""
    buzz= ""
    frog= ""
    moose= ""
    cow= ""
    x=x+1
    if x%3==0:
        fizz= "fizz"
    if x%5==0:
        buzz = "buzz"
    if x%7==0:
        frog = "frog"
    if x%11==0:
        moose = "moose"
    if x%13==0:
        cow= "cow"
    if x%3==0 or x%5==0 or x%7==0 or x%11==0 or x%13==0:
        print(fizz,buzz,frog,moose,cow)
    else:
        print(x)

x=0
while x<100:
    x=x+1
    output=""
     if x%3==0:
        output = output,"fizz"
    if x%5==0:
        output = output,"buzz"
    if x%7==0:
        output = output,"frog"
    if x%11==0:
        output = output,"moose"
    if x%13==0:
        output = output,"cow"
