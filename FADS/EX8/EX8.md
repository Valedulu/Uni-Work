# 1. Identify if an API is available

| Platform | URL | Path to API information | Documentation URL |
|----------|-----|------------------------|-------------------|
| GBIF | https://www.gbif.org/ | Home → Developers → API | https://techdocs.gbif.org/en/openapi/ |
| Eurostat | https://ec.europa.eu/eurostat/ | Home → Data → API | https://ec.europa.eu/eurostat/web/user-guides/browser/api-data-access/api-introduction |
| INE | https://www.ine.pt/ | Home → Database → API | https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_api&INST=322751522 |
| Climate Data Store | https://cds.climate.copernicus.eu/ | Home → Toolbox → API | https://cds.climate.copernicus.eu/how-to-api |
| Copernicus Data Space Ecosystem | https://dataspace.copernicus.eu/ | Home → Analyse → APIs | https://documentation.dataspace.copernicus.eu |
| WMO | https://worldweather.wmo.int/en/home.html | Home → Download | https://worldweather.wmo.int/en/dataguide.htm |
| Agri4Cast | https://agri4cast.jrc.ec.europa.eu/DataPortal/ | Data Portal (no public API documented) | http://agri4cast.jrc.ec.europa.eu/
| European Environment Agency | https://www.eea.europa.eu/ | Home → Code → API | https://www.eea.europa.eu/code/api |



# 2. Use web scraping

## 2.1 How to Detect Hidden Data in a Website

### Methods to Identify Hidden APIs

#### Browser Developer Tools (F12)
- Open Network tab before interacting with the page
- Filter by XHR/Fetch requests
- Look for API calls when downloading data or loading charts
- Examine request URLs, headers, and payloads

#### Inspect Page Source
- Look for embedded JSON data in `<script>` tags
- Search for API endpoints in JavaScript files
- Check for data attributes in HTML elements

#### Look for Patterns
- XLSX downloads often use hidden API endpoints
- Check the URL structure when triggering downloads
- Parameters in URLs reveal API structure (e.g., `stationId`, `startDate`, `pollutant`)

### Signs of Hidden Data
- Dynamic content loading without page refresh
- Download buttons that don't link to static files
- Interactive charts/maps that update based on selections
- JSON or XML responses in Network tab

---

## 2.2 Manual vs Automatic Web Scraping

### When to Do Steps Manually
- One-time data extraction
- Small dataset (< 100 records)
- Complex CAPTCHA or authentication
- Exploring data structure for the first time
- When automation is blocked or prohibited

### When to Automate
- Regular/periodic data collection
- Large datasets requiring many requests
- Data from multiple stations/parameters
- Time-series analysis requiring historical data
- When data structure is well understood

### Exemple of Decision Framework

```
Time to develop automation > Time for manual extraction? → Manual
Need repeated updates? → Automate
Data volume > 1000 records? → Automate
Learning exercise? → Try both approaches
```

---

## 2.3 Advantages and Disadvantages of Web Scraping

### Advantages
- Access to publicly displayed but not downloadable data
- Automation of repetitive tasks
- Ability to collect large datasets efficiently
- Create custom datasets for specific research needs
- Update data regularly without manual intervention

### Disadvantages

#### Legal/Ethical
- May violate Terms of Service
- Copyright concerns with scraped data
- Server load and bandwidth usage

#### Technical
- Website structure changes break scrapers
- Rate limiting and IP blocking
- CAPTCHA and anti-bot measures
- JavaScript-rendered content
- Need for maintenance and updates

#### Data Quality
- No guaranteed data format
- Potential for incomplete data
- Lack of metadata/documentation

---

## 2.4 Web Scraping vs API Access

### When to Prefer APIs
- Available and well-documented
- Need guaranteed data structure
- Long-term project requiring stability
- Large-scale data extraction
- Official support and updates

