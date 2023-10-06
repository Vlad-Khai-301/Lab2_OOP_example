import lab2

num_to_func = {
  "1": lab2.task_if1,
  "2": lab2.task_geometry1,
  "3": lab2.task_series1
}

# Стандартний варіант реалізації меню через розгалуження
if __name__ == "__main__":
  choice = "-1"
  while choice != "0":
    choice = input("Please, choose the task again (0-EXIT): ")
    if choice == "1":
      lab2.task_if1()
    elif choice == "2":
      lab2.task_geometry1()
    elif choice=="3":
      lab2.task_series1()
    else:
      print("Wrong task number!")
  print("Good by!")


# Альтернативний варіант реалізації меню через використання словника
if __name__ == "__main__":
  choice = "-1"
  while choice != "0":
    choice = input("Please, choose the task again (0-EXIT): ")
    if choice in num_to_func:
      num_to_func.get(choice)()
    else:
      print("Wrong task number!")
  print("Good by!")


