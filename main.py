from tkinter import *
from tkinter import colorchooser
canvas_width = 500
canvas_height = 500
r = 10
class main():
        def __init__(self):
                self.node_edges = {}
                self.nodes_cord = {}
                self.total_nodes=0
                self.color = "#ffffff"

        def addEdge(self):
                edge = t1.get("1.0",'end-1c').split(" ")
                for i in range(len(edge)):
                        if(i%2 !=0):
                                node1 =(int)(edge[i])
                                node2 =(int)(edge[i-1])
                                line_id = canvas.create_line(self.nodes_cord[node1]["x"], self.nodes_cord[node1]["y"], self.nodes_cord[node2]["x"], self.nodes_cord[node2]["y"])
                                self.node_edges[node1][2].append(line_id)
                                self.node_edges[node2][2].append(line_id)
                
        def create_node(self, x, y):
                node_id = canvas.create_oval(x-r, y-r, x+r, y+r, fill=self.color)
                self.total_nodes = self.total_nodes+1
                txt_id = canvas.create_text(x,y,text=str(self.total_nodes))
                self.nodes_cord[self.total_nodes] = {"x": x, "y": y}
                self.node_edges[self.total_nodes] = [node_id, txt_id, []]

        def delete_node(self, x, y):
                for key, node in self.nodes_cord.items():
                        if (node["x"]+r>x and node["x"]-r<x and node["y"]+r>y and node["y"]-r<y):
                                canvas.delete(self.node_edges[key][0])
                                canvas.delete(self.node_edges[key][1])
                                for edge in self.node_edges[key][2]:
                                        canvas.delete(edge)

        def colorEdgeNode(self, x, y):
                item = canvas.find_closest(x, y)[0]
                canvas.itemconfig(item, fill=self.color)

        def mouse(self, event):
                if(button_value.get()=="create"):
                        self.create_node(event.x, event.y)
                elif (button_value.get()=="delete"):
                        self.delete_node(event.x, event.y)
                else:
                      self.colorEdgeNode(event.x, event.y)

        def clearGraph(self):
                self.__init__()

        def loadGraph(self):
                pass

        def saveGraph(self):
                pass
        def choosecolor(self):
                self.color = colorchooser.askcolor(title="Select Color")[1]

if __name__ == '__main__':
        main_obj = main()
        master = Tk()
        master.minsize(500, 500)
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.title( "Graph Algorithms" )
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=main_obj.clearGraph)
        filemenu.add_command(label="Open", command=main_obj.loadGraph)
        filemenu.add_command(label="Save", command=main_obj.saveGraph)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index")
        helpmenu.add_command(label="About...")
        menubar.add_cascade(label="Help", menu=helpmenu)
        master.config(menu=menubar)
        
        canvas = Canvas(master)
        canvas.grid(row = 0, column = 0, sticky="nsew")
        canvas.bind("<Button-1>", main_obj.mouse)
        side_frame = Frame(master, width=20)
        side_frame.grid(row = 0, column = 1, sticky="ns")
        button_value = StringVar(side_frame, "create")  
        values = {"Create Node" : "create", 
                  "Delete Node" : "delete", 
                  "Color Node" : "color"}
        l=0
        for (text, value) in values.items(): 
            Radiobutton(side_frame, text = text, variable = button_value, value = value).grid(row = l, column = 0, sticky="ns")
            l+=1
        c1 = Button(side_frame, text='Choose Color', command=main_obj.choosecolor)
        c1.grid(row = 3, column = 0, sticky="nsew")
        t1 = Text(side_frame, width=20)
        b1 = Button(side_frame, text='Add', command=main_obj.addEdge)
        t1.grid(row = 4, column = 0, sticky="nsew")
        b1.grid(row = 5, column = 0, sticky="nsew")
        mainloop()
