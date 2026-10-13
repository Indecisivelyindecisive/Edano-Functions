first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
choice = int(input("Choices: 1 - addition, 2 - subtraction, 3 - multiplication, 4 - division\n"))

if choice == 4 and second_number == 0:
  print("Invalid choice.")
else:
  def add_number(sum):
     return sum

  def subtract_number(difference):
     return difference
  
  def multiply_number(product):
    return product
  
  def divide_number(quotient):
     return quotient

  if choice == 1:
    sum_final = add_number(first_number + second_number)
    print(f"Your sum is... {sum_final}!")
  elif choice == 2:
    difference_final = subtract_number(first_number - second_number)
    print(f"Your difference is... {difference_final}!")
  elif choice == 3:
    product_final = multiply_number(first_number * second_number)
    print(f"Your product is... {product_final}!")
  elif choice == 4:
    quotient_final = divide_number(first_number / second_number)
    print(f"Your quotient is... {quotient_final}!")
  else:
    print("Invalid choice.")
