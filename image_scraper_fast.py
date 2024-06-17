from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

search_term = input("Enter the search term: ")
limit = int(input("Enter the number of images to download: "))

response().download(search_term, limit=limit)
            