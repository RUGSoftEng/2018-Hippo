package com.rug.hippo;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteDataStreamer;
import org.apache.ignite.stream.twitter.OAuthSettings;
import org.apache.ignite.stream.twitter.TwitterStreamer;

import java.util.Map;

public class TwitterConnection
{
    private Ignite ignite;
    private TwitterStreamer<Integer, String> streamer;
    private IgniteDataStreamer<Integer, String> dataStreamer;
    
    public TwitterConnection(Ignite ignite, String cacheName)
    {
        this.ignite = ignite;
        
        dataStreamer = ignite.dataStreamer(cacheName);
        
        dataStreamer.allowOverwrite(true);
        dataStreamer.autoFlushFrequency(10);
    }
    
    public void SetConfiguration(OAuthSettings oAuthSettings, String endpointUrl, Map<String, String> parameters)
    {
        streamer = new TwitterStreamer<>(oAuthSettings);
        
        streamer.setIgnite(ignite);
        streamer.setStreamer(dataStreamer);
        streamer.setApiParams(parameters);
        streamer.setEndpointUrl(endpointUrl);
    }
    
    public void Start()
    {
        Start(8);
    }

    public void Start(int threadCount)
    {
        streamer.setThreadsCount(threadCount);
        streamer.start();
    }
    
    public void Stop()
    {
        streamer.stop();
    }
}
