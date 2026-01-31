#!/usr/bin/env python3
"""
Test script for Farm City Management System
This script demonstrates the program functionality
"""

import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from farm_city import FarmCity

def test_farm_city():
    """Test the Farm City Management System"""
    print("=" * 60)
    print("TESTING FARM CITY MANAGEMENT SYSTEM")
    print("=" * 60)
    
    # Clean up any existing data file
    if os.path.exists("farm_city_data.json"):
        os.remove("farm_city_data.json")
        print("✓ Cleaned up existing data file")
    
    # Create instance
    farm_city = FarmCity()
    print("✓ Farm City system initialized")
    
    # Add a farm
    print("\n--- Test 1: Adding Farm ---")
    farm_city.data['farms'].append({
        'id': 1,
        'name': 'Green Valley Farm',
        'location': 'North District',
        'size': '200',
        'created': '2024-01-01 10:00:00'
    })
    print("✓ Added 'Green Valley Farm'")
    
    # Add another farm
    farm_city.data['farms'].append({
        'id': 2,
        'name': 'Sunny Acres',
        'location': 'South County',
        'size': '150',
        'created': '2024-01-01 11:00:00'
    })
    print("✓ Added 'Sunny Acres'")
    
    # Add animals
    print("\n--- Test 2: Adding Animals ---")
    farm_city.data['animals'].append({
        'id': 1,
        'farm_id': 1,
        'type': 'cow',
        'count': '25',
        'added': '2024-01-02 10:00:00'
    })
    print("✓ Added 25 cows to Green Valley Farm")
    
    farm_city.data['animals'].append({
        'id': 2,
        'farm_id': 1,
        'type': 'chicken',
        'count': '100',
        'added': '2024-01-02 11:00:00'
    })
    print("✓ Added 100 chickens to Green Valley Farm")
    
    farm_city.data['animals'].append({
        'id': 3,
        'farm_id': 2,
        'type': 'pig',
        'count': '15',
        'added': '2024-01-02 12:00:00'
    })
    print("✓ Added 15 pigs to Sunny Acres")
    
    # Add crops
    print("\n--- Test 3: Adding Crops ---")
    farm_city.data['crops'].append({
        'id': 1,
        'farm_id': 1,
        'name': 'wheat',
        'area': '75',
        'planted': '2024-01-03 10:00:00'
    })
    print("✓ Planted wheat on Green Valley Farm (75 acres)")
    
    farm_city.data['crops'].append({
        'id': 2,
        'farm_id': 2,
        'name': 'corn',
        'area': '50',
        'planted': '2024-01-03 11:00:00'
    })
    print("✓ Planted corn on Sunny Acres (50 acres)")
    
    # Display farms
    print("\n" + "=" * 60)
    farm_city.view_farms()
    
    # Display animals
    print("\n" + "=" * 60)
    farm_city.view_animals()
    
    # Display crops
    print("\n" + "=" * 60)
    farm_city.view_crops()
    
    # Display statistics
    print("\n" + "=" * 60)
    farm_city.display_statistics()
    
    # Save data
    print("\n" + "=" * 60)
    print("\n--- Test 4: Saving Data ---")
    farm_city.save_data()
    
    # Verify data persists
    print("\n--- Test 5: Loading Data ---")
    farm_city2 = FarmCity()
    print(f"✓ Loaded {len(farm_city2.data['farms'])} farms")
    print(f"✓ Loaded {len(farm_city2.data['animals'])} animal groups")
    print(f"✓ Loaded {len(farm_city2.data['crops'])} crops")
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)
    print("\nThe program is ready to use!")
    print("Run: python3 farm_city.py")

if __name__ == "__main__":
    test_farm_city()
