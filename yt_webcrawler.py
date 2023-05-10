import pytube
from youtubesearchpython import *
import re
from pytube import Playlist
from pytube import YouTube

playlist_url = "https://www.youtube.com/playlist?list=PLd94ixR5XZyorl-7iH5bIiWR47Fnvrnnn"
playlist = Playlist(playlist_url)
print('List size = ', len(playlist))

total_view_count = 0
total_comment_count = 0
total_like_count = 0
countuse = 0
for urll in playlist:
    if countuse < 100:
        video = YouTube(urll)

        like_template = r'[0-9]{1,3},?[0-9]{0,3},?[0-9]{0,3} like'
        str_likes = re.search(like_template, str(video.initial_data)).group(0)
        likes = int(str_likes.split(' ')[0].replace(',', ''))
        comments = Comments(urll)
        
        try:
            while comments.hasMoreComments:
                comments.getNextComments()
            total_view_count += video.views
            total_like_count += likes
            total_comment_count += len(comments.comments["result"])
            print(str(countuse) + ': ' + video.title +' view:' + str(video.views) + ' comments:'+str(len(comments.comments["result"])) + ' like:'+str(likes))
            countuse += 1
        except:
            continue
    elif countuse == 100:
        break
countuse += 1
print('--------total--------')
print('total_view', total_view_count)
print('total_comment', total_comment_count)
print('total_like', total_like_count)
if countuse != 100:
    view_count = int(total_view_count / len(playlist))
    comment_count = int(total_comment_count / len(playlist))
    like_count = int(total_like_count / len(playlist))
else:
    view_count = int(total_view_count / 100)
    comment_count = int(total_comment_count / 100)
    like_count = int(total_like_count / 100)

print('--------result--------')
print('view = ', view_count)
print('comment = ', comment_count)
print('like = ', like_count)