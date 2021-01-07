import os
import sys

def image_extension(f):
	f = f.lower()
	return f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')

def delete_unused_images(dirname):
	html_files = [f for f in os.listdir(dirname) if f.endswith('.html')]
	website_contents = ""
	for filename in html_files:
		with open(os.path.join(dirname, filename), 'r') as f:
			data = f.read().replace('\n', '')
		website_contents += data
	website_contents = website_contents.lower()

	to_delete = []
	image_files = [f for f in os.listdir(dirname) if image_extension(f)]
	for filename in image_files:
		if filename.lower() not in website_contents:
			print(filename)
			to_delete.append(filename)

	for filename in to_delete:
		os.remove(os.path.join(dirname, filename))

def main():
	args = sys.argv[1:]
	dirname = args[0]

	delete_unused_images(dirname)

if __name__ == '__main__':
	main()