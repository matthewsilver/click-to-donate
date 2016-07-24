# click-to-donate
Automatically performs all clicks on click-to-donate website <a href= "http://www.care2.com/click-to-donate/" target="_blank">care2</a>.

After downloading the script to the desired directory my/directory/path, insert the following code (mac) to add it to the PATH variable and run it from anywhere in the terminal:

export PATH="$PATH:/usr/local/bin"
cd my/directory/path
mv click_sites.py /usr/local/bin/click_sites.py
cd /usr/local/bin
chmod +x click_sites.py

Now any time you start up Terminal, simply type 

click_sites.py

and the program will run on its own. There is no need to monitor the program as it will simply click through the relevant site pages on its own and then close once finished.


