# click-to-donate.py
Python script that automatically performs all clicks on click-to-donate website <a href= "http://www.care2.com/click-to-donate/" target="_blank">care2</a>.

NOTE: in order to run this program, you must install selenium and correctly set up the webdriver. Currently this program works only on the Google Chrome Browser; you must have Google Chrome on your computer in order for this script to work. To install selenium, go to Terminal and type

pip install selenium

and use sudo permissions if needed. Instructions for downloading the webdriver can be found <a href="https://sites.google.com/a/chromium.org/chromedriver/getting-started" target="_blank">here</a>.

After downloading the script to the desired directory my/directory/path, insert the following code (mac) to add it to the PATH variable and run it from anywhere in the terminal:

export PATH="$PATH:/usr/local/bin"
cd my/directory/path
mv click_sites.py /usr/local/bin/click_sites.py
cd /usr/local/bin
chmod +x click_sites.py

Now any time you start up Terminal, simply type 

click_sites.py

and the program will run on its own. There is no need to monitor the program as it will simply click through the relevant site pages on its own and then close once finished.


