from moviepy.editor import *
from pytimeparse.timeparse import timeparse
import csv


def render_video_sections(file_name, video_sections):
    video_file = VideoFileClip(file_name)

    for section in video_sections:
        start_time = timeparse(section['start_time'])
        end_time = timeparse(section['end_time']) + 1
        title = "out/" + section['title'] + ".mp4"

        clip = video_file.subclip(start_time, end_time)

        clip.write_videofile(title,
                             audio_codec='aac',
                             temp_audiofile='temp-audio.m4a',
                             remove_temp=True
                             )


def read_csv_to_video_sections(file_name):
    with open(file_name, newline='') as csv_file:
        rows = csv.reader(csv_file)
        # skip first line
        next(rows)

        video_sections = []
        for row in rows:
            section = {
                'title': row[0],
                'start_time': row[1],
                'end_time': row[2],
            }
            video_sections.append(section)

        return video_sections


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Err: Missing file inputs! \n\n--Proper Usage--")
        print('python main.py video_file.mp4 rows.csv')
        print(
            'python main.py "video with spaces.mp4" "csv with spaces.csv"\n----------------')
        exit()

    # File names
    video_file = sys.argv[1]
    csv_file = sys.argv[2]

    video_sections = read_csv_to_video_sections(csv_file)
    render_video_sections(video_file, video_sections)
