def perimetro_cuadrado(): 
    lado = float(input("Digite cuanto mide el lado del cuadrado: "))
    print ('el perimetro del cuadrado es:', lado*4 )
    
def perimetro_rectangulo(): 
    base = float(input("Digite cuanto mide la base del rectangulo: "))
    altura = float(input("Digite cuanto mide la altura del rectangulo: "))
    print ('el perimetro del rectangulo es:', base**2 + altura**2)   

def perimetro_circulo(): 
    radio = float(input("Digite cuanto mide el radio del circulo: "))
    pi= 3.1416
    print ('el perimetro del circulo es:', pi * radio*2)
    

