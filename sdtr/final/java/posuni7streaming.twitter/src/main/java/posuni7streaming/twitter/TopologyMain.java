package posuni7streaming.twitter;

import java.io.IOException;

import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.topology.TopologyBuilder;

import twitter4j.TwitterException;

public class TopologyMain {

	public static void main(String[] args) throws InterruptedException, TwitterException, IOException {
		TopologyBuilder builder = new TopologyBuilder();
		builder.setSpout("twitterSpout", new TwitterSpout());
		builder.setBolt("twitterBolt", new TwitterBolt(), 1).shuffleGrouping("twitterSpout");

		Config conf = new Config();
		conf.setDebug(false);

		final LocalCluster cluster = new LocalCluster();
		cluster.submitTopology("twitterTopology", conf, builder.createTopology());
	}
}
