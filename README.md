

# YouTua

YouTua is a GUI Program to download videos from YouTube.com and a few more sites. It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform specific. It should work on your Unix box, on Windows or on macOS. It is released to the public domain, which means you can modify it, redistribute it or use it however you like.

<p align="center">
	<img src="https://user-images.githubusercontent.com/72680045/103451856-34b36980-4cef-11eb-9f8d-231d7654f5ca.PNG">
</p>
<br>

## Setup:

1. Install Python
2. Clone this repository
```
git clone https://github.com/dhhruv/YouTua.git
```

3. Install, create and activate virtual environment.
For instance we create a virtual environment named 'venv'.
```
pip install virtualenv
python -m virtualenv venv
venv\Scripts\activate.bat
```

4. Install dependencies
```
pip install -r requirements.txt
```


## How To Use !
1. Select the OUTPUT Folder by manually adding path or selecting the FOLDER using the SELECT FOLDER Button.<br>
(By Default the OUTPUT FOLDER is set to the current directory.)
2. Enter the Link of Youtube Video you want to download.
3. By Clicking START DOWNLOAD, YouTua will download the video in the best available quality (MAX=720p) and subtitles will be download if available.<br>
Note:- This is a Pre-release so STOP Button is under implementation.<br>
P.S. Wait until the video is downloaded.

## Important Note:

-	**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. Read the [LICENSE](https://github.com/dhhruv/YouTua/blob/master/LICENSE) for more information.**

## Credits:
- [youtube-dl](http://ytdl-org.github.io/youtube-dl/download.html)