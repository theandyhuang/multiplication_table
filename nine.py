for i in range(9):
    for j in range(9):
        print(f"{j+1:2d} *{i+1:2d} = {(i+1)*(j+1):2d}", end = " ")  #f string的:後面2d是指給兩個位元，會比較漂亮
    print("\n")