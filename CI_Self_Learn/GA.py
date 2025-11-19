import pandas as pd

# Distance matrix
dist = [
    [0, 5300, 17800, 11800, 4800, 5800, 7700],
    [5300, 0, 17000, 7000, 6000, 5600, 5100],
    [17800,17000,0,10800,8700,14000,9000],
    [11800,7000,10800,0,5200,11000,6900],
    [4800,6000,8700,5200,0,10400,8200],
    [5800,5600,14000,11000,10400,0,9000],
    [7700,5100,9000,6900,8200,9000,0]
]

# Routes
routes = {
    "I1":[0,1,2,3,4,5,6,0],
    "I2":[0,3,6,1,5,4,2,0],
    "I3":[0,2,5,3,6,1,4,0],
    "I4":[0,4,3,2,1,5,6,0],
    "I5":[0,6,4,1,3,2,5,0],
    "I6":[0,5,1,6,4,3,2,0],
    "Child1" :[0, 2,6,4,3,1,5,0]
}

def total_dist(route):
    return sum(dist[route[i]][route[i+1]] for i in range(len(route)-1))

# Compute
results = []
for name, rt in routes.items():
    d = total_dist(rt)
    f = 1 / d
    # simpan fitness sebagai string dengan 8 angka di belakang koma
    results.append([name, d, "{:.8f}".format(f)])

df = pd.DataFrame(results, columns=["Individu", "Total Distance", "Fitness"])
print(df.to_string(index=False))
