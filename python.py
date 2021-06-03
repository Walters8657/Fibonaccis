import tkinter

results = [] #Holds list of all result objects

#def fib(n):
def fib():
    for result in results:
        result.destroy()

    f1, f2, i = 0, 1, 1
    n = 0

    try:
        n = int(userInput.get())
    except:
        result = tkinter.Label(
            text="What are you doing thats not an integer"
        )
        result.pack(pady="5")

        results.append(result)
    finally:
        if (n < 1):
            return
        
        #print(f1)
        result = tkinter.Label(
            text=f1
        )
        result.pack(pady="2")

        results.append(result)

        while (i < n):
            #print(f2)
            result = tkinter.Label(
                text=f2
            )
            result.pack(pady="2")
            
            results.append(result)

            next = f1 + f2
            f1 = f2
            f2 = next
            i = i + 1

#num = int(input('How many numbers do you want? '))

#fib(num)

top = tkinter.Tk()
# Code to add widgets will go here...
greeting = tkinter.Label(
    text="Lets get some Fibonaccis"
)

inputLabel = tkinter.Label (
    text="Please make this an integer I don't want to do input validation"    
)

inputLabel2 = tkinter.Label (
    text="Enter how many numbers you want"
)

userInput = tkinter.Entry()

button = tkinter.Button(
    text="Get Numbers",
    command=fib
)

greeting.pack(pady="10")
inputLabel.pack(pady="10")
inputLabel2.pack(pady="10")
userInput.pack(pady="10")
button.pack(pady="10")

#Code to add widgets will go up there...
top.mainloop()