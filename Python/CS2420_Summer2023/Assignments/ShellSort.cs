InsertionSortInterleaved(numbers, numbersSize, startIndex, gap) {
   i = 0
   j = 0
   temp = 0  // Temporary variable for swap

   for (i = startIndex + gap; i < numbersSize; i = i + gap) {
      j = i
      while (j - gap >= startIndex && numbers[j] < numbers[j - gap]) {
         temp = numbers[j]
         numbers[j] = numbers[j - gap]
         numbers[j - gap] = temp
         j = j - gap
      }
   }
}

ShellSort(numbers, numbersSize, gapValues) {
   for each (gapValue in gapValues) {
      for (i = 0; i < gapValue; i++) {
         InsertionSortInterleaved(numbers, numbersSize, i, gapValue)
      }
   }
}