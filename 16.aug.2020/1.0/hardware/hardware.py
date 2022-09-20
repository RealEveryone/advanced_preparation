from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

        self.free_capacity = self.capacity
        self.free_memory = self.memory

    def install(self, software: Software):
        if self.free_memory < software.memory_consumption and self.free_capacity < software.capacity_consumption:
            raise Exception('Software cannot be installed')


        self.free_capacity -= software.capacity_consumption
        self.free_memory -= software.memory_consumption
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.free_capacity += software.capacity_consumption
        self.free_memory += software.memory_consumption
        self.software_components.remove(software)

