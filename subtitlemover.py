parser = argparse.ArgumentParser()

parser.add_argument('--dir_path', help='path to directory where movies are located')
parser.add_argument('--sub_folder_name', help='name of folder subtitles are located in')

args = parser.parse_args()

dir_path = args.dir_path
sub_folder_name = args.sub_folder_name

if not dir_path:
	print('positional argument "dir_path" not specified (defaulting to "./"')
	dir_path = './'
if not sub_folder_name:
	print('positional argument "sub_folder_name" not specified (defaulting to "Subs/"')
	sub_folder_name = 'Subs'

# List all movie folders in "Movies" folder
for folder in os.listdir(dir_path):
	# Get contents of each folder
	items = os.listdir(os.path.join(dir_path, folder))
	# Check if an mp4 file exists, if not continue
	movie = [i for i in items if i.endswith('.mp4')]
	extension = '.mp4'
	if not movie:
		movie = [i for i in items if i.endswith('.mkv')]
		extension = '.mkv'
		if not movie:
			print("Media file not found for {}...".format(folder))
			continue
	movie_name = movie[0]
	print('Checking for subtitles in {}...'.format(os.path.join(folder, sub_folder_name)))
	
	if('{}.{}.srt'.format(movie_name.rstrip(extension), 'en') in items):
		print('Found existing subtitle file, skipping...')
		continue