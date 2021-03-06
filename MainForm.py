from tkinter import *
from tkinter import ttk
import buttonEvents as be
from functools import partial
from pandastable import Table
from tkcalendar import Calendar, DateEntry

window = Tk()
window.geometry('600x400')
window.title("Python Stock Market")

lbl_searchText = Label(window, text="Enter Stock To Display: ", width=20, anchor="w")

tkvar = StringVar()
cb_stockList = ttk.Combobox(window, width=15, values=be.updateStockList(), textvariable=tkvar)

click_searchStock = partial(be.loadStockClicked, cb_stockList)
btn_searchStock = Button(window, text="Display Data", width=10, command=click_searchStock)

btn_viewReport = Button(window, text="View Report", width=10, command=be.viewReportClicked)

click_buildReport = partial(be.buildReportM)
btn_buildReport = Button(window, text="Build Report", width=10, command=click_buildReport)

click_graph = partial(be.plotStock, cb_stockList)
btn_graph = Button(window, text="Graph Data", width=15, command=click_graph)

click_predictGraph = partial(be.graphPrediction, cb_stockList)
btn_predictGraph = Button(window, text="Predict Data", width=15, command=click_predictGraph)

btn_import500 = Button(window, text="Import Form", width = 15, command=be.importStockClicked)


lbl_searchText.grid(column=0, row=0)
btn_searchStock.grid(column=2, row=0)
cb_stockList.grid(column=1, row=0)
btn_import500.grid(column=3, row=2)
btn_graph.grid(column=3,row=0)
btn_predictGraph.grid(column=4,row=0)
btn_buildReport.grid(column=4,row=2)
btn_viewReport.grid(column=2,row=2)
window.mainloop()