Initialization :

        text  = "tadadattaetadadadafa"
        pattern = 'dada'
        t = len(text)
        p = len(pattern)
        count = 0

        1. A for loop with variable i will run from 0 to length of the given text
        2. Inside the loop a while loop will run with condition variable j is less than the length of the pattern where j is initialized with 0.
        3. In that while loop if the index value of text with the pattern then the loop will break and every time it will check whether the value of j is equal to p and then the value of i will be increased by 1.
        4. If the index value of the text is matched with the pattern index value then j will be increased by 1 and the while loop will run until the value of j and p are not equal.
        5. If j and p are equal, this means our pattern size is over and we have found a full match and the count will be increased by 1 and the value of j will be reset to 0.

1 to 5 will run till the range of i is not over.

