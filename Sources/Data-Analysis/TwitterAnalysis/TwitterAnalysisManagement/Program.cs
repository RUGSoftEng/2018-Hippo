using Microsoft.AspNetCore;
using Microsoft.AspNetCore.Hosting;

using TwitterRealtimeAPI;

namespace TwitterAnalysisManagement
{
    public class Program
    {
        public static TwitterDataStreamer DataStreamer { get; set; }
        
        public static void Main(string[] args)
        {
            DataStreamer = new TwitterDataStreamer();
            
            BuildWebHost(args).Run();
        }

        public static IWebHost BuildWebHost(string[] args) =>
            WebHost.CreateDefaultBuilder(args)
                .UseStartup<Startup>()
                .Build();
    }
}