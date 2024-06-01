#Write a program that would ask user to input text split the received text in half and print first part normally and a second part reversed to output.
#ask user to insert text
text = input("Please insert the text: ")
#how long is the text
text_length =len(text) + 1
#lets split the text
text_mid_point = text_length//2
text1 = text[0:text_mid_point]
text2 = text[:text_mid_point-1:-1]
print(text1, text2)

#Write a program that would ask user to input text split the received text in half and print first part normally and a second part reversed to output.

#ask for the text
input("Write the text: ")

# text = input("Enter some text to be reformatted: ")
# half_index = int(len(text)/2)
# first_half = text[:half_index]
# second_half = text[half_index:]
# print(f"this is the reformatted version: {first_half}{second_half[::-1]}")











