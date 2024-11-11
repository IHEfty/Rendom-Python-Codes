# Phone Number Location Tracker

This Python project allows users to input a phone number and retrieves location information associated with that number. It utilizes the `phonenumbers` library for parsing phone numbers, the OpenCage Geocoder for obtaining geographical coordinates, and the Google Maps API for retrieving detailed addresses and generating a map.

## Features

- Parse and validate phone numbers.
- Retrieve the location description and service provider for a given phone number.
- Obtain geographical coordinates (latitude and longitude) of the location.
- Use Google Maps API to get a detailed address.
- Generate a map with a marker indicating the location.
- Save the map to an HTML file for easy viewing.

## Requirements

- Python 3.x
- `phonenumbers` library
- `folium` library
- `requests` library
- `opencage` library

You can install the required libraries using pip:

```bash
pip install phonenumbers 
pip install folium 
pip install requests 
pip install opencage 
```

## Setup

1. **Obtain API Keys:**
   - Sign up at [OpenCage](https://opencagedata.com/) to get your OpenCage API key.
   - Sign up for a Google Cloud account and enable the Google Maps Geocoding API to obtain your Google Maps API key.

2. **Update the Script:**
   - Replace the `key` variable in the script with your OpenCage API key.
   - Replace the `google_maps_key` variable with your Google Maps API key.

## Usage

Run the script in your terminal:

```bash
python track.py
```

You will be prompted to enter a phone number. The script will output:

- The location description.
- The service provider.
- The latitude and longitude of the location.
- The detailed address.
- A link to view the location on Google Maps.
- A saved HTML file (`location.html`) containing a map with the location marked.

### Example Input
```
Please give your number: +880123456****
```

### Example Output
```
Location description: Dhaka, Bangladesh
Service provider: Grameenphone
Latitude: 23.8103
Longitude: 90.4125
Detailed Address: 123 Example St, Dhaka, Bangladesh
View location on Google Maps: https://www.google.com/maps/@23.8103,90.4125,15z
Location tracking completed
```

## Acknowledgements

- Special thanks to [Ryan Okamuro](https://gist.github.com/RyanOkamuro/3829cde1b7db51a739c7ca5f11055c54#file-gistfile1-txt) for sharing the Google Maps API setup information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<!-- 78f7a0f7a7ef453a97613c548b2dee8a --> <!-- > Wooh you can use this -->
