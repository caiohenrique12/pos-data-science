package posuni7streaming.twitter;

import java.io.PrintWriter;
import java.util.Map;

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Tuple;

import twitter4j.Status;

public class TwitterBolt extends BaseBasicBolt {

	private PrintWriter writer;
	private String[] words = { "Pizza", "Brasil", "Peru", "America", "Copa", "Seleção", "Neymar", "Palmeiras",
			"Brasileirão", "Globo" };
	private OutputCollector collector;

	public void prepare(@SuppressWarnings("rawtypes") Map stormConf, TopologyContext context,
			OutputCollector collector) {
		this.collector = collector;
	}

	public void execute(Tuple tuple, BasicOutputCollector basicOutputCollector) {
		final Status tweet = (Status) tuple.getValueByField("status");
		for (String word : words) {
			if (tweet.getText().toLowerCase().contains(word)) {
				writer.println(word);
			}
		}
	}

	public void declareOutputFields(OutputFieldsDeclarer outputFieldsDeclarer) {
	}

	public void cleanup() {
		writer.close();
	}
}
