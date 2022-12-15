def test():
    print("im a function")

def  say_hello(name):
     print("hello there" + name)

say_hello("jim")

num1 = 1
num2 = 2 
def sum(num1, num2):
    return num1 + num2

result = sum(21,21)
print ("the result of sum(num1, num2 is" + str(result))

#List
def List():
    color = ["red", "green", "blue", "yellow"]     
    print(color)
    color.append("white")
    print(len(color))
    color.remove("white")
    print("list")

#list 2

def list2():
   print("list 2")
   num=[12,34,21,35,37,87,24,-1,1,2,3,5,-8,7,88,32,65,-84]

   for n in num:
        if n < 0:
            print(n)

        total = 0
        count = 0
        beteen = 0
        for nums in num:
            total = total + nums
        
        if nums < 50:
            count += 1
        if i >= 10 and i <= 50:
            between = between + 1
        print(total)
        print(between)
        print("there are" + str(count) + "numbers greater than 50")    

        me = {
            "name":"Manuel",
            "last":"Bailey",
            "age":"21",
            "city":"san diego",
        }  
        print(me)
        me["preferred color"]="blue"
        print(me["name"]["last"])
