package posuni7streaming;

import java.io.PrintWriter;
import java.util.Map;

import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

public class YahooFinanceBolt extends BaseBasicBolt {

	private PrintWriter writer;

	public void prepare(Map stormConf, TopologyContext topologyContext) {
		String fileName = stormConf.get("output").toString();
		try {
			this.writer = new PrintWriter(fileName, "UTF-8");
		} catch (Exception e) {
			throw new RuntimeException("Error Opening File " + fileName);
		}
	}

	public void execute(Tuple tuple, BasicOutputCollector basicOutputCollector) {
		String symbol = tuple.getValue(0).toString();
		String timeStamp = tuple.getString(1);
		Double price = tuple.getDoubleByField("price");
		Double prevClose = tuple.getDoubleByField("prev_close");
		Double gain = tuple.getDoubleByField("gain");
		basicOutputCollector.emit(new Values(symbol, timeStamp, price));
		writer.println("COMPANY: " + symbol + " | DATETIME: " + timeStamp + " | PRICE: " + price + " | PREV: " + prevClose + " | GAIN: " + gain);
	}

	public void declareOutputFields(OutputFieldsDeclarer outputFieldsDeclarer) {
		outputFieldsDeclarer.declare(new Fields("company", "timestamp", "price", "prev_close", "gain"));
	}

	public void cleanup() {
		writer.close();
	}
}
