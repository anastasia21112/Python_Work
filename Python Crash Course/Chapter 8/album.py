def make_album(artist_name, album_title, num_songs=''):
    if num_songs:
        album = {'artist name' : artist_name, 'album title' : album_title, 'songs stored' : num_songs}
    else:
        album = {'artist name' : artist_name, 'album title' : album_title}
    return album

pfalbum = make_album('Pink Floyd', 'Dark Side of the Moon')
print(pfalbum)
