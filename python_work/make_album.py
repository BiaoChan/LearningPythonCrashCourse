def make_album(singer_name, album_title, number_of_songs = ''):
	album = {'singer':singer_name, 'title':album_title}
	if number_of_songs:
		album['song_number'] = number_of_songs
	return album

# ~ album = make_album('cuijian', 'yiwusuoyou', 8)
# ~ print(album)

# ~ album = make_album('cuijian', 'yiwusuoyou')
# ~ print(album)

# ~ album = make_album('cuijian', 'yikuaihongbu')
# ~ print(album)

while True:
	print("\nPlease enter the infomations of the album.")
	print("Enter 'q' to quit.")
	
	singer = input("singer's name: ")
	if singer == 'q':
		break
	title = input("album's title: ")
	number = input("the number of songs: (optional, press enter to continue)")
	
	album = make_album(singer, title, number)
	print(album)
