start_power = 0
end_power = 63

for power in range(start_power, end_power + 1):
    print(2**power, end='\t')
    if (power - start_power + 1) % 8 == 0:
        print()
