def temperature(measurements):
    if len(measurements) > 7:
        measurements = sorted(measurements)[1:-1]
    else:
        measurements = sorted(measurements)[:3]
    return tuple(measurements)

print(temperature((26, 24, 28, 29, 32, 27, 30, 31, 29)),
      temperature((24, 22, 25, 27, 30, 30, 29)),
      temperature((29, 28, 30, 26)), sep='\n')