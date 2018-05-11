/*  Copyright © 2018 Jean Paul Donovan Meijer.
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License. */

using System;
using System.IO;
using System.Linq;
using System.Threading;

using Apache.Ignite.Core;
using Apache.Ignite.Core.Cache;
using Apache.Ignite.Core.Cache.Configuration;
using Apache.Ignite.Core.Configuration;
using Apache.Ignite.Core.Datastream;
using Apache.Ignite.Core.DataStructures;

using Tweetinvi;
using Tweetinvi.Events;
using Tweetinvi.Models;
using Tweetinvi.Streaming;
using Stream = Tweetinvi.Stream;

namespace TwitterRealtimeAPI
{
    public class TwitterDataStreamer
    {
        private readonly IIgnite _ignite;
        private readonly ICache<long, string> _cache;
        private readonly IDataStreamer<long, string> _dataStreamer;
        private readonly IAtomicSequence _tweetCount;

        private IFilteredStream _filteredStream;
        private OAuthCredential _oAuthCredential;
        
        public static IgniteConfiguration BuildConfiguration() =>
            new IgniteConfiguration
            {
                IgniteHome = Path.Combine(Directory.GetCurrentDirectory(), "Ignite"),
                
                DataStorageConfiguration = new DataStorageConfiguration
                {
                    DefaultDataRegionConfiguration = new DataRegionConfiguration
                    {
                        Name = "defaultRegion",
                        PersistenceEnabled = true
                    }
                },
                
                CacheConfiguration = new[]
                {
                    new CacheConfiguration
                    {
                        // Default data region has persistence enabled.
                        Name = "persistentCache"
                    }
                }
            };

        public TwitterDataStreamer()
        {
            _ignite = Ignition.Start(BuildConfiguration());
            
            _ignite.GetCluster().SetActive(true);
            
            _cache = _ignite.GetOrCreateCache<long, string>("Tweets");
            _dataStreamer = _ignite.GetDataStreamer<long, string>("Tweets");
            _dataStreamer.AutoFlushFrequency = 10;

            _tweetCount = _ignite.GetAtomicSequence("TweetCount", 0, true);

            var timer = new Timer(o => Console.WriteLine($"Total: {_cache.Count()}, Index: {_tweetCount.Read()}."), null, 100, 100);
        }

        public void Authenticate(OAuthCredential oAuthCredential)
        {
            _oAuthCredential = oAuthCredential;
            
            _oAuthCredential.Authenticate();
        }

        public void Start(string filterQuery, OAuthCredential oAuthCredential)
        {
            Authenticate(oAuthCredential);

            Start(filterQuery);
        }

        public void Start(string filterQuery)
        {
            if (_oAuthCredential == null)
            {
                Authenticate(new OAuthCredential("", "", "", ""));
            }
            
            if (_filteredStream != null && _filteredStream.StreamState != StreamState.Stop)
            {
                _filteredStream.StopStream();
            }
            
            _filteredStream = Stream.CreateFilteredStream();

            _filteredStream.AddTrack(filterQuery);

            _filteredStream.MatchingTweetReceived += StreamOnMatchingTweetReceived;
            _filteredStream.LimitReached += StreamOnLimitReached;
            _filteredStream.WarningFallingBehindDetected += StreamOnWarningFallingBehindDetected;
            _filteredStream.DisconnectMessageReceived += StreamOnDisconnectMessageReceived;
            
            _filteredStream.StartStreamMatchingAllConditions();
        }

        public void Stop()
        {
            if (_filteredStream != null && _filteredStream.StreamState != StreamState.Stop)
            {
                _filteredStream.StopStream();
            }
        }

        public void Shutdown()
        {
            if (_filteredStream != null && _filteredStream.StreamState != StreamState.Stop)
            {
                _filteredStream.StopStream();
            }

            _tweetCount.Close();
            _ignite.GetServices().CancelAll();
        }
        
        private void StreamOnMatchingTweetReceived(object sender, MatchedTweetReceivedEventArgs matchedTweetReceivedEventArgs)
        {
            var tweet = matchedTweetReceivedEventArgs.Tweet;

            _dataStreamer.AddData(_tweetCount.Increment(), tweet.ToJson());
            
            Console.WriteLine($"{_tweetCount.Read()} >>> {tweet.Text}");
        }
        
        private void StreamOnDisconnectMessageReceived(object sender, DisconnectedEventArgs disconnectedEventArgs)
        {
            var message = disconnectedEventArgs.DisconnectMessage;
            
            Console.WriteLine($"[!]: DisconnectMessageReceived >> Code={message.Code} - {message.Reason}");
        }

        private void StreamOnWarningFallingBehindDetected(object sender, WarningFallingBehindEventArgs warningFallingBehindEventArgs)
        {
            var message = warningFallingBehindEventArgs.WarningMessage;
            
            Console.WriteLine($"[!]: WarningFallingBehind >> Code={message.Code} - PercentFull={message.PercentFull}% - {message.Message}");
        }

        private void StreamOnLimitReached(object sender, LimitReachedEventArgs limitReachedEventArgs)
        {            
            Console.WriteLine($"[!]: LimitReached >> NumberOfTweetsNotReceived={limitReachedEventArgs.NumberOfTweetsNotReceived}");
        }
    }
}