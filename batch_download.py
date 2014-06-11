import sys
sys.path.append("/Users/Richo/Desktop/Flickr_Batch_Download")

import flickr_api
import requests
import json
import csv

API_KEY =  'fb5a21081f69661138906a829c3a73de'
API_SECRET = 'bcf6efadd8fd2aaa'

flickr_api.set_keys(api_key = API_KEY, api_secret = API_SECRET)

user = flickr_api.Person.findByUserName('Woodrow Wilson Presidential Library Archives')
photos = user.getPhotos()

# print photos.info.pages # the number of available pages of results
# print photos.info.page  # the current page number
# print photos.info.total # total number of photos

# print photos[0]

# for photo in photos:
	# Photo(id='9092395003', title='Shapes Study 20')
	# print photo

f = open('test_10_images.csv', 'w')
w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
w.writerow(['location', 'title', 'description', 'license', 'dc:title', 'dc:description', 'dc:creator', 'dc:type'])

# for i in range(0, 10):
for photo in photos:
	url = 'https://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=' + API_KEY + '&photo_id=' + photo.id + '&format=json&nojsoncallback=1'
	response = requests.get(url)
	data = response.json()
	urls = data['sizes']['size']
	for item in urls:
		if item['label'] == 'Original':
			row = [item['source'].encode('utf-8').replace("https", "http"), photo.title.encode('utf-8'), 'Description input', 'http://creativecommons.org/publicdomain/mark/1.0/', photo.title.encode('utf-8'), 'Description input', 'stefanb', 'Image']
			# print row
			w.writerow(row)

f.close()
