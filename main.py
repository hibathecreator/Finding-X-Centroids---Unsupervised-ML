import random, math, csv

coordinates = []

centroids = []

cluster_map = []

def calc_distance(coord1, coord2):
      return math.sqrt(math.pow(coord1[0] - coord2[0], 2) + math.pow(coord1[1] - coord2[1],2))


numClusters = int(input("Num clusters: "))

with open('coordinates.csv', mode='r') as file:
    csv_data = csv.reader(file, delimiter='\n')
    next(csv_data)

    for coord in csv_data:
        coord = coord[0].split(",")
        new_coord = [float(coord[0]), float(coord[1])]
        coordinates.append(new_coord)


for i in range(numClusters):
  centroids.append(random.choice(coordinates))


for coordinate in coordinates:
  distances = []
  for centroid in centroids:
    distances.append(calc_distance(coordinate, centroid))

  cluster_map.append(distances.index(min(distances)))


def calc_centroid(index):
  num_cluster_points = 0
  sum_x = 0
  sum_y = 0

  for i in range(len(cluster_map)):
      if(cluster_map[i] == index):
        num_cluster_points += 1
        sum_x += coordinates[i][0]
        sum_y += coordinates[i][1]
    
  avg_x = sum_x/num_cluster_points
  avg_y  = sum_y/num_cluster_points
  return [avg_x, avg_y]

for i in range(numClusters):
   centroids[i] = calc_centroid(i)


def calc_dist_to_centroids():
  sum = 0
  for i in range(len(cluster_map)):
     sum += calc_distance(coordinates[i], centroids[cluster_map[i]]) ** 2
  return sum

distance = calc_dist_to_centroids()

def calc_cluster_changes():
  cluster_changes = 0
  for i in range(len(cluster_map)):
    distances = []
    for centroid in centroids:
      distances.append(calc_distance(coordinates[i], centroid))
    new_centroid = distances.index(min(distances))
    if(new_centroid != cluster_map[i]):
       cluster_changes += 1
       cluster_map[i] = new_centroid
  return cluster_changes


cluster_changes = calc_cluster_changes()
print(f'Cluster changes: {cluster_changes}')

while cluster_changes > 0:
  centroids=[]
  for i in range(numClusters):
   centroids.append(calc_centroid(i))
  
  distance = calc_dist_to_centroids()
  print(f'Distance: {distance}')

  cluster_changes = calc_cluster_changes()
  print(f'cluster changes: {cluster_changes}')
  
