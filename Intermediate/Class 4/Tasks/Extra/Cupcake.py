import concurrent.futures
import re

def process_paragraph(paragraph):
    processed_sentences = []
    for sentence in paragraph.split('.'):
        # Lowercase every letter
        sentence = sentence.lower()

        # Capitalize 'C' at the beginning of the sentence
        if sentence.startswith(' c'):
            sentence = 'C' + sentence[1:]

        # Remove the sentence if it starts with 'C'
        if sentence.startswith('c'):
            continue

        # Reverse the sentence if it contains the word 'roll'
        if 'roll' in sentence:
            sentence = sentence[::-1]

        # Capitalize the entire sentence if it contains the word 'bears'
        if 'bears' in sentence:
            sentence = sentence.upper()

        processed_sentences.append(sentence.strip())

    return '\n'.join(processed_sentences)

def main():
    text = """
Cupcake ipsum dolor sit amet muffin marshmallow biscuit. Cookie jelly beans sugar plum dragée sesame snaps ice cream liquorice. Tiramisu chocolate pudding gingerbread brownie fruitcake sugar plum cake danish. Lollipop liquorice icing apple pie gingerbread gingerbread chocolate gingerbread gingerbread.
Shortbread bear claw pie halvah toffee cupcake pudding icing soufflé. Sweet chocolate bar candy jujubes dessert. Pudding bonbon bear claw cheesecake sesame snaps.
Macaroon croissant oat cake candy wafer. Pastry candy dragée tart chupa chups danish cake caramels. Tootsie roll cake jelly beans candy canes pastry jelly candy marzipan chupa chups. Tootsie roll gingerbread brownie tiramisu jujubes chocolate donut apple pie dessert.
Chupa chups jelly-o gingerbread muffin pastry marshmallow. Gummi bears marshmallow pie cake bear claw pudding pastry chupa chups. Marzipan chocolate muffin biscuit candy canes. Liquorice cheesecake biscuit liquorice croissant ice cream.
Sweet roll fruitcake dragée macaroon jelly danish ice cream tart. Marshmallow macaroon cake toffee candy canes lollipop tiramisu chocolate bar. Cake chocolate cake tart dragée dragée powder cookie jelly beans croissant.
"""

    # Split the text into paragraphs
    paragraphs = text.split('\n')

    # Process each paragraph concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        processed_paragraphs = list(executor.map(process_paragraph, paragraphs))

    # Write the final result to a file
    with open("processed_text.txt", "w") as file:
        for paragraph in processed_paragraphs:
            file.write(paragraph + '\n\n')

if __name__ == "__main__":
    main()
