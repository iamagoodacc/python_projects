def Bubble_Sort(Array):
    #FUNCTION: Loops through items and swaps them until larger items are at the end
    ArrayToSort = Array
    print(f'Bubble sorting array: {ArrayToSort}...')
    SortsPerformed = 0
    SwapsPerformed = 0
    FinishedSwapping = False #To keep running the sort until the array is fully sorted
    while not FinishedSwapping:
        FinishedSwapping = True
        SortsPerformed += 1 #Increment total sort count
        for i in range(len(ArrayToSort)-1): #Loop through array
            #print(f'Comparing {ArrayToSort[i]} with {ArrayToSort[i+1]}...')
            if ArrayToSort[i] > ArrayToSort[i+1]: #If first item is bigger than the second item
                #print(f'Swapping values...')
                SwapsPerformed += 1
                ArrayToSort[i], ArrayToSort[i+1] = ArrayToSort[i+1], ArrayToSort[i] #Swap them
                FinishedSwapping = False
        print(f'After pass {SortsPerformed}, the current array is: {ArrayToSort}')
    print(f'Number of sorts performed: {SortsPerformed-1}') #-1 because last one is just a sort check to ensure everything is sorted
    print(f'Number of swaps performed: {SwapsPerformed}')
    return ArrayToSort

def Insertion_Sort(Array):
    #Splits array into two parts: sorted and unsorted by continuously moving each value from unsorted list into the sorted list in the correct place
    SortedArray = []
    UnsortedArray = Array

    for i in range(len(UnsortedArray) - 1):

        LowestValue = UnsortedArray[i]

        for v in range(len(UnsortedArray) - 1):
            if UnsortedArray[v] > LowestValue:
                LowestValue = UnsortedArray[i]


#Array = [10, 4, 2, 5, 24, 30, 23, 7, 12, 10] - Numbers
#Array = ['CD', 'DE', 'AB', 'BC', 'GH', 'FG', 'EF'] - Characters
Array = ['Olivia', 'Amelia', 'Ava', 'Isla', 'Emily', 'Mia', 'Isabella', 'Sophia', 'Ella', 'Grace']
Array = Bubble_Sort(Array)
print(Array)