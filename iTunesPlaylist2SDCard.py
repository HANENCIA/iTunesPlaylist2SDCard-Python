import pandas as pd
import os
import shutil
import glob

ITUNES_PLAYLIST_LOCATION = './iTunesPlaylist'
TARGET_MUSIC_LOCATION = './Music'

def copy_m4a_file(playlist_location, dest_location):
    file_location = read_location(playlist_location)

    if not os.path.exists(dest_location):
        os.makedirs(dest_location)

    f = open(str(dest_location) + '\\' + str(os.path.splitext(os.path.basename(playlist_location))[0])+'.m3u', 'w', encoding='utf-8')
    f.write('#EXTINF')
    f.write('\n')
    
    for list in file_location:
        list_dir = os.path.basename(os.path.dirname(list))
        list_file = os.path.basename(list)
        dest_dir = str(dest_location)+'\\'+str(list_dir)
        dest_file = str(dest_location)+'\\'+str(list_dir)+'\\'+str(list_file)
        m3u_dest_file = str(list_dir) + '\\' + str(list_file)
        

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        if not os.path.exists(dest_file):
            shutil.copy(list, dest_file)
            print('COPYING: ' + str(dest_file))
        else:
            print("File already exists: " + str(dest_file))
        f.write(m3u_dest_file)
        f.write('\n')
    f.close()


def read_location(filename):
    playlist = pd.read_csv(filename, sep='\t', encoding='utf-16-le')['위치']
    return playlist


def read_playlist(dirname):
    return glob.glob(str(dirname)+'/*.txt')


def main():
    playlist = read_playlist(ITUNES_PLAYLIST_LOCATION)
    target_dir = str(TARGET_MUSIC_LOCATION)
    for list in playlist:
        copy_m4a_file(list, target_dir)

    
if __name__ == "__main__":
    main()