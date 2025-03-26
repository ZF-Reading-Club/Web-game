
from src.repositories.buildings_repository import BuildingsRepository


class BuildingService:
    
    def get_building(self, building_type):
        """
        Get building by type.
        """
        return BuildingsRepository(building_type).get_building_data()
    
    def add_building(self, building_type, price, size):
        """
        Add building to the database.
        """
        BuildingsRepository(building_type, price, size).set_building_data()
    
    def delete_building(self, building_id):
        """
        Delete building from the database.
        """
        BuildingsRepository(building_id).delete_building()    