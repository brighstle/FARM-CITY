# FARM-CITY
FARM CITY MANAGEMENT SYSTEM

## Description
A simple and intuitive command-line program to manage farms, animals, and crops in your farm city. Track multiple farms, register animals, plant crops, and view statistics all in one place.

## Features
- 🏡 **Farm Management**: Add and view farms with details like name, location, and size
- 🐄 **Animal Management**: Register animals on farms and track their counts
- 🌾 **Crop Management**: Plant and track crops across different farms
- 📊 **Statistics**: View comprehensive statistics about your farm city
- 💾 **Data Persistence**: Automatically save and load your farm data

## Requirements
- Python 3.6 or higher

## How to Run the Program

### Quick Start
```bash
python3 farm_city.py
```

Or make it executable and run directly:
```bash
chmod +x farm_city.py
./farm_city.py
```

### Usage
Once you run the program, you'll see a menu with the following options:

1. **Add Farm** - Register a new farm with name, location, and size
2. **View Farms** - Display all registered farms
3. **Add Animal** - Add animals to a specific farm
4. **View Animals** - Display all animals across farms
5. **Add Crop** - Plant crops on a farm
6. **View Crops** - Display all planted crops
7. **View Statistics** - See overall statistics
8. **Save Data** - Manually save your data
9. **Exit** - Exit the program (option to save before exiting)

### Example Workflow
1. Start by adding a farm (Option 1)
2. Add some animals to your farm (Option 3)
3. Plant some crops (Option 5)
4. View your statistics (Option 7)
5. Save your data (Option 8) or exit and save (Option 9)

## Data Storage
The program automatically saves your data to `farm_city_data.json` in the same directory. This file is created automatically and will persist your farm data between sessions.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests!

## License
This project is open source and available for educational purposes.
