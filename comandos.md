import turtle #importa a biblioteca

s= turtle.Screen() #define a tela

t= turtle.Turtle() #define a caneta

t.shape("turtle") #caneta com formato de tartaruga

t.fd() #mover pra frente, coloque numero de passos entre parenteses

t.lt() #gira pra esquerda, coloque angulo entre parenteses

t.rt() #gira pra direita

t.bk() #mover pra tras

t.goto() #mover pra qualquer lugar, coordenadas entre parenteses

t.home() #volta pra origem

t.pu() #sem escrever

t.pd() #escrevendo

t.dot() #faz um ponto

t.circle() #faz um circulo

turtle.mainloop() #mantem a tela aberta ao fim do desenho