f = open('countries.txt','r')

countries = []

for line in f:
    line = line.strip()
    countries.append(line)

f.close()

print(countries)
print(len(countries))

counter = 0
for country in countries:
    if country[0] == 'T':
        print(country)
        counter = counter + 1
print(counter)
