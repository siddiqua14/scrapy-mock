import os
import requests
from sqlalchemy.orm import sessionmaker
from scrapyproject.models import Product, engine

class ScrapyprojectPipeline:
    def __init__(self):
        # Initialize database session
        self.Session = sessionmaker(bind=engine)
        # Define the directory for storing images inside the container
        self.image_dir = "/images"  # Inside the container
        # Ensure the directory exists
        os.makedirs(self.image_dir, exist_ok=True)

    def process_item(self, item, spider):
        # Download and save the image
        image_url = item['image_url']
        image_response = requests.get(image_url, stream=True)
        
        if image_response.status_code == 200:
            # Save image to the container's image directory
            image_filename = os.path.join(self.image_dir, os.path.basename(image_url))
            with open(image_filename, 'wb') as f:
                f.write(image_response.content)

            # Save product details (including the image path) in the database
            session = self.Session()
            product = Product(
                name=item['name'],
                price=item['price'],
                url=item['url'],
                image_path=image_filename  # Path to the image in the container
            )
            session.add(product)
            session.commit()
            session.close()

        # Return the item to allow Scrapy to continue the pipeline
        return item
