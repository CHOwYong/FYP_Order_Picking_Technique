from SimulationRunner import simulate
from tkinter import *
from tkinter import ttk


root = Tk()

root.title = "Warehouse Simulation Software"
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



labelmaxRowsCols = ttk.Label(mainframe,text="Maximum value of range of possible\nrow and column size(n x n) generated:")
labelmaxRowsCols.grid(row=0,column=0,padx=10,pady=10)

labelmaxNoWorkers = ttk.Label(mainframe,text="Maximum value of range of possible\nnumber of workers generated:")
labelmaxNoWorkers.grid(row=0,column=1,padx=10,pady=10)

labelmaxNoSkus = ttk.Label(mainframe,text="Maximum value of range of possible\nnumber of SKUs in orderlist generated:")
labelmaxNoSkus.grid(row=0,column=2,padx=10,pady=10)


maxRowsCols = IntVar(value=1)
maxNoWorkers = IntVar(value=20)
maxNoSkus = IntVar(value=20)

spinmaxRowsCols = ttk.Spinbox(mainframe,from_=1,to_=9,textvariable=maxRowsCols,wrap=True)
spinmaxRowsCols.grid(row=1,column=0,padx=10,pady=10)
spinmaxRowsCols.state(['readonly'])

spinmaxNoWorkers = ttk.Spinbox(mainframe,from_=1,to_=40,textvariable=maxNoWorkers,wrap=True)
spinmaxNoWorkers.grid(row=1,column=1,padx=10,pady=10)
spinmaxNoWorkers.state(['readonly'])

spinmaxNoSkus = ttk.Spinbox(mainframe,from_=1,to_=40,textvariable=maxNoSkus,wrap=True)
spinmaxNoSkus.grid(row=1,column=2,padx=10,pady=10)
spinmaxNoSkus.state(['readonly'])




rowsColsFixed = IntVar(value=0)
noWorkersFixed = IntVar(value=0)
maxSKUsFixed = IntVar(value=0)

checkrowsColsFixed = ttk.Checkbutton(mainframe,text= "Fix Row and Column Sizes",variable = rowsColsFixed,onvalue=1,offvalue=0)
checkrowsColsFixed.grid(column = 0, row = 2,padx=10,pady=10);

checknoWorkersFixed = ttk.Checkbutton(mainframe,text= "Fix Number of Workers",variable = noWorkersFixed,onvalue=1,offvalue=0)
checknoWorkersFixed.grid(column = 1, row = 2,padx=10,pady=10);

checkmaxSKUsFixed = ttk.Checkbutton(mainframe,text= "Fix Number of Skus\ngenerated per orderlist",variable = maxSKUsFixed,onvalue=1,offvalue=0)
checkmaxSKUsFixed.grid(column = 2, row = 2,padx=10,pady=10);

noIterations = IntVar(value=25)


labelnoIterations = ttk.Label(mainframe,text="Number of Iterations\nto be run:")
labelnoIterations.grid(row=3,column=0,padx=10,pady=10)


spinnoIterations = ttk.Spinbox(mainframe,from_=25,to_=1000,textvariable=noIterations,increment=25)
spinnoIterations.grid(row=4,column=0,padx=10,pady=10)
spinnoIterations.state(['readonly'])


labelfilename = ttk.Label(mainframe,text="Enter your output file name\n(without .csv extension):")
labelfilename.grid(row=3,column=1,padx=10,pady=10)



filename = StringVar(value = "Results")
entryfilename = ttk.Entry(mainframe,textvariable=filename)
entryfilename.grid(row=4,column=1,padx=10,pady=10)


progressSimulate = ttk.Progressbar(mainframe,orient=HORIZONTAL,length=200,value=0)
progressSimulate.grid(row=5,column=1,padx=10,pady=10)

buttonrunSimulate = ttk.Button(mainframe, text = "Run Simulation", default= "active", command= lambda:simulate(maxRowsCols.get(),maxNoSkus.get(),noIterations.get(),maxNoWorkers.get(),filename.get(),progressSimulate,mainframe,rowsColsFixed.get(),maxSKUsFixed.get(),noWorkersFixed.get()))
buttonrunSimulate.grid(column= 1, row= 6,padx=10,pady=10)




root.mainloop()


