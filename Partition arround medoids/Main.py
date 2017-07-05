import csv
import random
import sys
import timing


def column(matrix, i):
    return [row[i] for row in matrix]

#stablishing a value 1 for class <=50K and 0 for class >50K
def classe(matrix):
    output = []
    for row in matrix:
        if row == '<=50K':
            output.append(1)
        else:
            output.append(0)
    return output

def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices

def distance(matrix,medoid):
    d = 0
    for i in range(8):

        if matrix [i] != medoid[i]:

            d=d+1
    return d

def new_medoid(l):

    x = len(l)
    if x <= 1:
        sys.exit('list too short')
    else:
        if x % 2 == 1:
            medoid = l[int((x+1)/2)]
        else:
            medoid = l[int(x/2)]

    return medoid

def result(l1, l2, colms, itr):
    last_col_less = column(l1, colms)
    last_class_less = classe(last_col_less)
    last_col_more = column(l2, colms)
    last_class_more = classe(last_col_more)
    print(line)
    print('COST: ', final_cost)
    print(line)
    print('CONFUSION MATRIX: ')
    print()
    print(none, '||  <=50K  ', '||  >50K  ||')
    print('-' * 32)
    print('  <=50K  ||   ', last_class_less.count(1), '   ||  ', last_class_more.count(1), '  ||')
    print('-' * 32)
    print('   >50K  ||   ', last_class_less.count(0), '   ||  ', last_class_more.count(0), '  ||')
    print(line)
    print('PRECISION: ')
    print()
    if not last_class_less:
        print('<=50K precision: EMPTY LIST, NO VALUE POSSIBLE')
    else:
        print('<=50K precision: ',
              (last_class_less.count(1) / (last_class_less.count(1) + last_class_less.count(0))) * 100, '%')
    if not last_class_more:
        print('>50K precision: EMPTY LIST, NO VALUE POSSIBLE')
    else:
        print('>50K precision: ',
              (last_class_more.count(0) / (last_class_more.count(0) + last_class_more.count(1))) * 100, '%')
    print('total precision: ', ((last_class_less.count(1) + last_class_more.count(0)) / (last_class_less.count(1) +
                    last_class_less.count(0) + last_class_more.count(1) + last_class_more.count(0))) * 100, '%')
    print('=' * 40)
    print('TOTAL ITERATIONS: ', itr)


ncols = 8

