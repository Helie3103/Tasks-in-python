dimension=int(input("What kind of list do you want? \nEnter \t1:1D list\n\t2:2D list\n\t3:3D List: "))
if(dimension=="1"):
  element=input("How many elements do you want to enter?")
  element=int(element)
  for element in range(element):
    oneD=int(input(f"Enter element {element}: "))
  print(oneD)

if(dimension=="2"):
  rows = int(input("Enter number of rows: "))
  cols = int(input("Enter number of columns: "))
  matrix = []
  for i in range(rows):
    row = []
    for j in range(cols):
      value = input(f"Enter value for [{i}][{j}]: ")
      row.append(value)
    matrix.append(row)
  print(matrix)

elif dimension == 3:
    x = int(input("Enter number of rows: "))
    y = int(input("Enter number of columns: "))
    z = int(input("Enter depth: "))
    cube = []

    for i in range(x):
        layer = []
        for j in range(y):
            row = []
            for k in range(z):
                value = int(input(f"Enter value for [{i}][{j}][{k}]: "))
                row.append(value)
            layer.append(row)
        cube.append(layer)

    print("3D List:", cube)