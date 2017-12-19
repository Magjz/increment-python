def increment(liste):
    print([i + 1 if(isinstance(i, int)) else i for i in liste])

increment([3, 4 , 9, 'a', 'qvb'])
