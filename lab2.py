import math


#module m.py
def task_if1():
  """If1. An integer is given.
  If the integer is positive then increase it by 1,
  otherwise do not change it.
  Output the obtained integer """
  try:
    int_num = int(input("Integer Number: "))
  except ValueError:
    print("INTEGER expected!")
  else:
    if int_num > 0:
      int_num += 1
    print ("New value: ", int_num)

def task_geometry1():
    """Calculation of the number of points inside the area according to the variant"""
    # Ввод входных параметров
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        if a <= 0 or b <= 0:
            raise ValueError
    except ValueError:
        print("Wrong values (a, b)")
    else:
        # створюємо список координат
        x_y_list = [] 
        # Вводимо координати точок для перевірки
        try:
            n = int(input("N = "))
            for i in range(n):  # n = 3: range(3) = 0, 1, 2
                x_i = float(input("\nX{} = ".format(i + 1)))
                y_i = float(input("Y{} = ".format(i + 1)))
                x_y_list.append((x_i, y_i))
        except ValueError:
            print("Wrong values (n, x, y)")
        else:
            # лічильник
            in_count = 0
            # Безпосередня перевірка входження кожної з наявних точок
            circle_r = a / 2
            center_x = b / 2
            center_y = a / 2
            for x, y in x_y_list: # [(2,1), (1, 1), (3, -1)]
                length = math.sqrt(math.pow(x - center_x, 2) + math.pow(y - center_y, 2))
                if (0 <= x <= center_x and 0 <= y <= a and length <= circle_r) or \
                (center_x < x <= b and 0 <= y <= a and length >= circle_r):
                    in_count += 1
            print("Final count = {}".format(in_count))
          
def task_series1():
  """check the series (variant 1) for convergence"""  
  n = 1
  s = 0
  e = 1e-10
  g = 1e+10
  while True:
    try:
      num = n*(n**0.5)
      denom = (n/2)**n
      u = num / denom
    except ValueError:
      print("Something went wrong!")
    except ZeroDivisionError:
      print("Division by zero")
    else:
      s += u
      n += 1
      print(u)
      if abs(u) < e:
        print("Ряд збігається до ", s)
        break
      elif abs(u) > g:
        print("Ряд розбігається")
        break

if __name__ == "__main__":
  task_series1()