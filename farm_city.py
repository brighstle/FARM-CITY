#!/usr/bin/env python3
"""
Farm City Management System
A simple program to manage farms, animals, and crops
"""

import json
import os
from datetime import datetime


class FarmCity:
    """Main class for managing the Farm City system"""
    
    def __init__(self):
        self.data_file = "farm_city_data.json"
        self.data = self.load_data()
    
    def load_data(self):
        """Load data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Warning: Could not read data file. Starting fresh.")
        
        return {
            'farms': [],
            'animals': [],
            'crops': []
        }
    
    def save_data(self):
        """Save data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
        print("Data saved successfully!")
    
    def add_farm(self):
        """Add a new farm"""
        print("\n--- Add New Farm ---")
        name = input("Farm name: ").strip()
        if not name:
            print("Error: Farm name cannot be empty!")
            return
        
        location = input("Location: ").strip()
        size = input("Size (in acres): ").strip()
        
        farm = {
            'id': len(self.data['farms']) + 1,
            'name': name,
            'location': location,
            'size': size,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.data['farms'].append(farm)
        print(f"✓ Farm '{name}' added successfully!")
    
    def view_farms(self):
        """Display all farms"""
        print("\n--- Farms List ---")
        if not self.data['farms']:
            print("No farms registered yet.")
            return
        
        for farm in self.data['farms']:
            print(f"\nID: {farm['id']}")
            print(f"Name: {farm['name']}")
            print(f"Location: {farm['location']}")
            print(f"Size: {farm['size']} acres")
            print(f"Created: {farm['created']}")
            print("-" * 40)
    
    def add_animal(self):
        """Add a new animal"""
        print("\n--- Add New Animal ---")
        
        if not self.data['farms']:
            print("Error: Please add a farm first!")
            return
        
        print("Available farms:")
        for farm in self.data['farms']:
            print(f"  {farm['id']}. {farm['name']}")
        
        try:
            farm_id = int(input("Select farm ID: "))
            if not any(f['id'] == farm_id for f in self.data['farms']):
                print("Error: Invalid farm ID!")
                return
        except ValueError:
            print("Error: Please enter a valid number!")
            return
        
        animal_type = input("Animal type (e.g., cow, chicken, pig): ").strip()
        count = input("Number of animals: ").strip()
        
        animal = {
            'id': len(self.data['animals']) + 1,
            'farm_id': farm_id,
            'type': animal_type,
            'count': count,
            'added': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.data['animals'].append(animal)
        print(f"✓ {count} {animal_type}(s) added successfully!")
    
    def view_animals(self):
        """Display all animals"""
        print("\n--- Animals List ---")
        if not self.data['animals']:
            print("No animals registered yet.")
            return
        
        for animal in self.data['animals']:
            farm = next((f for f in self.data['farms'] if f['id'] == animal['farm_id']), None)
            farm_name = farm['name'] if farm else "Unknown"
            
            print(f"\nID: {animal['id']}")
            print(f"Type: {animal['type']}")
            print(f"Count: {animal['count']}")
            print(f"Farm: {farm_name}")
            print(f"Added: {animal['added']}")
            print("-" * 40)
    
    def add_crop(self):
        """Add a new crop"""
        print("\n--- Add New Crop ---")
        
        if not self.data['farms']:
            print("Error: Please add a farm first!")
            return
        
        print("Available farms:")
        for farm in self.data['farms']:
            print(f"  {farm['id']}. {farm['name']}")
        
        try:
            farm_id = int(input("Select farm ID: "))
            if not any(f['id'] == farm_id for f in self.data['farms']):
                print("Error: Invalid farm ID!")
                return
        except ValueError:
            print("Error: Please enter a valid number!")
            return
        
        crop_name = input("Crop name (e.g., wheat, corn, tomatoes): ").strip()
        area = input("Area planted (in acres): ").strip()
        
        crop = {
            'id': len(self.data['crops']) + 1,
            'farm_id': farm_id,
            'name': crop_name,
            'area': area,
            'planted': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.data['crops'].append(crop)
        print(f"✓ Crop '{crop_name}' planted successfully!")
    
    def view_crops(self):
        """Display all crops"""
        print("\n--- Crops List ---")
        if not self.data['crops']:
            print("No crops planted yet.")
            return
        
        for crop in self.data['crops']:
            farm = next((f for f in self.data['farms'] if f['id'] == crop['farm_id']), None)
            farm_name = farm['name'] if farm else "Unknown"
            
            print(f"\nID: {crop['id']}")
            print(f"Name: {crop['name']}")
            print(f"Area: {crop['area']} acres")
            print(f"Farm: {farm_name}")
            print(f"Planted: {crop['planted']}")
            print("-" * 40)
    
    def display_statistics(self):
        """Display system statistics"""
        print("\n--- Farm City Statistics ---")
        print(f"Total Farms: {len(self.data['farms'])}")
        print(f"Total Animals: {len(self.data['animals'])}")
        print(f"Total Crops: {len(self.data['crops'])}")
        
        if self.data['animals']:
            total_animal_count = sum(int(a.get('count', '0')) for a in self.data['animals'] if a.get('count', '0').isdigit())
            print(f"Total Animal Count: {total_animal_count}")
        
        if self.data['crops']:
            total_crop_area = sum(float(c.get('area', '0')) for c in self.data['crops'] if c.get('area', '0').replace('.', '', 1).isdigit())
            print(f"Total Crop Area: {total_crop_area} acres")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "=" * 50)
        print("       FARM CITY MANAGEMENT SYSTEM")
        print("=" * 50)
        print("\n1. Add Farm")
        print("2. View Farms")
        print("3. Add Animal")
        print("4. View Animals")
        print("5. Add Crop")
        print("6. View Crops")
        print("7. View Statistics")
        print("8. Save Data")
        print("9. Exit")
        print("-" * 50)
    
    def run(self):
        """Main program loop"""
        print("\nWelcome to Farm City Management System!")
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-9): ").strip()
            
            if choice == '1':
                self.add_farm()
            elif choice == '2':
                self.view_farms()
            elif choice == '3':
                self.add_animal()
            elif choice == '4':
                self.view_animals()
            elif choice == '5':
                self.add_crop()
            elif choice == '6':
                self.view_crops()
            elif choice == '7':
                self.display_statistics()
            elif choice == '8':
                self.save_data()
            elif choice == '9':
                save = input("Save data before exiting? (y/n): ").strip().lower()
                if save == 'y':
                    self.save_data()
                print("\nThank you for using Farm City Management System!")
                print("Goodbye!")
                break
            else:
                print("\nError: Invalid choice! Please enter a number between 1-9.")
            
            input("\nPress Enter to continue...")


def main():
    """Entry point for the program"""
    farm_city = FarmCity()
    farm_city.run()


if __name__ == "__main__":
    main()
