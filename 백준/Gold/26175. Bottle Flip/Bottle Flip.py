def center_of_mass_height(water_height, bottle_height, air_density, water_density):
    air_volume = (bottle_height * bottle_height - water_height * water_height) * air_density * 0.5
    water_volume = water_height * water_height * water_density * 0.5
    total_weight = water_height * water_density + (bottle_height - water_height) * air_density
    return (air_volume + water_volume) / total_weight


bottle_height, radius, air_density, water_density = map(float, input().split())
epsilon = 1e-10
left, right = 0, bottle_height

while right - left >= epsilon:
    mid_left = left + (right - left) / 3
    mid_right = right - (right - left) / 3
    if center_of_mass_height(mid_left, bottle_height, air_density, water_density) > center_of_mass_height(mid_right, bottle_height, air_density, water_density):
        left = mid_left
    else:
        right = mid_right

print(f"{left:.10f}")