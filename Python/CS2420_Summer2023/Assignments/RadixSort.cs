// Returns the maximum length, in number of digits, out of all elements in the array
RadixGetMaxLength(array, arraySize) {
    maxDigits = 0
    for (i = 0; i < arraySize; i++) {
        digitCount = RadixGetLength(array[i])
        if (digitCount > maxDigits)
            maxDigits = digitCount
    }
    return maxDigits
}

// Returns the length, in number of digits, of value
RadixGetLength(value) {
    if (value == 0)
        return 1

    digits = 0
    while (value != 0) {
        digits = digits + 1
        value = value / 10
    }
    return digits
}


RadixSort(array, arraySize) {
    buckets = create array of 10 buckets

        // Find the max length, in number of digits
        maxDigits = RadixGetMaxLength(array, arraySize)
        
    pow10 = 1
    for (digitIndex = 0; digitIndex < maxDigits; digitIndex++) {
        for (i = 0; i < arraySize; i++) {
            bucketIndex = abs(array[i] / pow10) % 10
            Append array[i] to buckets[bucketIndex]
        }
        arrayIndex = 0
        for (i = 0; i < 10; i++) {
            for (j = 0; j < buckets[i]⇢size(); j++) {
                array[arrayIndex] = buckets[i][j]
                arrayIndex = arrayIndex + 1
            }
        }
        pow10 = pow10 * 10
        Clear all buckets
    }

    negatives = all negative values from array
        nonNegatives = all non-negative values from array
        Reverse order of negatives
        Concatenate negatives and nonNegatives into array
}