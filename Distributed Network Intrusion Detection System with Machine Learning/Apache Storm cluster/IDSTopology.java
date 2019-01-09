package storm.IDS;

import backtype.storm.Config;
import backtype.storm.LocalCluster;
import backtype.storm.StormSubmitter;
import backtype.storm.task.ShellBolt;
import backtype.storm.topology.BasicOutputCollector;
import backtype.storm.topology.IRichBolt;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.topology.TopologyBuilder;
import backtype.storm.topology.base.BaseBasicBolt;
import backtype.storm.tuple.Fields;
import backtype.storm.tuple.Tuple;
import backtype.storm.tuple.Values;
import storm.IDS.spout.CSVSpout;
import java.util.HashMap;
import java.util.Map;

/**
 * This topology demonstrates Storm's stream groupings and multilang capabilities.
 */
public class IDSTopology {
  public static class DosBolt extends ShellBolt implements IRichBolt {

    public DosBolt() {
      super("python", "DosBolt.py");
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
      declarer.declare(new Fields(String[]));
    }
	
    @Override
    public Map<String, Object> getComponentConfiguration() {
      return null;
    }
  }
  
    public static class DDosBolt extends ShellBolt implements IRichBolt {

    public DDosBolt() {
      super("python", "DDosBolt.py");
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
      declarer.declare(new Fields(String[]));
    }
	
    @Override
    public Map<String, Object> getComponentConfiguration() {
      return null;
    }
  }

	public static class InfiltrateBolt extends ShellBolt implements IRichBolt {

    public InfiltrateBolt() {
      super("python", "InfiltrateBolt.py");
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
      declarer.declare(new Fields(String[]));
    }
	
    @Override
    public Map<String, Object> getComponentConfiguration() {
      return null;
    }
  }

   public static class BruteForceSSHBolt extends ShellBolt implements IRichBolt {

    public DDosBolt() {
      super("python", "BruteForceSSHBolt.py");
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
      declarer.declare(new Fields(String[]));
    }
	
    @Override
    public Map<String, Object> getComponentConfiguration() {
      return null;
    }
  }

  public static class AggregatorBolt extends ShellBolt implements IRichBolt {

    public AggregatorBolt() {
      super("python", "AggregatorBolt.py");
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
      //declarer.declare(new Fields("word"));
    }
	
    @Override
    public Map<String, Object> getComponentConfiguration() {
      return null;
    }
  }


  public static void main(String[] args) throws Exception {

    TopologyBuilder builder = new TopologyBuilder();

    builder.setSpout("spout", new CSVSpout(), 1);
    builder.setBolt("DosBolt", new DosBolt(), 4).shuffleGrouping("spout");
    builder.setBolt("DDosBolt", new DDosBolt(), 4).shuffleGrouping("spout");
	  builder.setBolt("InfiltrateBolt", new InfiltrateBolt(), 4).shuffleGrouping("spout");
	  builder.setBolt("BruteForceSSHBolt", new BruteForceSSHBolt(), 4).shuffleGrouping("spout");
	  builder.setBolt("AggregatorBolt",new AggregatorBolt(), 4).shuffleGrouping("DosBolt",4).shuffleGrouping("DDosBolt",4).shuffleGrouping("InfiltrateBolt",4).shuffleGrouping("BruteForceSSHBolt",4);
    Config conf = new Config();
    conf.setDebug(true);


    if (args != null && args.length > 0) {
      conf.setNumWorkers(3);
      StormSubmitter.submitTopologyWithProgressBar(args[0], conf, builder.createTopology());
    }
    else {
      conf.setMaxTaskParallelism(4);

      LocalCluster cluster = new LocalCluster();
      cluster.submitTopology("dist-IDS", conf, builder.createTopology());

      Thread.sleep(10000);

      cluster.shutdown();
    }
  }
}
