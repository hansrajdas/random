import collections


Person = collections.namedtuple('Person', ['name', 'birth', 'death'])

def get_min_max_year(persons):
    _min = persons[0].birth
    _max = persons[0].birth
    for idx in range(1, len(persons)):
        _min = min(_min, persons[idx].birth)
        _max = max(_max, persons[idx].birth)
    return _min, _max

def get_year_with_population(persons):
    if not persons:
        return -1

    _min, _max = get_min_max_year(persons)  # 2001, 2009
    population = [0 for _ in range(_max - _min + 2)]  # 2009 - 2001 = 8 + 1, len = 9
    for p in persons:
        birth = p.birth - _min  # 2009 - 2001 = 8
        death = p.death - _min  # 2005 - 2001 = 4
        population[birth] += 1
        if death + 1 < len(population):
            population[death + 1] -= 1

    max_count = 0
    count = 0
    max_year = _min
    for year in range(len(population)):
        count += population[year]
        if count > max_count:
            max_count = count
            max_year = year + _min # 0 + 2001
    return max_year


def main():
  persons = [                  # 0 1 2 3 4
    Person('P1', 2001, 2005),  # 1 1 1 1 1
    Person('P2', 2005, 2009),  #         
    Person('P3', 2003, 2020),  #     2
    Person('P3', 2002, 2002),  #   2
  ]
  print ('Year with max population is: %d' % get_year_with_population(persons))

  persons = [
    Person('P1', 2001, 2005),
    Person('P2', 2009, 2019),
  ]
  print ('Year with max population is: %d' % get_year_with_population(persons))

if __name__ == '__main__':
  main()


# Output:
# ---------------------------------
# Year with max population is: 2005
# Year with max population is: 2001
