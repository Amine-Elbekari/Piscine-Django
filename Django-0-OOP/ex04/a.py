
class Playlist:
    
    def __init__(self, name="My Songs", songs=None):
        self.name = name
        if songs is not None and not isinstance(songs, list):
            self.songs = [songs]
        else:
            self.songs = [] if songs is None else songs

    def __str__(self):
        
        result = self.format_songs()
        return result

    def format_songs(self):
        
        result = ''
        if len(self.songs) == 0:
            return ''
        for song in self.songs:
            result += str(song) + '\n'
        return result
            

if __name__ == "__main__":
    
    b = Playlist("SOSN",Playlist())
    print(b)