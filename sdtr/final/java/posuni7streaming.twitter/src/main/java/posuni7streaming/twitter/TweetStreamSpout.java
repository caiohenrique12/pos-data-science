package posuni7streaming.twitter;

import java.util.Map;
import java.util.concurrent.LinkedBlockingQueue;

import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichSpout;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.apache.storm.utils.Utils;

import twitter4j.FilterQuery;
import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.conf.ConfigurationBuilder;

public class TweetStreamSpout extends BaseRichSpout {

	private SpoutOutputCollector collector;

	private LinkedBlockingQueue<Status> queue;
	private TwitterStream twitterStream;
	private String[] hashtags = { "Trump", "Java", "Storm", "Bible", "Python", "Palmeiras", "Facebook", "Stranger", "Globo", "Obama" };
	private static final long serialVersionUID = 4256154244602991768L;

	public void nextTuple() {
		final Status status = queue.poll();
		if (status == null) {
			Utils.sleep(50);
		} else {
			collector.emit(new Values(status));
		}
	}

	public void open(@SuppressWarnings("rawtypes") Map map, TopologyContext context, SpoutOutputCollector collector) {
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true).setOAuthConsumerKey("")
				.setOAuthConsumerSecret("")
				.setOAuthAccessToken("")
				.setOAuthAccessTokenSecret("");
		this.collector = collector;
		this.twitterStream = new TwitterStreamFactory(cb.build()).getInstance();
		this.queue = new LinkedBlockingQueue<>();
		StatusListener listener = new StatusListener() {

			public void onStatus(Status status) {
				queue.offer(status);
			}

			public void onDeletionNotice(StatusDeletionNotice sdn) {
			}

			public void onTrackLimitationNotice(int i) {
			}

			public void onScrubGeo(long l, long l1) {
			}

			public void onException(Exception e) {
			}

			public void onStallWarning(StallWarning warning) {
			}
		};
		twitterStream.addListener(listener);
		FilterQuery filterQuery = new FilterQuery();

		for (String hashtag : hashtags) {
			filterQuery.track(hashtag);
		}

		twitterStream.filter(filterQuery);
	}

	@Override
	public void activate() {
	};

	@Override
	public void deactivate() {
		twitterStream.cleanUp();
	};

	@Override
	public void close() {
		twitterStream.shutdown();
	}

	public void declareOutputFields(OutputFieldsDeclarer declarer) {
		declarer.declare(new Fields("status"));
	}
}
