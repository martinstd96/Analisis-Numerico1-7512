"""Funciones Runge-Kutta 4"""

def un_paso_rk4(yk,tk,h,funcion):
	return yk + h*(f1(yk,tk,h,funcion)+2*f2(yk,tk,h,funcion)+2*f3(yk,tk,h,funcion)+f4(yk,tk,h,funcion))/6

def f1(yk,tk,h,funcion):

	return funcion(yk,tk)

def f2(yk,tk,h,funcion):

	return funcion(yk+(h/2)*f1(yk,tk,h,funcion),tk+h/2)

def f3(yk,tk,h,funcion):

	return funcion(yk+(h/2)*f2(yk,tk,h,funcion),tk+h/2)

def f4(yk,tk,h,funcion):
	return funcion(yk+h*f3(yk,tk,h,funcion),tk+h)