package posuni7streaming.twitter;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Tuple;

import twitter4j.Status;

public class TwitterAnalyzerBolt extends BaseRichBolt {
	 
    private FileManager manager = new FileManager();
    private OutputCollector collector;
    private String[] hashtags = { "Trump", "Java", "Storm", "Bible", "Python", "Palmeiras", "Facebook", "Stranger", "Globo", "Obama" };
    private Map<String, Integer> result = new HashMap<String, Integer>();
    private static final long serialVersionUID = 8465078768241865446L;
 
    public void prepare(@SuppressWarnings("rawtypes") Map stormConf, TopologyContext context,
            OutputCollector collector) {
        this.collector = collector;
    }
 
    public void execute(Tuple tuple) {
        final Status tweet = (Status) tuple.getValueByField("status");
        for (String hashtag : hashtags) {
            if (tweet.getText().toLowerCase().contains(hashtag.toLowerCase())) {
            	if(result.keySet().contains(hashtag)) {
            		result.put(hashtag, result.get(hashtag).intValue() + 1);
            	} else {
            		result.put(hashtag,1);
            	}
            	
                try {
                    manager.writeTweet(result);
                } catch (IOException e) {
                    collector.fail(tuple);
                }
            }
        }
 
        System.out.println(result);
    }
 
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
    }
}
