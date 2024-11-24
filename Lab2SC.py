import sympy as sp
def LaGrange(valoresX,valoresY):
  """
  Performs a Lagrange interpolation given a 2 arrays of multiple coordinates

  Args:
    valoresX : Array of X values
    valoresY : Array of Y values

  Returns:
    polinomio : Lagrange interpolation polynomial

  """
  x = sp.Symbol('x')
  # Variable initialization
  polinomio = ""
  suma = 0

  # We check if the arrays have the same length
  if len(valoresX) == len(valoresY):
      for i in range(len(valoresX)):
          producto = 1
          # Construction of the L_i(x)
          for j in range(len(valoresX)):
              if i != j:
                  producto *= (x - valoresX[j]) / (valoresX[i] - valoresX[j])
          # Add y_i * L_i(x) to the polynomial
          suma += valoresY[i] * producto
      # Simplification of the polynomial
      polinomio = sp.simplify(suma)
      print("\nLagrange interpolation polynomial:")
      print(polinomio)

      # Verify that the polynomial evaluates correctly at the given points
      print("\nVerificación:")
      for i in range(len(valoresX)):
          valor_evaluado = polinomio.subs(x, valoresX[i])
          print(f"P({valoresX[i]}) = {valor_evaluado}, Expected value = {valoresY[i]}")
          assert round(valor_evaluado, 5) == valoresY[i], "The polynomial does not evaluate correctly  ."
  else:
      print("Arrays dont have the same lenght.")


def __main__():
  x = input("Input all the x values separated by comas: ")
  y = input("Input all the y values separated by comas: ")
  valores_x = [float(x.strip()) for x in x.split(',')]
  valores_y = [float(y.strip()) for y in y.split(',')]

  lagrange = LaGrange(valores_x,valores_y)

if __name__ == '__main__':
    __main__()
