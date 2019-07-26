tw = 20
th = 20
fw = int(input("enter floor width: "))
fh = int(input("enter floor height: "))
tile_cost = 50
area = fw*fh
tile_need = area / (tw*th)
print("cost of tile to cover area: ", tile_need*tile_cost)
