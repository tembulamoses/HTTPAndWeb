"""
Simple app to search for location address using the google geocode api
"""
import urllib.request
import urllib.parse
import json
# first, the api url core




		

def get_location_address():

	api_url= 'https://maps.googleapis.com/maps/api/geocode/json?'
	# the client input that would be used for full url
	print('enter location by name, official initials, or global position. You will get the details of the place')
	user_input = input('Enter Location: ')

	if isinstance(user_input, int):
		print ('Currently not handling integers. Try again')
		return get_location_address()

	# completing the url
	complete_url = api_url + urllib.parse.urlencode({'address': user_input})
	#  requesting for information using HTTp get method
	# the data returned is usually in json form thus 
	json_data = urllib.request.urlopen(complete_url)
	read_json_data = json.loads(json_data.read().decode('utf-8'))

	print()
	response_status= read_json_data['status']
	# print (read_json_data)
	
	if response_status != 'OK':
		print('Location details Not found. Something could have gone wrong\n')
		print('You might have entered an unrecognised location')
		return get_location_address()
	else:
		try:
			address = 'Address for ' + user_input +'\n'+ read_json_data['results'][0]['formatted_address']
		except(IndexError, socket.gaierror):
			print("That's not a proper location, Please enter simple location")
			return get_location_address()
		else:
			print(address)