line = '='*40
none = ' '*8
out_tup = []
sum_d1 = 0
sum_d0 = 0
# open file with autoclose when finish
with open(r'C:\Users\falgue\Desktop\adult.data.csv') as f:
    # omiting first line "header"
    next(f)
    reader = csv.reader(f)
    """in this section I made the treatment of .csv, first, read that and save in nested list a,
     in nested list (nl) b I delete all rows that contains symbol '?'. In c-set and c I remove repeated 
     possible lines in adult.data.csv. L1 is used to pass index number of columns to delete to the list in d,
     columns with strings formed only by numbers. The lists e and f split list d in two, each one with only class
     <=50k and >50K respectively. e2 and f2 are used to select 100 random instances of each one, and finally I 
     merge e2 and f2 in an out_tup list."""
    # creating list with all data from adult.data.csv
    a = list(reader)
    # deleting all lines with unknown values
    b = [t for t in a if '?' not in t]
    # deleting repeated lines
    c_set = set(tuple(x) for x in b)
    c = [list(x) for x in c_set]
    # deleting columns with string that have only integers
    L1 = [0, 2, 4, 10, 11, 12]
    d = (list([i for i in a if a.index(i) not in L1] for a in c))
    # creating two lists from list above, each one with unique class
    e = list(row for row in d if '<=50K' in row)
    f = list(row for row in d if '>50K' in row)
    # selecting randomly hundred instance of each list
    num_of_tup = 100
    e2 = random.sample(e, num_of_tup)
    f2 = random.sample(f, num_of_tup)
    # merging the hundred instances of each type in one list 'out_tup'
    for row in e2:
        out_tup.append(row)
    for row in f2:
        out_tup.append(row)

    last_col = column(out_tup, ncols)
    print('initial objects with <=50K: ', last_col.count('<=50K'))
    print('initial objects with >50K: ', last_col.count('>50K'))
    print(line)
    init_class = classe(last_col)
    index_mespetit = all_indices("<=50K", last_col)
    index_gran = all_indices(">50K", last_col)
    # get a random elem from class <=50K and create the first medoid for this class
    i_petit = random.sample(index_mespetit, 1)
    little_medoid = out_tup[i_petit[0]]
    # get a random elem from class >50K and create the first medoid for this class
    i_gran=random.sample(index_gran,1)
    big_medoid = out_tup[i_gran[0]]

    medoids_list = []
    medoids = []
    medoids.append(little_medoid)
    medoids.append(big_medoid)
    medoids_list.append(medoids)
    print("Initial little medoid: ", little_medoid)
    print("Initial big medoid: ", big_medoid)

    cluster_1 = []
    cluster_0 = []
    i = 0
    for row in out_tup:
        i = i+0
        d1 = distance(little_medoid, row)
        d0 = distance(big_medoid, row)
        if d1 <= d0:
            row.append(d1)
            cluster_1.append(row)
            sum_d1 = sum_d1 + d1
        else:
            row.append(d0)
            cluster_0.append(row)
            sum_d0 = sum_d0 + d0
    # sorting clusters by distance
    cluster_1.sort(key=lambda x: x[9])
    cluster_0.sort(key=lambda x: x[9])
    # deleting distance from rows in clusters
    for x in cluster_1:
        del x[9]
    for x in cluster_0:
        del x[9]

    new_lit_med = []
    new_big_med = []
    last_cluster_1 = []
    last_cluster_0 = []
    d1 = []
    d0 = []
    n = 0
    m = 0
    while (sorted(last_cluster_1) != sorted(cluster_1)) and (new_lit_med != little_medoid or new_big_med != big_medoid):
        medoids = []
        sum_d1 = 0
        sum_d0 = 0
        n = n+1
        x1 = column(cluster_1, ncols)

        if x1.count('<=50K')+x1.count('>50K') < 1:
            sys.exit('ERROR: empty list for cluster 1 (<=50K), impossible to continue')
        if (x1.count('<=50K')+x1.count('>50K')) % 2 == 1:
            y = (x1.count('<=50K')+x1.count('>50K'))/2
            new_lit_med = cluster_1[int(y)]
        else:
            y = ((x1.count('<=50K') + x1.count('>50K')) / 2)-1
            new_lit_med = cluster_1[int(y)]
        medoids.append(new_lit_med)

        x0 = column (cluster_0, ncols)
        if x0.count('<=50K') + x0.count('>50K') < 1:
            sys.exit('ERROR: empty list for cluster 0 (>50K), impossible to continue')
        if (x0.count('<=50K') + x0.count('>50K')) % 2 == 1:
            y = (x0.count('<=50K') + x0.count('>50K')) / 2
            new_big_med = cluster_0[int(y)]
        else:
            y = ((x0.count('<=50K') + x0.count('>50K')) / 2) - 1
            new_big_med = cluster_0[int(y)]
        medoids.append(new_big_med)

        for row in out_tup:
            i = i + 0
            d1 = distance(new_lit_med, row)
            d0 = distance(new_big_med, row)
            if d1 <= d0:
                row.append(d1)
                last_cluster_1.append(row)
                sum_d1 = sum_d1 + d1
            else:
                row.append(d0)
                last_cluster_0.append(row)
                sum_d0 = sum_d0 + d0

        last_cluster_1.sort(key=lambda x: x[9])
        last_cluster_0.sort(key=lambda x: x[9])
        for x in last_cluster_1:
            del x[9]
        for x in last_cluster_0:
            del x[9]

        if (sorted(last_cluster_1) == sorted(cluster_1)) or (new_lit_med == little_medoid and new_big_med == big_medoid):
            final_cost = sum_d1 + sum_d0
            result(last_cluster_1, last_cluster_0, ncols, n)
            sys.exit(0)

        for t in medoids_list:
            if medoids == t:
                final_cost = sum_d1 + sum_d0
                result(cluster_1, cluster_0, ncols, n)
                print(line)
                print("IMPORTANT: stop execution to avoid to enter in a loop without end because of medoids "
                      "for example like a wheel like this: A-B, C-D, E-F, A-B, C-D, E-F, A-B, C-D, etc.")
                sys.exit(0)

        medoids_list.append(medoids)
        cluster_1 = last_cluster_1
        cluster_0 = last_cluster_0
        last_cluster_1 = []
        last_cluster_0 = []
        little_medoid = new_lit_med
        big_medoid = new_big_med
        new_lit_med = []
        new_big_med = []
        d1 = []
        d0 = []
    #if never enter into the while
    final_cost = sum_d1 + sum_d0
    result(cluster_1, cluster_0, ncols, n)
    sys.exit(0)


