package com.rug.hippo;

import com.sun.org.apache.bcel.internal.generic.RETURN;
import org.apache.ignite.*;
import org.apache.ignite.configuration.DataStorageConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;

public class App 
{
    public static void main(String[] args)
    {
        IgniteConfiguration configuration = GetConfiguration();
        Ignite ignite = Ignition.start(configuration);
        
        TwitterConnection twitterConnection = new TwitterConnection(ignite, "Tweets");
        
        twitterConnection.SetConfiguration(null, null, null);
        twitterConnection.Start();
    }
    
    private static IgniteConfiguration GetConfiguration()
    {
        IgniteConfiguration cfg = new IgniteConfiguration();
        DataStorageConfiguration storageCfg = new DataStorageConfiguration();

        storageCfg.getDefaultDataRegionConfiguration().setPersistenceEnabled(true);

        cfg.setDataStorageConfiguration(storageCfg);

        return cfg;
    }
}
