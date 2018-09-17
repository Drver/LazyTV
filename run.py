from VideoDB import Video
import subprocess
import time

video_path_array = ["D:/Movie/[碟中谍1][英语配音][中英双字]/碟中谍1.mp4", 
					"D:/Movie/[碟中谍2][英语配音][中英双字]/碟中谍2.mp4", 
					"D:/Movie/[碟中谍3][英语配音][中英双字]/碟中谍3.mp4", 
					"D:/Movie/[碟中谍4][英语配音][中英双字]/碟中谍4.mp4", 
					"D:/Movie/[碟中谍5][英语配音][中英双字]/碟中谍5.mp4", 
					"D:/Movie/[哈利波特与魔法石][英语配音][中英双字]/哈利波特与魔法石.mp4", 
					"D:/Movie/[哈利波特与密室][英语配音][中英双字]/哈利波特与密室.mp4", 
					"D:/Movie/[哈利波特与阿兹卡班的囚徒][英语配音][中英双字]/哈利波特与阿兹卡班的囚徒.mp4", 
					"D:/Movie/[哈利波特与火焰杯][英语配音][中英双字]/哈利波特与火焰杯.mp4", 
					"D:/Movie/[哈利波特与凤凰社][英语配音][中英双字]/哈利波特与凤凰社.mp4", 
					"D:/Movie/[哈利波特与混血王子][英语配音][中英双字]/哈利波特与混血王子.mp4", 
					"D:/Movie/[哈利波特与死亡圣器(上)][英语配音][中英双字]/哈利波特与死亡圣器(上).mp4", 
					"D:/Movie/[哈利波特与死亡圣器(下)][英语配音][中英双字]/哈利波特与死亡圣器(下).mp4"]
pot_player_path = 'C:/PotPlayer/PotPlayerMini64.exe'
db = Video()

while 0 < 1:
    for video_path in video_path_array:
        video_info = db.select_video_info_by_path(video_path)[0]
        start = db.get_video_info_start(video_info)
        cost = db.get_video_info_cost(video_info)

        cmd = pot_player_path + " " + video_path + " " + "/seek=" + start

        subprocess.Popen(cmd)
        time.sleep(cost)