### When Web Scraping is Acceptable
- No API available
- API is rate-limited or expensive
- Need data not exposed through API
- Short-term research project
- Public data with no access restrictions

### Comparison Table

| Aspect | Web Scraping | Official API |
|--------|--------------|--------------|
| **Legality** | Gray area, check ToS | Explicitly permitted |
| **Reliability** | Breaks with site changes | Stable, versioned |
| **Data Quality** | Variable, needs cleaning | Structured, validated |
| **Rate Limits** | Unclear, risk of blocking | Clearly defined |
| **Documentation** | Self-documented | Official docs |
| **Maintenance** | High (adapt to changes) | Low (stable interface) |
| **Performance** | Slower (HTML parsing) | Faster (direct data) |
| **Authentication** | Often complex | Standard (API keys) |

---
# 3. SASSCAL WeatherNET Planning Exercise

About SASSCAL WeatherNET
SASSCAL (Southern African Science Service Centre for Climate Change and Adaptive Land Management) operates 160+ Automatic Weather Stations across Angola, Botswana, Namibia, South Africa, and Zambia.
Data Available:

- Air temperature
- Rainfall
- Humidity
- Wind speed and direction
- Barometric pressure
- Solar radiation
- Soil temperature and moisture
- Leaf wetness


## Planning Web Scraping for SASSCAL
###  3.1 Legal and Ethical Considerations
Can I legally scrape SASSCAL data?
YES, with caveats:

Public Access: Data is publicly available without authentication
Research Purpose: SASSCAL supports scientific research
No Explicit Prohibition: No robots.txt restrictions or ToS against scraping
Ethical Consideration: Contact data team for bulk requests:
 -  oadc-datarequest@sasscal.org

Important Note from Research:
A published academic paper (Data Science Journal, 2021) actually developed a Web Scraping API (WebSAPI) for SASSCAL data, indicating that scraping is academically acceptable. However, the paper notes: "For data requests regarding specific countries, stations, time periods or specific sensors please contact 

- oadc-datarequest@sasscal.org"

Best Practices:
Respect rate limits (add delays between requests)
Use appropriate User-Agent headers
Don't overload servers
Consider contacting SASSCAL for large datasets
Give attribution when publishing results


### 3.2 Available Information for Web Scraping
- Station Identifiers:

Station names (e.g., "Gobabeb", "Windhoek")
Geographic coordinates (latitude, longitude)
Country codes (Angola, Botswana, Namibia, South Africa, Zambia)
Station IDs (internal database identifiers)

- Temporal Parameters:

Time resolution: 15-minute or hourly intervals
Date ranges: Historical data available since 2009
Data formats: Hourly, daily, monthly aggregations

- Weather Parameters:

Temperature (air, soil)
Precipitation (rainfall)
Humidity
Wind (speed, direction)
Pressure
Solar radiation
Additional sensors (leaf wetness, fog, dew point)

- Data Quality Indicators:

Automated quality control flags
Last transmission time
Station status (active/inactive)


### 3.3 Web Scraping Strategy
URL Structure to Investigate:
Base URL: https://sasscalweathernet.org/
Station page: /station/[station-id]/
Data views: /hourly/, /daily/, /monthly/
Data download: /data/
Information to Extract:

- Station Metadata:

Station ID
Name
Location (lat/lon)
Elevation
Country
Installation date
Status


- Time Series Data:

Timestamp
All measured parameters
Quality flags
Data gaps

**Implementation Plan:**

```python
# Step 1: Get list of all stations
def get_station_list():
    """Scrape main page for station IDs and metadata"""
    pass

# Step 2: For each station, extract data
def get_station_data(station_id, start_date, end_date, resolution='hourly'):
    """Extract time series data for specific station"""
    pass

# Step 3: Handle pagination and date ranges
def download_all_data(station_ids, date_range):
    """Batch download with rate limiting"""
    import time
    for station in station_ids:
        data = get_station_data(station, date_range)
        time.sleep(2)  # Polite delay
    pass
```
