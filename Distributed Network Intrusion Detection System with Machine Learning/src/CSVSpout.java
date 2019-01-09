package storm.IDS.spout;

import backtype.storm.spout.SpoutOutputCollector;
import backtype.storm.task.TopologyContext;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.topology.base.BaseRichSpout;
import backtype.storm.tuple.Fields;
import backtype.storm.tuple.Values;
import backtype.storm.utils.Utils;

import java.util.Map;
import java.util.Random;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class CSVSpout extends BaseRichSpout {
  SpoutOutputCollector _collector;
  FileReader file = new FileReader();
  BufferedReader br = null;
  String cvsSplitBy = ",";


  @Override
  public void open(Map conf, TopologyContext context, SpoutOutputCollector collector) {
    _collector = collector;
    String csvFile = "/home/student/storm/apache-storm-0.10.0/project/data/testData.csv";

	try {
		br = new BufferedReader(new FileReader(csvFile));
		}

	} catch (FileNotFoundException e) {
		e.printStackTrace();
	} catch (IOException e) {
		e.printStackTrace();
	} finally {
		if (br != null) {
			try {
				br.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

  }

  @Override
  public void nextTuple() {
		while ((line = br.readLine()) != null) {
		        // use comma as separator
			String[] packet = line.split(cvsSplitBy);
	} 
		
   _collector.emit(new Values(packet));
  }

  @Override
  public void ack(Object id) {
  }

  @Override
  public void fail(Object id) {
  }

  @Override
  public void declareOutputFields(OutputFieldsDeclarer declarer) {
    declarer.declare(new Fields("packet"));
  }

}
