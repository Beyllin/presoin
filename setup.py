from setuptools import setup

README = open("README.md", "r")
readmed = README.read()
README.close()

setup(
	name = "presoin",
	version = "2023.05.01",
	description = "Downloads songs, albums or playlists from deezer",
	long_description = readmed,
	long_description_content_type = "text/markdown",
	license = "CC BY-NC-SA 4.0",
	python_requires = ">=3.8",
	author = "Beyllin",
	author_email = "Pandasoa@protonmail.com",
	url = "https://github.com/Beyllin/presoin",

	packages = [
		"deezloader",
		"deezloader/models", "deezloader/spotloader",
		"deezloader/deezloader", "deezloader/libutils"
	],

	install_requires = [
		"mutagen", "pycryptodome", "requests",
		"spotipy", "tqdm", "fastapi",
		"uvicorn[standard]", "librespot"
	],

	scripts = [
		"deezloader/bin/deez-dw.py",
		"deezloader/bin/deez-web.py"
	]
)
