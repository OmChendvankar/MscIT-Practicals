using System;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Configuration;
using Microsoft.AspNetCore.Http;
namespace helloworld
{
internal class Program
{
static void Main(string[] args)
{
var config=new ConfigurationBuilder()
.AddCommandLine(args)
.Build();
var host=new WebHostBuilder()
.UseKestrel()
.UseStartup<Startup>()
.UseUrls("http://localhost:5200/")
.UseConfiguration(config)
.Build();
host.Run();
}
}
public class Startup
{
public Startup(IHostingEnvironment env) {}
public void Configure(IApplicationBuilder app,
IHostingEnvironment env, ILoggerFactory loggerFactory)
{
app.Run(async (context) => {await
context.Response.WriteAsync("Hello, world!");});
}
}
}