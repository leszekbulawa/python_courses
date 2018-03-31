scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 
              'Isaac Newton', 'Dimitri Mendeleev', 'Antoine Lavoisier', 
              'Carl Linnaeus', 'Alfred Wegner', 'Charles Darwin']

print(sorted(scientists, key=lambda name: name.split()[-1]))
