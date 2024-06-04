def maior_palindromo(n1, n2):
  """
  Retorna o maior palindromo, resultado do produto de dois números com n dígitos.

  Args:
    n1: O primeiro número.
    n2: O segundo número.

  Returns:
    O maior palindromo encontrado.
  """

  if n1 == n2:
    return n1

  def é_palindromo(n):
    """
    Retorna True se o número n é um palíndromo.

    Args:
      n: O número a ser verificado.

    Returns:
      True se o número n é um palíndromo, False caso contrário.
    """

    return str(n) == str(n)[::-1]

  maior_palindromo = 0
  for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
      produto = i * j
      if é_palindromo(produto) and produto > maior_palindromo:
        maior_palindromo = produto

  return maior_palindromo


def main():
  """
  Resolve o problema proposto.
  """

  maior_palindromo = 0
  for i in range(1000, 10000):
    for j in range(1000, 10000):
      produto = i * j
      if é_palindromo(produto) and produto > maior_palindromo:
        maior_palindromo = produto

  print(maior_palindromo)


if __name__ == "__main__":
  main()
