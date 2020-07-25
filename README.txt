  __  __                 _ _             
 |  \/  |               | (_)            
 | \  / | ___   ___   __| |_ _ __  _   _ 
 | |\/| |/ _ \ / _ \ / _` | | '_ \| | | |
 | |  | | (_) | (_) | (_| | | |_) | |_| |
 |_|  |_|\___/ \___/ \__,_|_| .__/ \__, |
                            | |     __/ |
                            |_|    |___/
                            
############## USER GUIDE ##################

This guide will explain how to get the app up and running on your PC. 
You'll be listening to songs you actually like in no time.

1. Clone the repository.
	a. Install the latest version of Git on your PC : https://git-scm.com/downloads
	b. Once it finishes, open File Explorer and find a directory where you want the Moodipy files to be cloned.
	c. Right-click in the empty space in the window (where your files would appear), and click "Git Bash Here."
	d. A terminal window should appear. Copy and paste the following, then hit enter : 
			git clone https://github.com/stpilks99/Moodipy
	e. The Moodipy folder should appear in the directory once cloning is done.
  
2. Open the repository in a Python IDE and install prerequisites.
	a. If you don't have Python already installed, grab the latest version from : https://www.python.org/downloads/
	Make sure you hit "Install Now" to get all the required components to run Moodipy.
	b. In your preferred Python IDE, select the "Open Project Folder" option and find the Moodipy folder you just cloned.
	c. Once it opens, you should see all the files in the working directory in your IDE. 
	d. There are a few prereqs you need before running the app, but you can install them using the package
	manager called pip. Open a Python terminal window (you can just search for Python in the Windows search bar 
	and it should come up as an app) and run each of the following commands:
			pip install spotipy
			pip install Pillow
	Spotipy is a Python library for Spotify that makes API calls a lot easier. Pillow is a fork of the Python
	Image Library that is capable of opening many types of image files - this is needed for the GUI.

3. Run GUI.py.
	a. A login window will appear. Enter your Spotify username, click the "Login with Spotify" button and you'll be
	taken to a Spotify webpage asking for authorization. This is so Moodipy can add/remove playlists/songs and see 
	where your musical tastes lie. No, we do not sell your personal data.
	b. Login with your Spotify credentials on the webpage and click "Authorize." The Moodipy main menu will open
	and you'll see all the playlists in your library.
	
