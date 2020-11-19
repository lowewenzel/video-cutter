# Video Timestamps Cutter CLI

Command line interface for cutting one video into multiple parts utilizing `moviepy`, via a CSV.

## Installation

Either download this as a zip, or clone the repo. Utilize a virtual env (I used 3.7 to develop).

```bash
git clone https://github.com/lowewenzel/video-cutter.git

cd video-cutter

# virtual env
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage

For simplicity, place two files in the same folder as `main.py`. (You can also use any directory reachable by bash and python).

```bash
python main.py video_file.mp4 rows.csv
python main.py "video with spaces.mp4" "csv with spaces.csv"
```

This will create your video files in the `out/` directory.

#### Video File

Format can be any format supported by [moviepy](https://zulko.github.io/moviepy/)(which is a lot).

#### CSV file

This is where the parts are separated/dictated. Use the following CSV format:

###### As a CSV

```csv
File Title,Start Time,End Time
Intro,0:00:02,0:01:16
Chapter 1,0:01:17,0:24:35
Chapter 6-10,0:24:37,0:34:41
Credits,0:34:46,0:36:04
```

###### As a table

| File Title   | Start Time | End Time |
| ------------ | ---------- | -------- |
| Intro        | 0:00:02    | 0:01:16  |
| Chapter 1    | 0:01:17    | 0:24:35  |
| Chapter 6-10 | 0:24:37    | 0:34:41  |
| Credits      | 0:34:46    | 0:36:04  |

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
