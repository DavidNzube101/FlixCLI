# FlixCLI

FlixCLI is a command-line tool that allows you to download media files (images, videos, and audios) from a given website URL.

## Features
- Scans a website for media files with common extensions (`.jpg`, `.mp4`, `.mp3`, etc.)
- Allows the user to select which media files to download
- Downloads the selected files to a `downloads` directory within the project

## Prerequisites
- Java Development Kit (JDK) 11 or later
- Maven

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/DavidNzube101/FlixCLI.git
   ```
2. Navigate to the project directory:
   ```
   cd FlixCLI
   ```
3. Install the required dependencies using Maven:
   ```
   mvn install
   ```

## Usage
1. Run the Python script:
   ```
   python flixcli.py -d
   ```
2. When prompted, enter the URL of the website containing the media files you want to download.
3. Select the files you want to download by entering the corresponding numbers (separated by commas).
4. The selected files will be downloaded to the `downloads` directory within the project.

## Example
```
$ python flixcli.py -d
Enter the URL to scrape media files from: https://example.com

Found Media Files:
1. https://example.com/image1.jpg
2. https://example.com/video1.mp4
3. https://example.com/audio1.mp3

Enter the numbers of files to download (comma-separated): 1,3

Downloaded: image1.jpg
Downloaded: audio1.mp3
```

## Development
The project is structured as a Maven-based Java project with a Python CLI. The Java script handles the media file downloading logic, while the Python script provides the command-line interface and integrates with the Java script.

To run the project in development:
1. Compile and run the Java script using Maven:
   ```
   mvn compile
   mvn exec:java -Dexec.mainClass="com.skipp.flixcore.flixcore"
   ```
2. Run the Python script:
   ```
   python flixcli.py -d
   ```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).