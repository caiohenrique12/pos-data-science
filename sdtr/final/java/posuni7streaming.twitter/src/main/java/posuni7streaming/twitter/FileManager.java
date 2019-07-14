package posuni7streaming.twitter;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Serializable;
import java.util.Map;

import twitter4j.Status;

public class FileManager implements Serializable {
	 
    private static final long serialVersionUID = -3987517536486344388L;
 
    public void writeTweet(Map<String, Integer> results) throws IOException {
        File file = new File("hashtags");
        if (!file.exists()) {
            file.createNewFile();
        }
 
        FileWriter fileWritter = new FileWriter(file.getName(),true);
        BufferedWriter bufferWritter = new BufferedWriter(fileWritter);
        for(Map.Entry<String, Integer>  result : results.entrySet()) {
        	bufferWritter.write("\n" + result);
        }
        bufferWritter.close();
    }
}
