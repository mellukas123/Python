vowels = 'aeiou'
text = "Cupcake ipsum dolor sit amet chocolate bar. Lollipop caramels chupa chups cupcake I love biscuit pudding toffee I love. I love dessert oat cake candy biscuit donut cotton candy. Macaroon I love cookie lollipop biscuit."
amount_of_vowels = 0

for char in text:
     if char.lower() in vowels:
         amount_of_vowels += 1

print(f"Number of vowels in the text: {amount_of_vowels}")