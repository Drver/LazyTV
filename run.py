from VideoDB import Video

video_path_array = ["video1", "video2"]
pot_player_path = 'path'
db = Video()

while 0 < 1:
    for video_path in video_path_array:
        video_info = db.select_video_info_by_path(video_path)[0]
        start = db.get_video_info_start(video_info)
        cost = db.get_video_info_cost(video_info)

        cmd = pot_player_path + " " + video_path + " " + "/seek=" + start

        print(cmd)
