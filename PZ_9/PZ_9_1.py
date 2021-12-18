# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных стран. Определить какие марки машин
# были доставлены во все указанные страны, какие в некоторые страны и какие не доставлены ни в одну страну.

cars = {'BMW', 'Mercedec', 'Volvo', 'Audi'}
russia = {'BMW', 'Mercedec'}
france = {'Volvo', 'BMW'}
poland = {'Mercedec', 'Volvo', 'BMW'}
spain = {'Mercedec', 'Volvo', 'BMW'}
print('Во все страны были доставлены: ', russia & france & poland & spain)
print('Ни в одну страну не были доставлены: ', cars - russia - france - poland - spain)
print('В некоторые страны были доставлены: ', russia | france | poland | spain)
