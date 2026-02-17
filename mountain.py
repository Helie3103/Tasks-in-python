data = [
    ["MountainA","MountainB","MountainC","MountainD","MountainE"],
    [10,12,15,25],      
    [4,3,12],           
    ["ahd","ahd"]       
]

output = {}

key = data[0]
width = data[1]
height = data[2]
location = data[3]

while (len(width) < len(key)):
    width.append(0)

while (len(height) < len(key)):
    height.append(0)

while (len(location) < len(key)):
    location.append("Not available")
    
for i in range(len(key)):
    output[key[i]] = {
        "width": width[i],
        "height": height[i],
        "location": location[i]
    }

for keys,values in output.items():
    print(keys,values)
