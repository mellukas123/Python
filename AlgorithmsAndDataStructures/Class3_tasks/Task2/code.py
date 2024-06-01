import json
import csv


# Function for cleaning the data
def clean_data(products):
    cleaned_products = []
    for product in products['data']:
        cleaned_product = {
            'id': product.get('id', ''),
            'name': product.get('name', ''),
            'category': product.get('category', ''),
            'price': product.get('price', ''),
            'currency': product.get('currency', ''),
            'stock': product.get('stock', ''),
            'description': product.get('description', ''),
            'manufacturer': product.get('manufacturer', ''),
            'warranty': product.get('warranty', ''),
            'extra_field': product.get('extra_field', '')
        }
        cleaned_products.append(cleaned_product)
    return cleaned_products


# Function for saving data to CSV
def save_to_csv(cleaned_data, csv_file_path):
    fieldnames = ['id', 'name', 'category', 'price', 'currency', 'stock', 'description', 'manufacturer', 'warranty',
                  'extra_field']
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)


# Main function
def main():
    json_file_path = 'electronics_products.json'
    csv_file_path = 'electronics_products.csv'

    # Open the JSON file and read its content
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Clean the data
    cleaned_data = clean_data(data)

    # Save the cleaned data to a CSV file
    save_to_csv(cleaned_data, csv_file_path)
    print("CSV file created successfully.")


# Run the program
if __name__ == "__main__":
    main()
