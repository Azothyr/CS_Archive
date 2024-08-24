SelectionSort(numbers, numbersSize) {
    i = 0
    j = 0
    indexSmallest = 0
    temp = 0  // Temporary variable for swap
   
    for (i = 0; i < numbersSize - 1; ++i) {
      
        // Find index of smallest remaining element
        indexSmallest = i
        for (j = i + 1; j < numbersSize; ++j) {
         
            if ( numbers[j] < numbers[indexSmallest] ) {
                indexSmallest = j
            }
        }
      
        // Swap numbers[i] and numbers[indexSmallest]
        temp = numbers[i]
        numbers[i] = numbers[indexSmallest]
        numbers[indexSmallest] = temp
    }
}

main() {
    numbers[] = { 10, 2, 78, 4, 45, 32, 7, 11 }
    NUMBERS_SIZE = 8
    i = 0
   
    print("UNSORTED: ")
    for (i = 0; i < NUMBERS_SIZE; ++i) {
        print(numbers[i] + " ")
    }
    printLine()
   
    SelectionSort(numbers, NUMBERS_SIZE)
   
    print("SORTED: ")
    for (i = 0; i < NUMBERS_SIZE; ++i) {
        print(numbers[i] + " ")
    }
    printLine()   
}