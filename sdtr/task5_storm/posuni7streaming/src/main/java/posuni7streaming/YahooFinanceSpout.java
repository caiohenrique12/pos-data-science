package posuni7streaming;

import java.math.BigDecimal;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Map;

import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichSpout;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;

import yahoofinance.Stock;
import yahoofinance.YahooFinance;
import yahoofinance.quotes.stock.StockQuote;

public class YahooFinanceSpout extends BaseRichSpout {

	private SpoutOutputCollector collector;
	private SimpleDateFormat sdf = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss");

	public void open(Map conf, TopologyContext context, SpoutOutputCollector collector) {
		this.collector = collector;
	}

	public void nextTuple() {
		try {
			Stock d = YahooFinance.get("MSFT");
			StockQuote quote = YahooFinance.get("MSFT").getQuote();
			Double price = quote.getPrice().doubleValue();
			Timestamp timestamp = new Timestamp(System.currentTimeMillis());
			Double prevClose = quote.getPreviousClose().doubleValue();
			Double gain = price - prevClose;
			collector.emit(new Values("MSFT", sdf.format(timestamp), price, prevClose, gain));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public void declareOutputFields(OutputFieldsDeclarer declarer) {
		declarer.declare( new Fields("company", "timestamp", "price", "prev_close", "gain"));
	}

}
