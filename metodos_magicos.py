class Coordenadas:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+ ')'
    
    def __add__(self,otro):
        return Coordenadas(self.x+otro.x,self.y+otro.y)
    def __eq__(self,otro):
        return self.x==otro.x and self.y==otro.y
    
p1= Coordenadas(4,5)
p2= Coordenadas(7,0)

print(p1+p2)
