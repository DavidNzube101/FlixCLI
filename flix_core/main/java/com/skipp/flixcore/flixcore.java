package flix_core.main.java.com.skipp.flixcore;
import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.util.*;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class flixcore {
    private String baseUrl;
    private static final List<String> MEDIA_EXTENSIONS = Arrays.asList(
        // Image extensions
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp",
        // Video extensions
        ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv",
        // Audio extensions
        ".mp3", ".wav", ".flac", ".aac", ".ogg"
    );

    public flixcore(String baseUrl) {
        this.baseUrl = baseUrl;
    }

    public List<String> findMediaFiles() {
        List<String> mediaFiles = new ArrayList<>();
        try {
            // Connect to the URL
            Document doc = Jsoup.connect(baseUrl)
                .userAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
                .get();

            // Find all links
            Elements links = doc.select("a[href]");
            for (Element link : links) {
                String href = link.attr("abs:href");
                
                // Check if the URL ends with media extensions
                if (MEDIA_EXTENSIONS.stream().anyMatch(href.toLowerCase()::endsWith)) {
                    mediaFiles.add(href);
                }
            }
        } catch (IOException e) {
            System.err.println("Error fetching URL: " + e.getMessage());
        }
        return mediaFiles;
    }

    public void downloadMedia(List<String> mediaFiles, String outputDir) {
        // Create output directory if it doesn't exist
        try {
            Files.createDirectories(Paths.get(outputDir));
        } catch (IOException e) {
            System.err.println("Error creating output directory: " + e.getMessage());
            return;
        }

        for (String fileUrl : mediaFiles) {
            try {
                URL url = new URL(fileUrl);
                String fileName = Paths.get(url.getPath()).getFileName().toString();
                Path outputPath = Paths.get(outputDir, fileName);

                try (InputStream in = url.openStream()) {
                    Files.copy(in, outputPath, StandardCopyOption.REPLACE_EXISTING);
                    System.out.println("Downloaded: " + fileName);
                }
            } catch (IOException e) {
                System.err.println("Error downloading " + fileUrl + ": " + e.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Get URL from user
        System.out.print("Enter the URL to scrape media files from: ");
        String url = scanner.nextLine();
        
        // Create downloader
        flixcore downloader = new flixcore(url);
        
        // Find media files
        List<String> mediaFiles = downloader.findMediaFiles();
        
        if (mediaFiles.isEmpty()) {
            System.out.println("No media files found.");
            return;
        }
        
        // Display media files
        System.out.println("\nFound Media Files:");
        for (int i = 0; i < mediaFiles.size(); i++) {
            System.out.println((i + 1) + ". " + mediaFiles.get(i));
        }
        
        // Select files to download
        System.out.print("\nEnter the numbers of files to download (comma-separated): ");
        String selections = scanner.nextLine();
        
        List<String> selectedFiles = new ArrayList<>();
        for (String selection : selections.split(",")) {
            int index = Integer.parseInt(selection.trim()) - 1;
            selectedFiles.add(mediaFiles.get(index));
        }
        
        // Download selected files
        downloader.downloadMedia(selectedFiles, "downloads");
        
        scanner.close();
    }
}