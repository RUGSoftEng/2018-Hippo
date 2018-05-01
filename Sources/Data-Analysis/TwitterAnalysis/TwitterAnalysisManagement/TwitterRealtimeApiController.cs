using Microsoft.AspNetCore.Mvc;

using TwitterRealtimeAPI;

namespace TwitterAnalysisManagement
{
    public class TwitterRealtimeApiController : Controller
    {
        public IActionResult Authenticate(OAuthCredential oAuthCredential)
        {
            Program.DataStreamer.Authenticate(oAuthCredential);
            
            return Ok();
        }
        
        public IActionResult Start(string filterQuery)
        {
            Program.DataStreamer.Start(filterQuery);
            
            return Ok();
        }
    }
}