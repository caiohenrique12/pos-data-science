package posuni7streaming;

import org.apache.storm.Config;
import org.apache.storm.StormSubmitter;
import org.apache.storm.generated.StormTopology;
import org.apache.storm.topology.TopologyBuilder;

public class TopologyMain {
	public static String PATH = "/home/master/output_storm.txt";

	public static void main(String[] args) throws InterruptedException {

		// Construir topology
		TopologyBuilder builder = new TopologyBuilder();
		builder.setSpout("Yahoo-Finance-Spout", new YahooFinanceSpout());
		builder.setBolt("Yahoo-Finance-Bolt", new YahooFinanceBolt()).shuffleGrouping("Yahoo-Finance-Spout");
		StormTopology topology = builder.createTopology();

		// Configurar
		Config config = new Config();
		config.setDebug(true);
		config.put("output", PATH);

		// Submeter no cluster
		//LocalCluster cluster = new LocalCluster();
		//cluster.submitTopology("Stock-Tracker-Topology", config, topology);

		try {
			StormSubmitter.submitTopology("MinhaTopology", config, topology);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
