def main():
	print( euler(1000,1/999,1,y_prima))
#funcion y_prima
#y0 valor inicial
def euler(y0,h,x,funcion):
	uk = y0
	i = 0
	while i<x:
		uk = uk + h*funcion(uk,i)
		i+=h
	return uk

	
def y_prima(y,t):
	return 0.7*y
main()