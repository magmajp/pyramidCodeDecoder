# pyramidCodeDecoder
Little project made for an interview

This is a function that takes a file as input, parses the text, and decodes and outputs a secret message.

Files are in the format:

5 you

1 I

6 computers

2 cats

4 dogs

3 love

<br/>

The words are sorted into a "pyramid structure":

   1
   
  2 3
  
 4 5 6
 
The code is then read down the side of the pyramid so 1, 3, 6...
The output is then a single string containing the final message, in the above example it would be:
"I love computers"


# Solution Explanation
The basic idea is to parse the text where each line becomes a node with a number and text component. We then sort the nodes by number into a Linked List. Despite the name we don't need a proper pyramid structure because this is actually just a list with strange wrapping. Once you have your sorted Linked List you just go through and grab the nodes at the pyramid numbers 1,3,6,10...
