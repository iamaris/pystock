import random



class StockCharts():
    x_line = []
    width = 100
    height = 100


    def startgen(self):
        for y in range(0,self.height):    
            zeile = []
            for x in range(0,self.width):
                zeile.append(random.randint(0,100))
            self.x_line.append(zeile)


    def analyse(self, x, y):
        starty = max([0,y-1])
        endy = min([y+1,self.height-1])
        startx = max([0,x-1])
        endx = min([x+1,self.width-1])

        num = 0

        for sy in range(starty, endy+1):
            for sx in range(startx, endx):
                pass # her you can write your if-clauses


    def showgen(self):
        for y in range(0, self.height):
            print self.x_line[y]
        print



stock = StockCharts()
stock.startgen()
stock.showgen()
