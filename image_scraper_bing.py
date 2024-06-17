from bing_image_downloader import downloader

search_term = input("Enter the search term: ")
limit = int(input("Enter the number of images to download: "))

downloader.download(search_term, limit=limit, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60)