def main():
	print(runge_kutta(1000,1/52,1,0,y_prima))

def runge_kutta(y0,h,xn,x0,funcion):
	uk = y0

	while x0<xn:

		uk = uk + (h/2)*(funcion(uk,x0)+funcion(uk+h*funcion(uk,x0),x0+h))
		
		x0 += h

	return uk

def y_prima(y,x):
	return 0.7*y

main()