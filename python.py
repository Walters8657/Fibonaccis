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
            scrollableFrame,
            text="What are you doing thats not an integer"
        )
        result.pack(
            pady="2",
            anchor="w"
        )

        results.append(result)
    finally:
        if (n < 1):
            return
        
        #print(f1)
        result = tkinter.Label(
            scrollableFrame,
            text=f1
        )
        result.pack(
            pady="2",
            anchor="w"
        )

        results.append(result)

        while (i < n):
            #print(f2)
            result = tkinter.Label(
                scrollableFrame,
                text=f2
            )
            result.pack(
                pady="2",
                anchor="w"
            )
            
            results.append(result)

            next = f1 + f2
            f1 = f2
            f2 = next
            i = i + 1

#num = int(input('How many numbers do you want? '))

#fib(num)

top = tkinter.Tk()
top.geometry("500x500")
top.title("Fibonacci")
top.resizable(False, False)

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

#Sets up scrollable result section
resultFrame = tkinter.Frame(top) #main box to hold everything dealing with results

canvas = tkinter.Canvas(resultFrame) #Contains scrollable content

yscroll = tkinter.Scrollbar(resultFrame, orient="vertical", command=canvas.yview) #The actual scrollbar

scrollableFrame = tkinter.Frame(canvas) #What is actually scrolling

scrollableFrame.bind(
    '<Configure>',
    lambda e: canvas.configure(
        scrollregion = canvas.bbox('all')
    )
) #Sets up scroll region to be the entire box of content

canvas.create_window((0, 0), window=scrollableFrame, anchor="nw") #Canvas window created within the scrollable frame
canvas.configure(yscrollcommand=yscroll.set) #Tells canvas to detect vertical scrolling

resultFrame.pack(fill="both", padx="10", pady="10") #Frame fills horizontal and vertical space with 10px of padding
canvas.pack(side="left", fill="both", expand=True) #Canvas fills space available starting from left
yscroll.pack(side="right", fill="y") #Scrollbar sits to the right villing vertical space

#Code to add widgets will go up there...
top.mainloop()