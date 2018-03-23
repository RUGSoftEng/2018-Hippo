package com.rug.hippo;

import org.apache.ignite.*;
import org.apache.ignite.stream.twitter.*;

import java.util.*;

public class App 
{
    public static void main(String[] args)
    {
        Ignite ignite = null;
        
        IgniteDataStreamer<Integer, String> dataStreamer = ignite.dataStreamer("myCache");
        dataStreamer.allowOverwrite(true);
        dataStreamer.autoFlushFrequency(10);

        OAuthSettings oAuthSettings = new OAuthSettings("<>", "<>", "<>", "<>");

        TwitterStreamer<Integer, String> streamer = new TwitterStreamer<>(oAuthSettings);
        streamer.setIgnite(ignite);
        streamer.setStreamer(dataStreamer);

        Map<String, String> params = new HashMap<>();
        params.put("track", "apache, twitter");
        params.put("follow", "3004445758");

        streamer.setApiParams(params);// Twitter Streaming API params.
        streamer.setEndpointUrl(endpointUrl);// Twitter streaming API endpoint.
        streamer.setThreadsCount(8);

        streamer.start();
    }
}
